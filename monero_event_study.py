import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("xmr_data.csv")

# Calculate returns
df['Returns'] = df['Close'].pct_change() * 100

# Rolling volatility
df['Volatility'] = df['Returns'].rolling(window=30).std()

# Plot volatility
plt.plot(df['Volatility'])
plt.title("Monero Rolling Volatility")
plt.show()
