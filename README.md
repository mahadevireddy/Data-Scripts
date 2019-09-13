# Data-Scripts

Rule aggregator is a python script which takes two "%Impact by Rule and FI" files of different dates from power BI in .xlsx format and aggregates total number of accounts grouped by rule name and dates and also outputs the percentage difference between the two compared dates.

Pre-requisite:
1. Windows PC
2. Python 3.x installed on PC

Steps to run this script
1. Download this repository on your machine and unzip/extract the zip file. 
2. Download 2 files from Power BI with different dates where you want to compare the total number of accounts. (.xlsx format)
3. Open the extracted folder and dump the two input files(.xlsx) in subfolder 'files'
4. Navigate one step back and you will find script 'rule_aggregator'.
5. Double click the script 'rule_aggregator' to execute it (execution time in seconds).
6. Navigate further to 'files' and you will find a new xlsx created file named 'result' which has the output.

