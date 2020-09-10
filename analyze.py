#!/usr/bin/env python3
"""
This example assumes the JSON data is saved one line per timestamp (message from server).

It shows how to read and process a text file line-by-line in Python, converting JSON fragments
to per-sensor dictionaries indexed by time.
These dictionaries are immediately put into Pandas DataFrames for easier processing.

Feel free to save your data in a better format--I was just showing what one might do quickly.
"""
import pandas
from pathlib import Path
import argparse
import json
from datetime import datetime
import typing as T
import matplotlib.pyplot as plt
import numpy as np
filer = open('output.txt')

def load_data(file: Path) -> T.Dict[str, pandas.DataFrame]:

    temperature = {}
    occupancy = {}
    co2 = {}

    with open(file, "r") as f:
        for line in f:
            r = json.loads(line)
            room = list(r.keys())[0]
            time = datetime.fromisoformat(r[room]["time"])

            temperature[time] = {room: r[room]["temperature"][0]}
            occupancy[time] = {room: r[room]["occupancy"][0]}
            co2[time] = {room: r[room]["co2"][0]}
        temp = []
        for k,v in temperature.items():
            temp.append(list(v.values())[0])
        tempDF = pandas.DataFrame(temp)
        tempMedian = tempDF.median()
        tempVar = tempDF.var()
        print("The median of the temperatures is:", tempMedian[0])
        print("The variance of the temperatures is:", tempVar[0])

        occu = []
        for k,v in occupancy.items():
            occu.append(list(v.values())[0])
        occuDF = pandas.DataFrame(occu)
        occuMedian = occuDF.median()
        occuVar = occuDF.var()
        print("The median of occupancy is:", occuMedian[0])
        print("The variance of occupancy is:", occuVar[0])

    data = {
        "temperature": pandas.DataFrame.from_dict(temperature, "index").sort_index(),
        "occupancy": pandas.DataFrame.from_dict(occupancy, "index").sort_index(),
        "co2": pandas.DataFrame.from_dict(co2, "index").sort_index(),
    }

    return data


if __name__ == "__main__":
    data = load_data('output.txt')
    for k in data:
        data[k].plot()
        time = data[k].index
        data[k].hist()
        plt.figure()
        plt.hist(np.diff(time.values).astype(np.int64) // 1000000000)
        plt.xlabel("Time (seconds)")
    plt.show()
