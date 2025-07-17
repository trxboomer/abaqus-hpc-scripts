from odbAccess import *
import numpy as np
import csv


def get_field_output(field_values):
    field_output_data = []
    for v in field_values.values:
        data = [v.elementLabel, v.nodeLabel, v.position]
        data.append(entry for entry in v.data)
        field_output_data.append(data)
        
    return np.array(field_output_data)


def get_csv(
    filename,
    input_path,
    output_path,
    step,
    output_types,
    node_sets,
):
    odb_path = input_path + "\\" + filename
    odb = openOdb(path=odb_path)

    frame = odb.steps[step].frames[-1]

    for output_type in output_types:
        field = frame.fieldOutputs[output_type].getSubset(position=INTEGRATION_POINT)
        print(field.getSubset())
        f = open(output_path+"\\"+filename+"-"+output_type+".npy", "wb")
        bulk_data = np.concatenate([np.copy(block.data) for block in field.bulkDataBlocks])
        np.save(f, bulk_data)
        
    odb.close()


if __name__ == "__main__":
    get_csv(
        filename="test_0-x.odb",
        input_path=r"C:\Users\harryhz\Documents\abaqus",
        output_path=r"C:\Users\harryhz\Documents\abaqus\test",
        step="Step1",
        output_types=["HFL"],
        node_sets=["ALL NODES"],
    )
