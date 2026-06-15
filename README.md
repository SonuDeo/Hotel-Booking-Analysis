# Hotel Booking Analysis

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![pandas](https://img.shields.io/badge/pandas-data%20analysis-150458.svg)](https://pandas.pydata.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-notebook-F37626.svg)](https://jupyter.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Exploratory data analysis (EDA) of hotel booking demand data, examining the drivers
behind reservation cancellations and revenue patterns across two hotel types. The
project loads and cleans ~119,000 booking records, engineers analytical features, and
produces a set of visualizations that surface actionable insights.

---

## Table of Contents

- [Overview](#overview)
- [Dataset](#dataset)
- [Key Insights](#key-insights)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Analysis Workflow](#analysis-workflow)
- [Generated Outputs](#generated-outputs)
- [Technologies](#technologies)
- [License](#license)

---

## Overview

Hotel cancellations have a direct impact on revenue, staffing, and inventory planning.
This analysis investigates **when**, **where**, and **why** bookings get canceled, and
compares performance between a **City Hotel** and a **Resort Hotel**. The goal is to
turn raw booking records into clear, decision-ready visuals.

The questions explored include:

- What proportion of bookings are ultimately canceled?
- How do cancellation rates differ between the City Hotel and the Resort Hotel?
- How does the Average Daily Rate (ADR) vary by month and hotel type?
- Which countries contribute the most cancellations?
- Is there a relationship between price (ADR) and cancellation?

## Dataset

The project uses the **Hotel Booking Demand** dataset, originally published on Kaggle.

- **Source:** [Hotel Booking Demand on Kaggle](https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand)
- **Records:** 119,390 bookings
- **Features:** 32 columns
- **Time span:** July 2015 – August 2017
- **Coverage:** 177 countries, two hotel types (City and Resort)

| Attribute | Detail |
| --- | --- |
| File | `hotel_bookings.csv` |
| Granularity | One row per booking |
| Target of interest | `is_canceled` (0 = honored, 1 = canceled) |
| Notable fields | `hotel`, `lead_time`, `arrival_date_*`, `adr`, `country`, `market_segment`, `deposit_type` |

> The dataset is included in this repository for convenience. If you prefer to download
> it yourself, see the [Getting Started](#getting-started) section.

## Key Insights

Findings derived directly from the data in this repository:

- **~37%** of all bookings were canceled — a substantial share of expected demand.
- The **City Hotel** has a notably higher cancellation rate (**~41.7%**) than the
  **Resort Hotel** (**~27.8%**).
- The **City Hotel** accounts for the majority of volume (79,330 vs. 40,060 bookings).
- The **average daily rate (ADR)** across all bookings is **~101.83**, with clear
  seasonal variation between the two hotel types.
- **Portugal (PRT)** is both the top source market and the largest single contributor
  to cancellations.

## Project Structure

```
Hotel-Booking-Analysis/
├── Hotel_Booking_Analysis.ipynb   # Main notebook: loading, cleaning, EDA, plots
├── Hotel_Booking_Analysis.py      # Companion script (runs a representative subset)
├── hotel_bookings.csv             # Raw dataset (~119k rows)
├── requirements.txt               # Python dependencies
├── LICENSE                        # MIT license
└── README.md                      # Project documentation
```

When you run the analysis, a `notebook_outputs/` folder is created containing the
generated figures and a cleaned sample preview.

## Getting Started

### Prerequisites

- Python 3.10 or newer
- `pip` for installing dependencies

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/SonuDeo/Hotel-Booking-Analysis.git
cd Hotel-Booking-Analysis

# 2. (Recommended) Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate        # On Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

### Getting the dataset (optional)

The dataset ships with this repository. To fetch a fresh copy via the Kaggle CLI:

```bash
pip install kaggle
kaggle datasets download -d jessemostipak/hotel-booking-demand
unzip hotel-booking-demand.zip
```

Place `hotel_bookings.csv` in the project root alongside the notebook.

## Usage

### Run the notebook (recommended)

```bash
jupyter notebook Hotel_Booking_Analysis.ipynb
```

Execute the cells in order to reproduce the full analysis and all figures.

### Run the companion script

```bash
python Hotel_Booking_Analysis.py
```

This produces a representative figure and writes it to `notebook_outputs/`.

## Analysis Workflow

1. **Data loading** — read `hotel_bookings.csv` into a pandas DataFrame.
2. **Preprocessing** — handle missing values (`children`, `agent`, `company`), fix data
   types, and inspect nulls.
3. **Feature engineering** — derive `total_guests` and a numeric `arrival_month_num`.
4. **Exploratory data analysis** — visualize cancellations, hotel comparisons, ADR
   trends, monthly patterns, and top cancellation markets.
5. **Export** — save figures and a cleaned sample to `notebook_outputs/`.

## Generated Outputs

Running the notebook produces the following figures in `notebook_outputs/`:

| File | Description |
| --- | --- |
| `fig_reservation_status.png` | Canceled vs. not-canceled bookings |
| `fig_city_vs_resort.png` | Reservation status by hotel type |
| `fig_adr_by_hotel.png` | Average daily rate by month and hotel |
| `fig_reservation_per_month.png` | Reservation status per month |
| `fig_top_countries_canceled.png` | Top 10 countries by cancellations |
| `fig_adr_canceled_vs_not.png` | ADR for canceled vs. honored bookings |
| `sample_cleaned_preview.csv` | 200-row cleaned data preview |

## Technologies

- **Python** — core language
- **pandas** & **NumPy** — data manipulation and numerical computing
- **Matplotlib** — visualization
- **Jupyter Notebook** — interactive analysis

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for
details.
