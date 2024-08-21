# Financial-Trend-Predict

## Overview

This repository contains an implementation of a trend prediction algorithm that leverages KRX (Korea Exchange) data and various technical analysis (TA) indicators. The algorithm is designed to optimize for both profitability and minimized maximum drawdown (MDD), providing a balance between potential returns and risk mitigation.

The final implementation is in the notebook `mod_tradelogicv2_park3.ipynb`, which includes all the functionalities discussed below.

## Project Structure

- **crawling & hurst exponent/**: This folder contains scripts and resources for data collection and analysis of the Hurst exponent. By calculating the Hurst exponent, we identify stocks that are more predictable and limit the analysis to these stocks. This ensures that the algorithm focuses only on assets with higher predictability, thereby improving overall performance.

- **mod_tradelogicv2_park3.ipynb**: The final implementation of the trend prediction algorithm, where KRX data is transformed into TA indicators and used to develop a trend prediction logic. The notebook also includes optimization through a Genetic Algorithm (GA) for tuning hyperparameters.

## Key Components

### 1. Hurst Exponent Analysis
The Hurst exponent is a statistical measure used to determine the predictability of a time series. A value closer to 1 indicates a persistent trend, while a value closer to 0.5 suggests a random walk. This analysis helps in filtering stocks that exhibit stronger trends and are therefore easier to predict.

The **crawling & hurst exponent/** folder contains scripts to calculate the Hurst exponent for different stocks in the KRX dataset. Only stocks with a high Hurst exponent are selected for further analysis, enhancing the accuracy and robustness of the predictive model.

### 2. Data Transformation to TA Indicators
The KRX data is processed and transformed into various technical analysis indicators. These indicators serve as the foundation for building predictive models. The algorithm converts the raw data into useful insights by considering:

- Moving Averages (e.g., SMA, EMA)
- Relative Strength Index (RSI)
- Bollinger Bands
- MACD (Moving Average Convergence Divergence)
- Other common TA indicators

The transformation requires several hyperparameters, which are optimized using a Genetic Algorithm (GA) to improve the effectiveness of the indicators.

### 3. Hyperparameter Optimization using Genetic Algorithm (GA)
Hyperparameters related to TA indicators and trend prediction models are optimized using a heuristic approach: a Genetic Algorithm (GA). The GA optimization focuses on maximizing the algorithm's performance by balancing:

- **Profitability**: Ensuring the algorithm generates positive returns over the backtesting period.
- **Maximum Drawdown (MDD)**: Limiting the largest observed loss from a peak to a trough, which helps in reducing the perceived risk for users.

The fitness function for the GA considers both profitability and MDD, ensuring a risk-aware optimization process.

### 4. Trend Prediction Logic with Threshold and RC Model (ESN)
To predict market trends, a threshold logic is used alongside a Reservoir Computing (RC) model, specifically an Echo State Network (ESN). The logic helps in making buy/sell decisions based on the predictions, improving the algorithm's practicality for trading.

The hyperparameters for the threshold and RC model are also optimized using the Genetic Algorithm, with the same fitness function focused on both returns and risk management.

### 5. Backtesting
Backtesting is an integral part of the project, providing insight into the algorithm's historical performance. The backtesting framework measures key metrics, such as:

- **Profitability**: Total returns generated over the backtesting period.
- **Maximum Drawdown (MDD)**: The largest observed loss during the period, reflecting the risk of the strategy.

The results are compared to existing strategies to showcase the improvements in performance.

## How to Run

1. **Install Dependencies**: Ensure that you have all the necessary dependencies installed. You can find a list of the required libraries in the `requirements.txt` file.

    ```bash
    pip install -r requirements.txt
    ```

2. **Data Collection and Hurst Exponent Calculation**: Use the scripts in the `crawling & hurst exponent/` folder to collect and preprocess the KRX data. After that, calculate the Hurst exponent for each stock to identify the ones with higher predictability.

3. **Run the Notebook**: Open and run `mod_tradelogicv2_park3.ipynb` to execute the full analysis, including data transformation, model optimization, and backtesting.

## Results

The final backtesting results demonstrate that the proposed trend prediction algorithm offers improved profitability and lower maximum drawdown compared to traditional strategies. The balance between returns and risk management is achieved through careful hyperparameter tuning using Genetic Algorithms.

Additionally, the Hurst exponent analysis further enhances the model by filtering for more predictable stocks, leading to better trend predictions and improved overall robustness of the algorithm.

## Conclusion

This project showcases the development of a trend prediction algorithm that combines technical analysis, heuristic optimization, and backtesting to create a balanced trading strategy. By focusing on both returns and risk management, and by using the Hurst exponent to select the most predictable stocks, the algorithm provides a practical solution for trading based on KRX data.

Feel free to explore the code and adapt the strategy to different markets or datasets.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
