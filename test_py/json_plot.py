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
from os import truncate
import sys
import plotly.graph_objects as go
import os.path

# Improvements
# - Command line paramater to force download the result file

print("Let me plot the results for you")
print("You need to run me from root of your Project and keep all the result files in the same directory")
print("Enter the Type of plot you like to see:")
print("Default plot:     1")
print("Statistical plot: 2")
print("Both plots:       3")
print()
print("Enter the json file name to plot as second argument.")
print("If no input, all test result files present in current directiry will be taken for plotting")
print()

# *************************** construt json **********************************************
is_single_file = False
result_file = './result.json'

if(os.path.exists(result_file)):
    os.remove(result_file)

try:
    single_file = "./" + sys.argv[2]
    is_single_file = True

except IndexError as error:  # if the resut file input is not provided
    print("fetching result files present in working directory...!")

if(is_single_file == False):
    # Read all the result files
    result_files = []
    for file in os.listdir("."):
        if file.endswith(".json"):
            result_files.append(file)

    if(len(result_files) == 0):
        print("result file/s does not exist")
        print("Noting to do : exit....!")
        exit()
    else:
        print("file/s : ")
        print(result_files)

    print("joining all files to one " + result_file + " file")

    final_data = {}  # contains all json data
    setup_element_list = []  # contains all test type information
    test_type_element_list = []  # contains all test type information

    for file in result_files:
        with open("./"+file) as f:
            json_file_data = json.load(f)

            # update to setup inoformation
            setup_element = json_file_data['setup']
            if(setup_element_list.count(setup_element) == 0):
                setup_element_list.append(setup_element)

            # update test type inforrmation from each file
            for test_type_element in json_file_data['Test_Type']:
                test_type_element["name"] = test_type_element["name"] + \
                    file[slice(6, -5)]
                test_type_element_list.append(test_type_element)

    # sorted to have largest setup info as first element
    final_data.update(
        {"setup": sorted(setup_element_list, key=lambda sub: len(sub), reverse=True)})
    final_data.update({"Test_Type": test_type_element_list})

    # Write the initial json object (list of dicts)
    with open(result_file, mode='w') as f:
        json.dump(final_data, f)

else:
    result_file = single_file


# *************************** plotting **********************************************

print('Using ' + result_file)

with open(result_file) as f:
    json_data = json.load(f)

if(is_single_file == False):
    clockCyclesPerSec = json_data['setup'][0]['cyclesPerSec']
else:
    clockCyclesPerSec = json_data['setup']['cyclesPerSec']


def select_test_type(test_types, test_type_name):
    ''' select_test_type '''
    return test_types['name'] == test_type_name

# Short note on whats happening here
#  https://stackoverflow.com/questions/4362153/lambda-returns-lambda-in-python


def select_test_type_curry(test_type_name):
    ''' select_test_type_curry '''
    return lambda test_types: select_test_type(
        test_types, test_type_name)


def remove_zero_latency(entries):
    ''' remove_zero_latency '''
    return list(filter(lambda entry: (
        round(entry['Cycles']) > 0), entries))


def get_test_type_entries(test_type):
    ''' get_test_type_entries '''
    entries = list(filter(
        select_test_type_curry(test_type), json_data['Test_Type']))[0]['entries']
    return remove_zero_latency(entries)


def payload(entry):
    ''' payload values'''
    return round(entry['payload'])


def avglatency(entry):
    ''' Cycles values in micro seconds'''
    return round((entry['Cycles'] * 1000000)/clockCyclesPerSec)


def throughput(entry):
    ''' Throughput in Kbps'''
    return (entry['payload'] * 8 * 1000000) / (entry['Cycles'] * 1024)


# Bar plots
# https://plotly.com/python/bar-charts/

# Line plots
# https://plotly.com/python/line-charts/#simple-line-plot-with-plotlyexpress

# # Create random data with numpy
# np.random.seed(1)
# N = 100
# random_x = np.linspace(0, 1, N)
# random_y0 = np.random.randn(N) + 5
# random_y1 = np.random.randn(N)
# random_y2 = np.random.randn(N) - 5
# Generate graph using Figure Constructor
# https://hackersandslackers.com/4-ways-to-improve-your-plotly-graphs/


def plot_chart(layout, data_set, test_types, y_axis=avglatency):
    ''' plot_chart '''
    fig = go.Figure(layout=layout)

    for test_type in test_types:
        if len(data_set[test_type]) == 0:
            continue
        fig.add_trace(draw_trace(data_set, test_type, y_axis, test_type))

    # # @todo calculate these values from the input data
    # fig.update_xaxes(tickvals=[8,      16,     32,     64,      128,     256,    512,
    #                            1024,   2048,   4096,   8192,    16384,   32768,  65536,
    #                            ])
    return fig


def plot_test_type_stats(layout, data_set, test_type):
    ''' plot_test_type_stats '''
    fig = go.Figure(layout=layout)

    fig.add_trace(draw_trace(data_set, test_type, avglatency, "avgLatency"))

    fig.update_layout(
        title="roundtrips : {0}, env : {1}, test_type : {2}".format(
            get_repetitions(), json_data['setup'][0]['env'], test_type),
        xaxis_title="payload(bytes)",
        yaxis_title="time(µs)")

    return fig


def draw_trace(data_set, test_type, y_axis, legend):
    ''' draw_trace '''
    plot_data = {"x": list(map(payload, data_set[test_type])),
                 "y": list(map(y_axis, data_set[test_type]))}
    trace = go.Scatter(plot_data,
                       mode='lines+markers',
                       name=legend,)
    return trace


def prepare_stack_latency(test_types, data_set):
    ''' prepare_stack_latency '''
    if len(set(['udp_interdomain', 'aracom_method_interdomain']).intersection(test_types)) == 2:
        aracom = data_set['aracom_method_interdomain']
        udp = data_set['udp_interdomain']
        latency_stack = map(lambda aracom, udp: {'payload': aracom['payload'], "avgLatency": (
            aracom['Cycles'] - udp['Cycles'])}, aracom, udp)
        return list(latency_stack)
    else:
        return []


def get_repetitions():
    ''' get value of number of repetitions'''
    return json_data['Test_Type'][0]['entries'][0]['repetitions']

# test_types.append('aracom_stack')
# data_set['aracom_stack'] = prepare_stack_latency(data_set)


def main():
    ''' plot latency v/s payload for different test_types '''
    test_types = [test_type["name"] for test_type in json_data["Test_Type"]]
    # test_types = ["udp_intradomain",
    #              "udp_interdomain",
    #              "aracom_method_intradomain",
    #              "aracom_method_interdomain"
    #              ]

    data_set = {x: get_test_type_entries(x) for x in test_types}
    if(is_single_file == False):
        try:
            layout = go.Layout(
                title="roundtrips : {0}, env : {1}, os : {2}, release:{3} , version: {4}".format(
                    get_repetitions(), json_data['setup'][0]['env'], json_data['setup'][0]['os'], json_data['setup'][0]['release'], json_data['setup'][0]['version']),
                xaxis_title="payload(bytes)",
                yaxis_title="time(µs)")

        except KeyError as error:  # incase there is error due to setup info mismatch, just show the complete setup info
            layout = go.Layout(
                title="setup: " + str(json_data['setup']),
                xaxis_title="payload(bytes)",
                yaxis_title="time(µs)")
    else:
        try:
            layout = go.Layout(
                title="roundtrips : {0}, env : {1}, os : {2}, release:{3} , version: {4}".format(
                    get_repetitions(), json_data['setup']['env'], json_data['setup']['os'], json_data['setup']['release'], json_data['setup']['version']),
                xaxis_title="payload(bytes)",
                yaxis_title="time(µs)")

        except KeyError as error:  # incase there is error due to setup info mismatch, just show the complete setup info
            layout = go.Layout(
                title="setup: " + str(json_data['setup']),
                xaxis_title="payload(bytes)",
                yaxis_title="time(µs)")

    if (sys.argv[1] == '1') or (sys.argv[1] == '3'):
        figure1 = plot_chart(layout, data_set, test_types)
        # figure1.show()
        figure1.update_xaxes(type="log")
        figure1.write_html('results.html', auto_open=True)

    if (sys.argv[1] == '2') or (sys.argv[1] == '3'):
        for test_type in test_types:
            figure2 = plot_test_type_stats(layout, data_set, test_type)
            # figure2.show()
            figure2.update_xaxes(type="log")
            figure2.write_html(test_type+'_stats.html', auto_open=True)


if __name__ == "__main__":
    main()
