# PyBank

## Overview
PyBank is a Python script designed to analyze the financial records of a company. The dataset contains two columns: "Date" and "Profit/Losses". The script calculates various financial metrics and outputs the results to both the terminal and a text file.

## Features
- Total number of months included in the dataset.
- Net total amount of "Profit/Losses" over the entire period.
- Average change in "Profit/Losses" over the entire period.
- Greatest increase in profits (date and amount) over the entire period.
- Greatest decrease in profits (date and amount) over the entire period.

## Dataset
The dataset is named `budget_data.csv` and should be placed in the `Resources` folder within the `PyBank` directory.

## Script
The main script file is `main.py`, located in the `PyBank` directory.

## Usage
1. Ensure the `budget_data.csv` file is located in the `PyBank/Resources` directory.
2. Run the script:
    ```sh
    python PyBank/main.py
    ```
3. The results will be printed to the terminal and saved to `PyBank/analysis/financial_analysis.txt`.

## Output
The script outputs the financial analysis in the following format:

Financial Analysis
Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)

# PyPoll

## Overview
PyPoll is a Python script designed to analyze election data. The dataset contains three columns: "Voter ID", "County", and "Candidate". The script calculates various election metrics and outputs the results to both the terminal and a text file.

## Features
- Total number of votes cast.
- A complete list of candidates who received votes.
- The percentage of votes each candidate won.
- The total number of votes each candidate won.
- The winner of the election based on popular vote.

## Dataset
The dataset is named `election_data.csv` and should be placed in the `Resources` folder within the `PyPoll` directory.

## Script
The main script file is `main.py`, located in the `PyPoll` directory.

## Usage
1. Ensure the `election_data.csv` file is located in the `PyPoll/Resources` directory.
2. Run the script:
    ```sh
    python PyPoll/main.py
    ```
3. The results will be printed to the terminal and saved to `PyPoll/analysis/election_analysis.txt`.

## Output
The script outputs the election analysis in the following format:

Election Results
Total Votes: 3521001
Charles Casper Stockham: 23.049% (852913)
Diana DeGette: 73.812% (2728923)
Raymon Anthony Doane: 3.139% (116165)
Winner: Diana DeGette
