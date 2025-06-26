<!-- # DL_xFPL_tp275_zh94 -->
# xFPL: Automated Fantasy Premier League (FPL) Strategic Advisor

## Project Overview

xFPL is a data-driven strategic advisor for Fantasy Premier League (FPL), designed to help FPL managers make better decisions about team selection, transfers, and captaincy picks. Utilizing machine learning techniques such as **supervised learning** and **data mining**, xFPL predicts player performance and offers weekly recommendations.

### Key Features
- **Player Recommendations:** Get personalized player transfer and captaincy suggestions based on data-driven analysis.
- **Predictive Models:** Uses historical player data to forecast expected points for the upcoming game weeks.
- **Continuous Updates:** Recommendations evolve with real-time data, ensuring relevance throughout the FPL season.

## Project Components

- **Data Mining & Engineering:** Extracts and analyzes historical player and team statistics to uncover performance patterns, enabling more accurate predictions.

- **Supervised Learning Model:**
  - **Regression Model (XGBoost):** Predict continuous outcome (expected player points).
  <!-- - **Classification Models:** Forecast binary outcomes like clean sheets or goal likelihood. -->
  
- **Evaluation:** 
  - **Offline Simulation:** Tests predictions on historical FPL data to benchmark against traditional methods.
  - **Real-time Testing:** Applies recommendations to an actual FPL team, comparing performance with other FPL tools and human experts.

<!-- ## Project Timeline

| Week  | Date           | Tasks                                         |
|-------|----------------|-----------------------------------------------|
| 0     | 9/23 - 9/27    | Finalize proposal, data sources, ETL scripts  |
| 1-2   | 9/30 - 10/11   | Exploratory Data Analysis (EDA), model dev.   |
| 3     | 10/14 - 10/18  | Interactive shell for demo                    |
| 4-5   | 10/21 - 11/1   | Model dev. & feature engineering, frontend    |
| 6     | 11/4 - 11/8    | Refine models                                 |
| 7     | 11/11 - 11/15  | Stage 2 testing, FPL manager feedback         |
| 8     | 11/18 - 11/22  | Demo preparation, finalize presentation       |
| 9-10  | 11/25 - 12/6   | Final clean-up, write-up                      | -->

<!-- ## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-repo/xFPL.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ``` -->

## Usage

<!-- 1. Ensure the required data is available (refer to the [vaastav/Fantasy-Premier-League](https://github.com/vaastav/Fantasy-Premier-League) repository for the data source). -->
1. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

2. Run the main program:

    ```bash
    python main.py
    ```

3. Follow the interactive prompts to get weekly FPL recommendations.

## Data Resources

- **Historical FPL Data:** [vaastav/Fantasy-Premier-League](https://github.com/vaastav/Fantasy-Premier-League) repository provides extensive player statistics, fixtures, and metadata updated weekly.

## Technologies Used

- **Programming Language:** Python (3.10.14)
- **Libraries:** Scikit-learn, xgboost, Pandas, NumPy (Data Manipulation), Matplotlib, Seaborn (Visualization)
- **Data Source:** Historical FPL data from GitHub

## Evaluation

xFPL will be evaluated through offline simulations using past FPL data and real-time testing during the current FPL season. Feedback from real FPL managers will ensure practical usability.

## Contributors

- **Anthony Huang (zh94)**
- **Tanay Punjabi (tp275)**
