# FAANG Data Pipeline

## Overview

This repository contains my work for the Computer Infrastructure assessment.

The goal of this project is to design and implement an automated data pipeline that retrieves, processes, and visualises stock data for FAANG companies using Python and GitHub Actions.

---

## Project Overview

The pipeline performs the following steps:

1. Downloads recent hourly stock data for FAANG companies using the `yfinance` library  
2. Saves the downloaded data into a `data/` folder  
3. Loads the most recent dataset and extracts closing prices  
4. Generates a plot comparing stock performance  
5. Saves the plot into a `plots/` folder  
6. Executes the entire workflow through a Python script  
7. Automates execution using GitHub Actions  

The FAANG companies included are:

- META  
- AAPL  
- AMZN  
- NFLX  
- GOOG  

---

## Repository Structure

- `problems.ipynb` — notebook containing explanations, solutions, and discussion  
- `faang.py` — Python script implementing the pipeline  
- `data/` — stored CSV datasets  
- `plots/` — generated visualisations  
- `.github/workflows/` — GitHub Actions automation  

---

## Assessment Tasks

### Problem 1 — Data Download

A function was implemented to retrieve hourly stock data for the previous five days using the `yfinance` library.  
The data is stored with a timestamp to ensure reproducibility and version tracking.

---

### Problem 2 — Plotting

The most recent dataset is loaded and processed to extract closing prices.  
A plot is generated using `matplotlib` to visually compare the performance of each company.

---

### Problem 3 — Script

All functionality is integrated into a single Python script (`faang.py`), allowing the entire pipeline to be executed in one command.

---

### Problem 4 — Automation

A GitHub Actions workflow (`faang.yml`) was created to automate the execution of the pipeline.  
This enables the process to be run without manual intervention and supports reproducibility.

---

## How to Run

### Notebook
Open `problems.ipynb` and run all cells in sequence.

### Script
```bash
python faang.py

Research and Design Choices
This project uses widely adopted data science tools:
pandas for data manipulation and analysis
matplotlib for visualisation
yfinance to access financial market data
These libraries were chosen due to their reliability, simplicity, and strong documentation.
Using these tools allows the focus to remain on pipeline design rather than low-level implementation.

Use of AI
AI tools were used during development as a support mechanism to assist with debugging and understanding concepts.
All generated suggestions were critically evaluated, tested, and adapted to ensure correctness and alignment with the project requirements.

References
https://pandas.pydata.org/
https://matplotlib.org/
https://pypi.org/project/yfinance/
https://docs.github.com/en/actions