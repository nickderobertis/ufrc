from enum import Enum
from typing import List, Union

from pydantic import BaseModel, Field


class MailType(str, Enum):
    NONE = "NONE"
    BEGIN = "BEGIN"
    END = "END"
    FAIL = "FAIL"
    ALL = "ALL"


class SBatchHeaders(BaseModel):
    job_name: str
    email: str
    memory_gb: float = 1.0
    n_tasks: int = 1
    cpus_per_task: int = 1
    mail_types: List[MailType] = Field(
        default_factory=lambda: [MailType.END, MailType.FAIL]
    )
    output: str = "%j.log"
    time: str = "14-0:00"

    @property
    def header_str(self) -> str:
        headers = [
            _sbatch_line("job-name", self.job_name),
            _sbatch_line("mail-user", self.email),
            _sbatch_line("mem", f"{self.memory_gb}gb"),
            _sbatch_line("ntasks", self.n_tasks),
            _sbatch_line("cpus-per-task", self.cpus_per_task),
            _sbatch_line("mail-type", self.mail_types),
            _sbatch_line("time", self.time),
            _sbatch_line("output", self.output),
        ]
        return "\n".join(headers)


def _sbatch_line(flag_name: str, value: Union[str, int, float, List[str]]) -> str:
    return f"#SBATCH --{flag_name}={_to_sbatch_value_str(value)}"


def _to_sbatch_value_str(value: Union[str, int, float, List[str]]) -> str:
    if isinstance(value, list):
        if isinstance(value[0], Enum):
            return ",".join(str(v.value) for v in value)
        return ",".join(str(v) for v in value)
    return str(value)


class SBatchFile(BaseModel):
    commands: List[str]
    headers: SBatchHeaders
    shebang: str = "#!/bin/bash"

    @property
    def contents(self) -> str:
        outputs = [self.shebang, self.headers.header_str, *self.commands]
        return "\n".join(outputs)
