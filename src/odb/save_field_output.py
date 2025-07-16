from obdAccess import *
import numpy as np
import numpy.typing as npt


def get_field_output(field_values):
    field_output_data: list[list[float]] = []
    for v in field_values:
        field_output_data.append([v.elementLabel, v.nodeLabel, v.position, *v.data])

    return np.array(field_output_data)


def get_csv(
    filename: str,
    input_path: str,
    output_path: str,
    step: str,
    output_types: list[str],
    node_sets: list[str],
):
    odb_path = f"{input_path}/{filename}"
    odb = openOdb(path=odb_path)

    frame = odb.steps[step].frames[-1]

    output_fields: dict[str, npt.NDArray[np.float64]] = {}

    for output_type in output_types:
        field = frame.fieldOutputs[output_type]
        with open(f"{output_path}/{filename}-{output_type}", "wb") as f:
            np.save(f, get_field_output(field))
