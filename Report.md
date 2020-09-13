# Final Report

Below is our final report and solutions for the 2020 sensor mini project.


## Task 0: Setup Python Websockets

After setting up and running the python code as described , the greeting string issues by the server to the client upon first connecting is: 
"ECE Senior Capstone IOT Simulator"

## Task 1: Data Flow

Added python code to Websockets client that saves the JSON data to "output.txt" as it comes in message by message. Included newlines for formatting consistency.

## Task 2: Analysis

## Task 3: Design

A persistent change in temperature does not always indicate a failed sensor. External factors can influence temperature in ways that may appear to indicate a failed sensor. For example if a sensor was recording temperature near the entrance to a building. When people enter or leave the building, the temperature around the entrance may change dramatically. This would result in a consistent change in temperature which is to be expected.

For each room type, the possible temperature bounds would be a few degrees above and below the average recorded temperature. In the case of our anomaly detector, the bounds were set to be 10 degrees above and below the average temperature.

## Task 4: Conclusions

