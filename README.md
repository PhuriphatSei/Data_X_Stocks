# Data_X_Stocks
This project fetches fundamental financial data for selected SET50 stocks using the yfinance library. It collects key metrics such as Price, PE ratio, PBV, ROE, EPS, Book Value per Share, and Net Income. Using these data points, it calculates intrinsic stock valuations based on Discounted Cash Flow (DCF) and Graham Number methods.

#File Structure
.
├── screener.py              # Main script to run
├── valuation_dcf.py         # DCF valuation function
├── valuation_graham.py      # Graham number valuation function
├── pe_roe_trend.py          # Visualization function for PE vs ROE
├── data/
│   └── raw/                 # CSV output saved here
└── output/
    └── pe_roe_trend.png     # Scatter plot output
