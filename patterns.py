import pandas as pd
  
def is_doji(open_price, close_price, threshold=0.01):  
    '''  
    Check if a candlestick is a Doji pattern.  
    :param open_price: The opening price of the candlestick.  
    :param close_price: The closing price of the candlestick.  
    :param threshold: The threshold for determining if the open and close prices are close.  
    :return: Boolean indicating if the candlestick is a Doji.  
    '''  
    return abs(open_price - close_price) < threshold * (open_price + close_price)/ 2 
 
def is_hammer(low, high, open_price, close_price):  
    '''  
    Check if a candlestick is a Hammer pattern.  
    :param low: The low price of the candlestick.  
    :param high: The high price of the candlestick.  
    :param open_price: The opening price of the candlestick.  
    :param close_price: The closing price of the candlestick.  
    :return: Boolean indicating if the candlestick is a Hammer.  
    '''  
    body = abs(close_price - open_price)  
    lower_shadow = open_price - low if open_price < close_price else close_price - low  
    upper_shadow = high - open_price if open_price < close_price else high - close_price  
    return body < (upper_shadow * 0.1) and lower_shadow > (2 * body) 

def is_engulfing(previous_open, previous_close, current_open, current_close):  
    '''  
    Check if there is a bullish or bearish Engulfing pattern.  
    :param previous_open: The opening price of the previous candlestick.  
    :param previous_close: The closing price of the previous candlestick.  
    :param current_open: The opening price of the current candlestick.  
    :param current_close: The closing price of the current candlestick.  
    :return: 'Bullish', 'Bearish', or 'None' indicating the type of Engulfing pattern detected.  
    '''  
    if (current_open < previous_close and current_close > previous_open):  return 'Bullish'  
    elif (current_open > previous_close and current_close <  previous_open):  return 'Bearish'  
    return 'None'  

def detect_patterns(data):  
    '''  
    Identify key candlestick patterns in historical price data.  
    :param data: A DataFrame containing the historical price data.  
    :return: A DataFrame with patterns identified.  
    '''  
    patterns = []  
    for i in range(1, len(data)):  
        current_candle = data.iloc[i]  
        previous_candle = data.iloc[i - 1]  
        if is_doji(current_candle['Open'], current_candle['Close']):  
            patterns.append((current_candle['Date'], 'Doji'))  
        elif is_hammer(current_candle['Low'],  current_candle['High'], current_candle['Open'], current_candle['Close']):
            patterns.append((current_candle['Date'], 'Hammer'))  
        elif (engulfing_type :=  is_engulfing(previous_candle['Open'], previous_candle['Close'], current_candle['Open'], current_candle['Close'])) != 'None':
            patterns.append((current_candle['Date'], engulfing_type + ' Engulfing'))  
    return patterns


#Example usage with sample data  
data = pd.DataFrame(
    {
        'Date': pd.date_range(start='2023-01-01', periods=6),  
        'Open': [100, 102, 101, 103, 99, 98],  
        'Close': [102, 101, 104, 99, 98, 97],  
        'High': [103, 104, 105, 104, 100, 99],  
        'Low': [99, 100, 100, 95, 97, 96]  
    })  
patterns_detected = detect_patterns(data)
  
#Output results  
for date, pattern in patterns_detected:  
    print(f"Date: {date}, Pattern Detected: {pattern}")
