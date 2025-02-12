import requests
import json
import sys

URL = "http://study-bible.herokuapp.com/bible-api/bible/model/nasb.json"


def get_data():
    source = requests.get(URL).json()
    return source


def sort_data_by_key(data, key=None):
    if key == None:
        return data

    data = sorted(data, key=lambda x: x[key])

    return data


def write_data_to_file(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f)

    print("Write operation complete")


if __name__ == "__main__":
    data = sort_data_by_key(get_data(), "pk")

    if len(sys.argv) == 2:
        write_data_to_file(data, sys.argv[1])
    else:
        print("Please pass in filepath to store data in")
