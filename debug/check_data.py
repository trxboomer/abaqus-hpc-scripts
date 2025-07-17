from odbAccess import *
import numpy as np
import csv



input_path=r"Y:\Students\Zhou_Harry\abaqus"
output_path=r"Y:\Students\Zhou_Harry\abaqus\test"

filename = "test_0-x.odb"

odb_path = input_path + "\\" + filename
odb = openOdb(path=odb_path)

frame = odb.steps["Step1"].frames[-1]

field_output = frame.fieldOutputs["HFL"]
assembly = odb.rootAssembly

# Get instance named 'PART-1-1'
instance = assembly.instances['PART-1-1']


element_labels = [v.elementLabel for v in field_output.values if hasattr(v, 'elementLabel')]
unique_elements = set(element_labels)
print("Number of elements with data:", len(unique_elements))
print("Total data rows:", len(field_output.values))

# Check integration points in data
ip_numbers = [getattr(v, 'integrationPoint', None) for v in field_output.values]
print("Unique integration points found:", set(ip_numbers))

all_elements = set(instance.elementLabel)  # e.g., all elements in an instance
output_elements = set(v.elementLabel for v in field_output.values)
missing_elements = all_elements - output_elements
print("Elements missing data:", missing_elements)