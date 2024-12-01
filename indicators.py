import pandas as pd
import numpy as np  

def calculate_sma(prices, period):
    '''
    Calculate the Simple Moving Average (SMA).
    :param prices: List of price values.  :param period: The number of periods to average over.
    :return: SMA values as a pandas Series.
    '''
    sma = pd.Series(prices).rolling(window=period).mean()
    return sma

def calculate_ema(prices, period):
    '''
    Calculate the Exponential Moving Average (EMA).
    :param prices: List of price values.
    :param period: The number of periods to calculate EMA.
    :return: EMA values as a pandas Series.
    '''
    ema = pd.Series(prices).ewm(span=period, adjust=False).mean()
    return ema

def calculate_macd(prices):
    '''
    Calculate the Moving Average Convergence Divergence (MACD).
    :param prices: List of price values.
    :return: Tuple of MACD values and the signal line as pandas Series.
    '''
    ema_12 = calculate_ema(prices, 12)
    ema_26 = calculate_ema(prices, 26)
    macd = ema_12 - ema_26
    signal_line = calculate_ema(macd, 9)
    
    #Signal line is the 9-day EMA of the MACD
    return macd, signal_line

def identify_horizontal_support_resistance(prices):  
    '''  
    Identify horizontal support and resistance levels from historical price data.  
    :param prices: A list or array of historical prices.
    :return: A dictionary containing support and resistance levels.
    '''
    
    levels = pd.Series(prices).value_counts()  
    resistance = levels[levels > 1].index.tolist()
    
    #Levels with more than one occurrence  
    support = levels[levels < 1].index.tolist()
    
    #Levels with less than one occurrence
    return {'support': support, 'resistance': resistance}

def calculate_fibonacci_levels(swing_high, swing_low):
    
    '''
    Calculate Fibonacci retracement levels.
    :param swing_high: The highest price in the recent trend.
    :param swing_low: The lowest price in the recent trend.
    :return: A dictionary of Fibonacci support and resistance levels.
    '''
    
    price_range = swing_high - swing_low  
    levels = {  
              'Support Level 1': swing_high - 0.236 * price_range,
              'Support Level 2': swing_high - 0.382 * price_range,
              'Support Level 3': swing_high - 0.618 * price_range,
              'Resistance Level 1': swing_low + 0.236 * price_range,
              'Resistance Level 2': swing_low + 0.382 * price_range,
              'Resistance Level 3': swing_low + 0.618 * price_range  
              }  
    return levels  

def peak_trough_analysis(prices):
    
    '''
    Conduct peak and trough analysis to identify support and resistance levels.
    :param prices: A list or array of historical prices.
    :return: A dictionary of identified peaks and troughs.
    '''
    
    peaks = []
    troughs = []
    for i in range(1, len(prices) - 1):
        if prices[i] > prices[i - 1] and prices[i] > prices[i + 1]:
            peaks.append(prices[i])  
        elif prices[i] < prices[i - 1] and prices[i] < prices[i + 1]:
            #Trough
            troughs.append(prices[i])
    return {'peaks': peaks, 'troughs': troughs}

#Example market price data (list of closing prices)  
prices = [61.50, 62.30, 61.80, 62.50, 62.90, 63.00, 63.30, 63.70, 64.50, 65.20, 64.80, 65.00, 66.50, 67.00, 67.80, 68.00, 67.50, 67.20, 68.50, 68.80]

#SMA for periods of 5 and 10
sma_5 = calculate_sma(prices, 5)
sma_10 = calculate_sma(prices, 10)

#EMA for periods of 5 and 10
ema_5 = calculate_ema(prices, 5)
ema_10 = calculate_ema(prices, 10)

#MACD calculation
macd_values, signal_line = calculate_macd(prices)

#Output results  
print("SMA (5):\n", sma_5, end="\n", sep="")
print("SMA (10):\n", sma_10, end="\n", sep="")
print("EMA (5):\n", ema_5, end="\n", sep="")
print("EMA (10):\n", ema_10, end="\n", sep="")
print("MACD Values:\n", macd_values, end="\n", sep="")
print("Signal Line:\n", signal_line, end="\n", sep="")

#Example usage
historical_prices = [100, 102, 105, 102, 107, 103, 101, 106, 109, 107, 110, 105]  

#Identify horizontal support and resistance levels
horizontal_levels = identify_horizontal_support_resistance(historical_prices)
print("Horizontal Support and Resistance Levels:", horizontal_levels)

#Calculate Fibonacci levels
fibonacci_levels = calculate_fibonacci_levels(swing_high=max(historical_prices), swing_low=min(historical_prices))
print("Fibonacci Levels:", fibonacci_levels)

#Conduct peak and trough analysis
analysis_results = peak_trough_analysis(historical_prices)
print("Peaks and Troughs:", analysis_results)