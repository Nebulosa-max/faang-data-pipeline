# FAANG Data Pipeline

## Overview

This repository contains my work for the Computer Infrastructure assessment.

The aim of this project is to design and implement an automated data pipeline that retrieves, stores, processes, and visualises recent stock market data for selected FAANG companies using Python and GitHub Actions.

The project demonstrates how a simple but reproducible pipeline can be built using well-established Python libraries and basic workflow automation.

---

## Project Overview

The pipeline performs the following steps:

1. Downloads recent hourly stock data for selected FAANG companies using the `yfinance` library  
2. Saves the downloaded data into the `data/` folder using a timestamped filename  
3. Loads the most recent dataset and extracts closing prices  
4. Generates a plot comparing stock performance over time  
5. Saves the generated visualisation into the `plots/` folder  
6. Executes the full process through a Python script  
7. Automates execution using GitHub Actions  

The companies included in this project are:

- META  
- AAPL  
- AMZN  
- NFLX  
- GOOG  

---

## Repository Structure

- `problems.ipynb` — notebook containing explanations, solutions, discussion, and analysis  
- `faang.py` — Python script version of the pipeline  
- `data/` — saved CSV files containing downloaded stock data  
- `plots/` — generated plot images  
- `.github/workflows/faang.yml` — GitHub Actions workflow for automation  
- `README.md` — project overview, setup, and documentation  

---

## Assessment Tasks

### Problem 1 — Data Download

A function was implemented to download hourly stock data for the previous five days for the selected FAANG companies.

The `yfinance` library was used because it provides straightforward access to financial market data and allows the retrieval of multiple stock tickers with relatively little code.

The downloaded data is saved in the `data/` folder using timestamped filenames. This supports reproducibility and keeps a record of different runs of the pipeline.

---

### Problem 2 — Plotting

A plotting function loads the most recent dataset and extracts the closing prices for all selected companies.

The visualisation was created using `matplotlib`, which is a widely used Python plotting library. This allows stock performance to be compared clearly in a single figure.

During development, readability issues were identified in the first version of the plot, especially on the x-axis where timestamps were overcrowded. A second plot was therefore used as an improved version to make the output easier to interpret.

This reflects an iterative approach to development, where outputs are reviewed and refined rather than accepted at first attempt.

---

### Problem 3 — Script

The main functions were combined into a single Python script called `faang.py`, allowing the entire process to be executed as one pipeline.

This improves usability and makes the project easier to run, test, and automate.

---

### Problem 4 — Automation

A GitHub Actions workflow was created in `.github/workflows/faang.yml` to automate the execution of the pipeline.

The workflow supports:

- manual execution using `workflow_dispatch`
- scheduled execution using `schedule`

This means the pipeline can be run either on demand or automatically at defined times, improving reproducibility and reducing manual effort.

---

## How to Run

### Notebook
Open `problems.ipynb` in VS Code or Jupyter and run the cells in sequence.

### Script
Run the pipeline locally with:


python faang.py

### Script

Run the pipeline locally with:

```bash
python faang.py

python3 faang.py

## Requirements

This project uses:

- Python 3
- yfinance
- pandas
- matplotlib
- Install the required packages with:

pip install yfinance pandas matplotlib

## Research and Design Choices
This project was informed by research into Python-based data workflows, financial data retrieval, and visualisation tools.

The following design choices were made:

- yfinance was selected to retrieve stock data because it offers convenient access to recent market data without requiring a more complex API integration process.
- pandas was used for loading and manipulating the dataset because it is a standard library for tabular data analysis in - Python.
- matplotlib was used for static visualisation because it is reliable, well documented, and sufficient for the plotting needs of this project.
- GitHub Actions was used for automation because it integrates directly with the repository and supports reproducible workflow execution.

These tools were chosen not only because they work, but because they are widely used, well supported, and appropriate for building a small reproducible pipeline.

## Critical Reflection

The project successfully demonstrates the core elements of a basic automated pipeline, but it also has some limitations.
Firstly, the pipeline depends on an external data source through yfinance, so failures in connectivity or external service availability could affect execution.

Secondly, the first version of the visualisation revealed readability issues on the x-axis due to overlapping timestamps. This was improved in a later version, showing the importance of reviewing outputs critically rather than assuming the first result is sufficient.

Thirdly, the current implementation uses a fixed list of companies. A more flexible version could allow user-defined tickers or configuration through an external file.

Finally, the project focuses mainly on data retrieval and visualisation. Future versions could include additional financial analysis, such as moving averages, volatility calculations, or interactive plots.

## Future Improvements

- Possible future improvements include:
- adding support for configurable ticker lists
- improving date formatting on plots
- including moving averages or summary statistics
- using interactive visualisation libraries such as Plotly
- adding logging and error handling
- scheduling more frequent automated runs

## Use of AI

AI tools were used during development as a support tool for debugging, structuring explanations, and improving clarity.

All code and written content were reviewed, tested, and adapted to ensure correctness and alignment with the assessment requirements.

AI assistance was not treated as a substitute for understanding. Official documentation and library references were also consulted to validate implementation choices.

## References

- Pandas Documentation: https://pandas.pydata.org/
- Matplotlib Documentation: https://matplotlib.org/
- yfinance Documentation / Package Page: https://pypi.org/project/yfinance/
- GitHub Actions Documentation: https://docs.github.com/en/actions