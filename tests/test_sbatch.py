from ufrc.sbatch import SBatchHeaders

EXPECT_SBATCH_HEADERS = """
#SBATCH --job-name=my_job
#SBATCH --mail-user=derobertisna@ufl.edu
#SBATCH --mem=1.0gb
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mail-type=END,FAIL
#SBATCH --time=14-0:00
#SBATCH --output=%j.log
""".strip()

def test_sbatch_headers():
    sbatch = SBatchHeaders(job_name="my_job", email="derobertisna@ufl.edu")
    output = sbatch.header_str
    assert output == EXPECT_SBATCH_HEADERS