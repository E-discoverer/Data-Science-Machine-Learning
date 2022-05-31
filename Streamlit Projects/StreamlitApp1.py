import yfinance as yf
import streamlit as st
import pandas as pd
import numpy as np

# heading and text
st.write(""" 
## Simple Stock Price App

Shown are the stock **closing price** and ***volume*** of Apple!

""")

# how to get data using python article
#define ticker symbol
tickerSymbol = 'AAPL'

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='id', start='2010-5-31', end='2022-4-30')
#Open High Low Close  Volume Dividends  Stock Splits

st.write("""
### Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
### Volume Price
""")
st.line_chart(tickerDf.Volume)
