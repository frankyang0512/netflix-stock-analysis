import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("Netflix Dataset.csv")
#查看前幾項
#print(data.head())

#查看缺失值
#print(data.isnull().sum())

#檢查數據描述統計
#print(data.describe())

#print(data[['Date', 'Close', 'rate_return']].head())

# 轉換日期格式
data['Date'] = pd.to_datetime(data['Date'])

#計算50,200天均線
data['moving_average_50'] = data['Close'].rolling(window=50).mean()
data['moving_average_200'] = data['Close'].rolling(window=200).mean()


# 繪製收盤價走勢圖

plt.figure(figsize=(12,6))
sns.lineplot(data = data, x = data['Date'], y = data['Adj Close'], label='Close Price')
plt.plot(data['Date'], data['moving_average_50'], label='moving average(50)')
plt.plot(data['Date'], data['moving_average_200'], label='moving average(200)')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.title('Netflix Stock Price History')
plt.legend()
plt.show()

#繪製成交量直條圖
plt.figure(figsize=(12,6))
plt.bar(data['Date'], data['Volume'])
plt.xlabel('Date')
plt.ylabel('Volumn')
plt.title('Netflix Stock Volumn History')
plt.show()