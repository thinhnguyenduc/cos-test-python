import json


def read_json_file(file_json: 'data.json'):
    f = open(file_json, "r")
    data = json.loads(f.read())
    for i in data['emp_details']:
        print(i)

    # Closing file
    f.close()
    return
