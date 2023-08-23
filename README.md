# NodeParser

## Usage

This code will scan all nodes connected to RaspberryPi, collect messages from each node for one hour and summarise the collected messages.

## To start

Clone the repo to RaspberryPi and run node_parser.py

## Arguments

* Port - Interface name used to connect
* Outfile - Name of csv file where result will be stored
* Logtime - Dutation of logging

## Example of using

Node sends messages like this:

 | #Date               | #Node id | #Uptime         | #Health |
 |---------------------|----------|-----------------|---------| 
 | 18/08/2023 14:06:36 | 40       | 0 days 23:00:54 | 2       |
 | 18/08/2023 14:06:36 | 73       | 0 days 13:34:28 | 2       |
 | 18/08/2023 14:06:36 | 71       | 0 days 17:38:09 | 2       |
 | 18/08/2023 14:06:36 | 50       | 0 days 20:52:37 | 2       |
 | 18/08/2023 14:06:36 | 51       | 0 days 13:25:52 | 2       |
 | 18/08/2023 14:06:36 | 40       | 0 days 23:00:55 | 2       |
 | 18/08/2023 14:06:36 | 73       | 0 days 13:34:28 | 2       |
 | 18/08/2023 14:06:36 | 71       | 0 days 17:38:10 | 2       |
 | 18/08/2023 14:06:36 | 50       | 0 days 20:52:38 | 2       |
 | 18/08/2023 14:06:37 | 51       | 0 days 13:25:52 | 2       |
 | 18/08/2023 14:06:37 | 40       | 0 days 23:00:55 | 2       |

These messages are collected in a list until the logging period has expired.
After the data has been collected, the second part of the script begins to summarise it.

Result of summarised data

 | #Date               | #Node id | #Uptime         | #Health |
 |---------------------|----------|-----------------|---------| 
 | 18/08/2023 14:06:36 | 73       | 0 days 13:34:28 | 2       |
 | 18/08/2023 14:06:36 | 71       | 0 days 17:38:10 | 2       |
 | 18/08/2023 14:06:36 | 50       | 0 days 20:52:38 | 2       |
 | 18/08/2023 14:06:37 | 51       | 0 days 13:25:52 | 2       |
 | 18/08/2023 14:06:37 | 40       | 0 days 23:00:55 | 2       |

After the summarisation process, logging starts again and new data is added to the output file.