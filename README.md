# text_mining_crypto_FG_index
a project of analyzing the Fear and Greed index of Ethereum as well as visualization of a time period from 2024/10/01-2025/10/01, weekly basis data
## Description
The concept of the **Crypto Fear & Greed Index** originates from the traditional financial market's Fear & Greed Index, which was designed by CNN in 2004 and subsequently widely adopted in the cryptocurrency space.

It is a metric that gauges **market sentiment**, with a score ranging from 0 to 100. **0 represents Extreme Fear, and 100 represents Extreme Greed.** It combines multiple indicators to assess the overall mood of the cryptocurrency market, helping investors understand whether the market is overbought (Greed) or oversold (Fear) to make more informed investment decisions.

---

## **Why not choose the traditional stock market as the target for analysis?**

Because the cryptocurrency market is **newer, smaller, and lacks fundamental analysis** compared to traditional stock markets, it is much **more easily driven by emotion**. Additionally, the average age of crypto investors is generally younger, making them more likely to express their emotions and opinions online.

---

## **Our Custom Index**

Our target is **Ethereum**, the second-largest cryptocurrency. We have created a **custom weighted index** referenced from the original formula, which is applicable to other cryptocurrencies and also simplifies the analysis process.

$$\text{Volatility} \times 25 + \text{Market Momentum/Volume} \times 25\% + \text{Social Media} \times 25\% + \text{Google Search Trends} \times 25\% = \text{Fear \& Greed Index}$$

**Formula Reference Source:** [https://alternative.me/crypto/fear-and-greed-index/](https://alternative.me/crypto/fear-and-greed-index/)

### **Variable Explanations:**

1.  **Volatility:** Compares the current 24-hour data with the average values of the past 30 and 90 days in a standardized way—specifically, the magnitude of the price fluctuation over the last 30/90 days. **A surge in volatility $\rightarrow$ Fear.**
2.  **Market Momentum/Volume:** Measures the daily trading volume and price momentum on major exchanges compared to the 30/90-day averages. **High volume and rising prices represents Greed.**
3.  **Social Media:** Sentiment index calculation.
4.  **Google Search Trends:** The relative quantity of searches for keywords like "Buy," "price prediction," or "scam." **A surge in "Buy" searches represents Greed.**

### Dependencies
copy the text to the your command to install dependencies:
`pip install -r requirements.txt`
* Windows 10 environment
## Folders
### eth
including the volatility and volume csv data
### google trends
including the code to scrap data from google trends with API integration
### social media
including the code to scrap data from reddit with API integration
and the sentimental analysis in jupyter notebook format
### visual
the visualization images from the data



## Authors
B12703009 高郁涵
B12703120 蕭宥平
B13703046 蔡育勳
B10303006 葉家睿
B12504098 李庭丞







