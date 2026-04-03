# faang-data-pipeline
Automated pipeline to download and visualize FAANG stock data using Python and GitHub Actions.
# faang-data-pipeline

This repository contains my work for the Computer Infrastructure assessment.

## Project overview

The goal of this assessment is to build an automated data pipeline that:

1. Downloads recent hourly stock data for the FAANG companies using `yfinance`
2. Saves the downloaded data into a `data/` folder
3. Opens the latest saved dataset and plots the closing prices
4. Saves the generated plot into a `plots/` folder
5. Runs the pipeline through a Python script and automates it using GitHub Actions

The FAANG companies used in this project are:

- META
- AAPL
- AMZN
- NFLX
- GOOG

## Repository structure

- `problems.ipynb` — notebook containing solutions, explanations, and discussion for each assessment problem
- `faang.py` — Python script version of the pipeline
- `data/` — saved CSV files containing downloaded stock data
- `plots/` — generated plot images
- `.github/workflows/` — GitHub Actions workflow for automation

## Assessment tasks

### Problem 1 — Data download
A function is used to download hourly stock data for the previous five days for the selected FAANG companies.  
The data is saved into the `data/` folder with a timestamped filename.

### Problem 2 — Plotting
A plotting function opens the most recent data file and creates a plot of the closing prices for all five stocks.  
The plot is saved into the `plots/` folder.

### Problem 3 — Script
The functions are included in a Python script called `faang.py`, so the whole process can be run as a single pipeline.

### Problem 4 — Automation
A GitHub Actions workflow is included to automate the execution of the pipeline.

## How to run

### Notebook
Open `problems.ipynb` and run the cells in order.

### Script
Run:

```bash
python faang.py

Requirements
Python 3
yfinance
pandas
matplotlib
Description

This project downloads stock data for FAANG companies, saves it, and generates a plot.

The notebook problems.ipynb contains the explanations and solutions for each problem.