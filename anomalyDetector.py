#!/usr/bin/env python3
"""
This is an implementation of an algorithm which detects anomalies in sensor data.
A data point is determined to be an anomaly when it is too far from the average temperature.
This distance is defined as greater than 2 times the standard deviation from the mean.
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

    data = {
        "temperature": pandas.DataFrame.from_dict(temperature, "index").sort_index(),
        "occupancy": pandas.DataFrame.from_dict(occupancy, "index").sort_index(),
        "co2": pandas.DataFrame.from_dict(co2, "index").sort_index(),
    }

    return data

def detectAnomalies(data, metric, room):
    cleanData = data[metric][room].dropna()
    mean = cleanData.mean()
    stdDev = cleanData.std()

    numAnomalies = 0
    length = len(cleanData)
    # Count and cleanse data of anomalies
    for i, temp in cleanData.iteritems():
        if (temp < mean - 2*stdDev) or (temp > mean + 2*stdDev):
            numAnomalies += 1
            cleanData.drop(i, inplace=True)

    print("Percentage of \"bad\" data points found:", len(cleanData) / length)
    print("Median for the", metric, "data in the", room, "room:", cleanData.median())
    print("Median for the", metric, "data in the", room, "room:", cleanData.var(), "\n")

if __name__ == "__main__":
    data = load_data('output.txt')
    detectAnomalies(data, "temperature", "office")
    detectAnomalies(data, "temperature", "lab1")
    detectAnomalies(data, "temperature", "class1")
