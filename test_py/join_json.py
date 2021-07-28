# -*- coding: utf-8 -*-
'''************************************************************************************************
*                                                                                                 *
* COPYRIGHT RESERVED, Robert Bosch GmbH, 2019. All rights reserved.                               *
* The reproduction, distribution and utilization of this document as well as the communication    *
* of its contents to others without explicit authorization is prohibited. Offenders will be held  *
* liable for the payment of damages.                                                              *
* All rights reserved in the event of the grant of a patent, utility model or design.             *
*                                                                                                 *
************************************************************************************************'''
# Python script to plot results
import json
import sys
import plotly.graph_objects as go
import os.path

# Read all the result files
result_files = []
for file in os.listdir("./json"):
    if file.endswith(".txt"):
        result_files.append(file)
        
print(len(result_files))

final_data = {} # contains all json data
test_type_element_list = [] # contains all test type information

for result_file in result_files:
    with open("./json/"+result_file) as f:
        json_data = json.load(f)

        # update to setup inoformation
        setup_element = json_data['setup']
        final_data.update({"setup": setup_element})

        # update test type inforrmation from each file
        for test_type_element in json_data['Test_Type']:
            test_type_element["name"] = test_type_element["name"]+result_file[slice(6, -5)]
            test_type_element_list.append(test_type_element)

final_data.update({"Test_Type" : test_type_element_list})


filename = 'final.json'
lst = [{'alice': 24, 'bob': 27}]
# Write the initial json object (list of dicts)
with open(filename, mode='w') as f:
    json.dump(final_data, f)
