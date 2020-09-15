#!/usr/bin/env python3
"""
This is an implementation of an algorithm which detects anomalies in temperature sensor data.
A temperature is determined to be an anomaly when it is too far from the average temperature.
This distance from the average is parameter which can be adjusted. 
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

        limit = 10   
        counter = 0
        runningAvg = 0
        for k,v in temperature.items():
            counter += 1
            runningAvg = (list(v.values())[0] + runningAvg * (counter-1))/counter 
            # An anomaly is detected if a value is too far from the average  
            if list(v.values())[0] > runningAvg + limit or list(v.values())[0] < runningAvg - limit:
                print("ANOMALY DETECTED!")

    data = {
        "temperature": pandas.DataFrame.from_dict(temperature, "index").sort_index(),
        "occupancy": pandas.DataFrame.from_dict(occupancy, "index").sort_index(),
        "co2": pandas.DataFrame.from_dict(co2, "index").sort_index(),
    }

    return data


if __name__ == "__main__":
    data = load_data('output.txt')
