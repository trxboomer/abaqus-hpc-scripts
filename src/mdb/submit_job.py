import os
from abaqus import *

def submit_input_file(filename, input_path, output_path, numCpus):
    file_path = input_path+ "\\" + filename
    scratch_dir = input_path+"\\scratch\\"+filename[:-4]
    
    if not os.path.isdir(scratch_dir):
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
    
    os.rmdir(scratch_dir)

    return
