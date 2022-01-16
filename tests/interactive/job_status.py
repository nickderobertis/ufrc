from settings import Settings, SETTINGS
from ufrc.main import UFRC


def get_job_status(settings: Settings):
    ufrc = UFRC()
    ufrc.connect(settings.username, settings.password)
    print(ufrc.job_status("nimalendran"))


if __name__ == "__main__":
    get_job_status(SETTINGS)
