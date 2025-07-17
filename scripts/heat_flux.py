from mdb import submit_job
import odb
import os

from odb import save_field_output

"""
This script need to do the following:
1. Run all input files in the specified input directory
2. Output .odb files into a new directory
3. Export the heat flux, and any other required fields from the .odb files
-> Exported fields should be organized into directories, where each directory corresponds to a set of input files which represent a single model
"""


def main(input_path: str, output_path: str, numcpu: int):
    input_files = [f for f in os.listdir(input_path) if f.endswith(".inp")]

    odb_dir = f"{output_path}/odb"
    for file in input_files:
        submit_job.submit_input_file(
            file, input_path=input_path, output_path=odb_dir, numCpus=numcpu
        )

    odb_files = [f for f in os.listdir(odb_dir) if f.endswith(".odb")]

    for file in odb_files:
        model_name = file.split("-")[0]
        model_dir = f"{odb_dir}/{model_name}"
        if not os.path.isdir(model_dir):
            os.mkdir(model_dir)

        save_field_output.get_csv(
            file,
            input_path=odb_dir,
            output_path=model_dir,
            step="Step 1",
            output_types=["HFL"],
            node_sets=["ALL NODES"],
        )


if __name__ == "__main__":
    main(
        input_path=r"Y:\Students\Zhou_Harry\abaqus",
        output_path=r"Y:\Students\Zhou_Harry\abaqus\test",
        numcpu= 1
    )
