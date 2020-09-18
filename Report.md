# Final Report

Below is our final report and solutions for the 2020 sensor mini project.


## Task 0: Setup Python Websockets

After setting up and running the python code as described , the greeting string issues by the server to the client upon first connecting is: 
"ECE Senior Capstone IOT Simulator"

## Task 1: Data Flow

Added python code to Websockets client that saves the JSON data to "output.txt" as it comes in message by message. Included newlines for formatting consistency.

## Task 2: Analysis

##### Median and Variance observed by Temperature data in office:

Temperature | Median | Variance
------------|--------|----------
Office | 23.01312357574916 | 2.9900143284023883

##### Median and Variance observed by Occupancy data in office:

Occupancy | Median | Variance
----------|--------|----------
Lab1 | 2.0 | 2.1021538083387097

## Graphs

##### Probability density function: Co2

![image](/Co2PDF.png)

##### Histogram: Co2

![image](/Co2Hist.png)

##### Probability density function: Temperature

![image](/TemperaturePDF.png)

##### Histogram: Temperature

![image](/TempHist.png)

##### Probability density function: Occupancy

![image](/OccupancyPDF.png)

##### Histogram: Occupancy

![image](/OccupancyHist.png)

##### Mean and variance of time interval of sensor readings:

Time Interval | Mean | Variance
----------|--------|----------
Sensor | 1.0065610682187331 | 1.056993023094602

##### Probability distribution function of time interval:

![image](/TimeIntervalPDF.png)

##### Histogram: Time Interval

![image](/TimeIntervalHist.png)

## Task 3: Design
Implemented an algorithm which detects anomalies in sensor data. A data point is determined to be an anomaly when it is too far from the average temperature. This distance is defined as greater than 2 times the standard deviation from the mean.

A persistent change in temperature does not always indicate a failed sensor. External factors can influence temperature in ways that may appear to indicate a failed sensor. For example if a sensor was recording temperature near the entrance to a building. When people enter or leave the building, the temperature around the entrance may change dramatically. This would result in a consistent change in temperature which is to be expected.

For each room type, the possible temperature bounds would be about 10 or 20 degrees above and below the average recorded temperature. Factors such as time of day, time of year, if air conditioning is functioning, etc, would influence the bounds and temperature. In the case of our anomaly detector, the bounds were set to be 2 standard deviations from the mean.

## Task 4: Conclusions

This project provides a good simulation of how temperature and occupancy sensors operate in the real world. The data is generated periodically, similar to how sensors in the real world would only be polled every once in a while. In addition, the data is randomly generated within a certain range. This is reflective of how in the real world, temperature and occupancy would flucuate due to various factors. 

However, this simulation is not perfect. It fails encompass the abnormalities of the real world. For example when measuring temperature, there may be a day where the air conditioning fails to turn on. As a result, the temperature of the room would be much higher than normal. This type of data was absent in the simulation data, as the temperatures had never ventured high or low enough to encompass the extreme temperatures that can be experienced in the real world. Furthermore, the same can be said about occupancy, where there may be a large-scale event where an abnormally high number of people enter a room. This would result in an large numbers which were not generated within the simulation.

Using the Python websockets library seemed much easier when compared to a compiled language like C++. There were plently of online resources about Python to rely on. In addition, there was relatively few lines of code which did the heavy lifting in Python, whereas in C++ would have required much more work.

It would be better to have the server poll the sensors for data, rather than have the sensors reach out to the server. Having the server poll the sensors would prevent bottlenecking, as the server would never be overloaded with data coming from sensors. In this case, the server would only reach out when it has the capacity to do so. In addition, the server would never have to deal with data coming in at the same time. The server would always only reach out to one sensor at a time so that it can be processed, rather than having a queueing system or dealing with lost data from multiple sensors.
