from abaqus import *


def submit_input_file(filename: str, input_path: str, output_path: str, numCpus: int):
    file_path = f"{input_path}/{filename}"
    scratch_dir = f"{input_path}/scratch/{filename[:-4]}"

    os.makedirs(scratch_dir)

    os.chdir(output_path)

    job = mdb.JobFromInputFile(
        name=filename[:-4],
        inputFileName=file_path,
        scratch=scratch_dir,
        numCpus=numCpus,
    )

    job.submit()
    job.waitForCompletion()

    return
