from src.mdb import submit_job


filename = "test_0-x.inp"
input_path = r"C:\Users\harryhz\Documents\abaqus\input_file"
output_path = r"C:\Users\harryhz\Documents\abaqus\input_file\test"
numCpus = 1
submit_job.submit_input_file(filename, input_path, output_path,numCpus)