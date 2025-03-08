---
layout: page
title: >-
  Volatility 2—Implied Ranges
date: 2013-04-09 18:13 -0700
author: Jim Bittman
origin_url: https://www.investors.com/research/options/volatility-2-8212-implied-ranges/
---





This is the second in a series of articles on volatility. The goal of this series is to clarify the different meanings of the term *volatility* and to discuss its many possible uses, including describing stock price action, evaluating option prices, choosing option strategies, and forecasting the market. Option traders should strive to gain an accurate understanding of volatility — and its many uses — because volatility affects option prices, trading decisions and risk analysis.


This article illustrates how traders might use the concept of historical stock price volatility discussed last week to estimate the range of stock prices in the near future.


**Brief Review**


"Volatility" is *price change without regard to direction*, and it is stated in percentage terms. For example, when looking at daily price changes in the past, it is common to say, "For the last 90 days, XYZ stock was trading at 20% volatility."


The stated volatility percentage, 20% in the example above, is the annual standard deviation of stock price movement. The consistent use of an annual rate makes comparisons possible. Without knowing the mathematics, it is obvious that a stock trading at 30% volatility is more volatile that a stock trading at 20% volatility.


**Standard Deviation Reviewed**


From statistics about normal distributions (bell-shaped curves), approximately 68% of all outcomes occur within one standard deviation of the mean; approximately 95% of all outcomes occur within two standard deviations of the mean; and approximately 99% of outcomes occur within three standard deviations.


This means that a $100 stock today that trades at 30% volatility has a 68% chance of closing between $70 and $130 one year from today, which is within the range of up one standard deviation to down one standard deviation. This stock also has a 95% chance of closing between $40 and $160, between up and down two standard deviations. And this stock has a 99% chance of closing between $10 and $190, between up and down three standard deviations.


**Converting the Annual Volatility**


Price-range probabilities for one year from today are not useful to short-term traders whose average holding period might be 60 days or less. So here is a formula for converting the stated volatility — the annual standard deviation — to a period of time chosen by the trader:


Standard Deviation for *n* days = Stock Price \* Volatility \* square root of time  
Where square root of time = square root of *n* days / square root of days per year 


Consider the following example in which stock XYZ has been trading at 25% volatility and is currently $60 per share. If XYZ continues to trade at 25% volatility, we know that the standard deviation for the coming year is 25%, or $15. But what is the standard deviation for the next 30 days? For the next 60 days?


Assuming a stock price of $60 and 25% volatility, the standard deviation for the next 30 days is calculated as follows:




|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Standard Deviation for 30 days | = | Stock Price | \* | Volatility | \* | square root of time |
|  | = | 60 | \* | 25% | \* | √ 60/365 |
|  | = | 60 | \* | .25 | \* | 7.75/19.1 |
|  | = | 6.08 |  |  |  |  |


6.08 is the standard deviation of stock XYZ for the next 30 days, assuming 25% volatility. This means that price of XYZ stock, in 30 days, has a 68% chance of closing between 66.08 (60.00 + 6.08) and 53.92 (60.00 — 6.08).  There is also a 95% chance that the closing price in 30 days will be between 72.16 between $47.84, which is between up and down two standard deviations. Finally, stock XYZ has a 99% chance of closing between $78.24 and 41.76, between up and down three standard deviations.


**Observations**


Note that 6.08 is approximately one-quarter of 25. In other words, the standard deviation for one month is approximately 25% of the standard deviation for one year. When traders say, "Volatility is skewed to the short term," this is what they mean.


For sellers of options, this means that a disproportionate part of the risk is allocated to the first part of an option's life. For buyers of options, this means that short-term options are more costly per unit of time than longer-term options.


**Using Volatility**


The statistics of volatility are a good starting point for traders, because the stock price has a 33% chance (approximately) of closing beyond one standard deviation at expiration. Consequently, a stock price equal to one-standard deviation is a realistic target for the stock to reach. In the example above, a bullish trader can realistically predict that stock XYZ will reach or move beyond $66.08. A trader still has to get the direction right, and there is still the risk that this time period will be one of the two-thirds when the stock price does not close beyond the one-standard deviation level. 


**More Statistics Coming**


Volatility gives traders probabilities that a stock's price will close within particular ranges *at the end of the time period*, which is usually expiration for options traders. These probabilities do not include the *path* that a stock price takes during the time period. Another set of probabilities helps traders estimate the chances that a stock price will reach a particular level at any time prior to expiration. These probabilities will be discussed next week.




