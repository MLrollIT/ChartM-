import matplotlib.pyplot as plt
import numpy as np

# Months in 2021
months = np.array(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])

# Market Capitalization data of top 10 cryptocurrencies
bitcoin = np.array([663.23, 745.46, 641.98, 834.23, 927.51, 658.21, 789.42, 850.64, 774.36, 819.23, 923.77, 996.51])
ethereum = np.array([160.85, 186.74, 201.76, 281.09, 389.54, 276.13, 322.45, 361.29, 301.67, 355.42, 414.37, 482.98])
binance_coin = np.array([20.98, 27.63, 37.15, 45.82, 59.41, 37.96, 49.13, 54.72, 41.54, 52.63, 61.87, 67.51])
cardano = np.array([0.31, 0.42, 0.38, 0.42, 0.59, 0.29, 0.34, 0.41, 0.32, 0.39, 0.44, 0.48])
xrp = np.array([0.29, 0.32, 0.28, 0.28, 0.40, 0.24, 0.29, 0.37, 0.27, 0.31, 0.35, 0.39])
dogecoin = np.array([0.01, 0.01, 0.01, 0.06, 0.28, 0.33, 0.31, 0.42, 0.30, 0.40, 0.48, 0.51])
polkadot = np.array([11.23, 11.81, 10.34, 14.72, 17.83, 9.44, 11.15, 14.63, 13.20, 17.28, 20.06, 23.42])
litecoin = np.array([3.57, 4.81, 3.98, 5.63, 7.92, 5.43, 6.45, 8.17, 6.83, 8.09, 9.35, 10.75])
chainlink = np.array([11.25, 11.48, 11.24, 13.36, 19.63, 11.04, 12.57, 15.44, 13.26, 16.18, 18.64, 21.89])
bitcoin_cash = np.array([541.05, 620.77, 518.23, 703.27, 811.14, 512.37, 618.53, 694.82, 576.59, 652.47, 737.93, 825.11])

# Stem plot for each cryptocurrency
plt.figure(figsize=(12,8))
plt.step(months, bitcoin, label = "Bitcoin")
plt.step(months, ethereum, label = "Ethereum")
plt.step(months, binance_coin, label = "Binance Coin")
plt.step(months, cardano, label = "Cardano")
plt