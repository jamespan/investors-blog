---
layout: page
title: >-
  The "Greeks" – What Options Traders Need To Know Part 4 – Theta
date: 2013-07-24 19:11 -0700
author: Jim Bittman
origin_url: https://www.investors.com/research/options/the-greeks-8211-what-options-traders-need-to-know-part-4-8211-theta/
---





How and why option prices change is a mystery to many options traders. This is the fourth in a [series](http://news.investors.com/investing-options/070313-662478-the-greeks-and8211-what-options-traders-need-to-know-part-1-and8211-delta.htm) [of](http://news.investors.com/investing-options/070913-663011-the-greeks-and8211-what-options-traders-need-to-know-part-2-and8211-gamma.htm) [articles](http://news.investors.com/investing-options/071713-664192-the-greeks-and8211-what-options-traders-need-to-know-part-3-and8211-vega.htm) that discuss the seemingly complex topic of options price behavior and the "Greeks."

  

**Introduction**

  

Time decay, which is also known as time erosion, is a well-known influence on option prices. It is a challenge to option buyers and a benefit to option sellers. What is not so well known, however, is exactly how time decay works and that it affects options with different strike prices differently. A thorough understanding of time decay can improve the results of one's options trades.

  

**Theta Defined**

  

Time decay is measured in units of time, and ***theta is the estimated change in option price for a one unit change in time to expiration, assuming other factors remain constant***. But this seemingly simple definition begs the question, "What is one unit of time?" Is one unit of time one day, one week, one month or some other period? The answer varies by the needs of traders.

  

Active, short-term traders most likely are concerned with the daily decline in options values. Longer-term traders, such as writers of 60-day or 90-day covered calls, however, might be more interest in the estimated 7-day or 10-day decline.

  

Exhibit 1 illustrates how a typical option pricing computer program takes six inputs and calculates the theoretical price of the call and put. The difference between columns 1 and 2 is that the assumption of time — Days to Expiration — has been decreased from 35 to 28, a decrease of one week.

  

In Exhibit 1, note that the "theta of −0.30" means that "a decrease of one unit of time to expiration, seven calendar days in this example, causes the price of the 90 Call to fall by 30 cents from 2.57 to 2.27. It also causes the price of the 90 Put to fall by 30 cents from 2.99 to 2.69." Thus, theta is stated in the same units (dollars and cents) as the option price. This is different than delta, which is stated in percentage terms.

  

**Is Theta Useful?**

  

Although computer programs are widely used to estimate option prices for traders' forecasts, an understanding of theta can be helpful.

  

Assuming a theta of ".30," or 30 cents per week as in the example above, then a trader who buys this 90 Call and who is willing to risk $1.20 per share can roughly estimate that, if the stock price does not change, then it will be approximately four weeks before the 90 Call will decrease to this loss limit. This line of thinking, however, does not include the possibility of a stock price decline which would likely cause the loss limit to be reached sooner than if only time erosion exerted a negative impact on the option's price.

  

**Thetas Change**

  

Table 1 contains theoretical values and thetas of a hypothetical 100 Call option at different stock prices and different days to expiration. The purpose of Table 1 is to illustrate some basic concepts of how thetas change as stock price and time to expiration change. The rows in Table 1 represent the stock prices, and the columns represent the number of days to expiration.

  

Looking up and down the columns and across the rows in Table 1, it is apparent that the theta of the 100 Call changes. What might not be so apparent is the logic of the changes. Here are some simple guidelines.

  

First, **theta is a negative number**. In every cell in Table 1, the theta is a negative number. This means that as time to expiration decreases and other factors remain unchanged, the option price also decreases. This causes some **problems with terminology**. For example, looking across row 4 (stock price 100), theta changes from −.21 in column 1 to −.56 in column 6. This is a *decrease* in theta from −.21 to −.56. Many traders, however, describe this as an "increase in theta" (because the absolute value of the theta increases). It is therefore important to listen carefully when "time decay" and "theta" and "increases" and "decreases" are being discussed.

  

The second guideline is that **for at-the-money and close-to-the-money options, time decay increases as expiration approaches, which means that theta decreases**. Looking across row 4, the value of the 100 Call is 5.09 in column 1 and 4.64 in column 2. This is a decrease of 45 cents (0.45) in 15 days. Then, in each 15-day period in row 4, the amount of time decay increases. From column 2 to column 3, the value of the 100 Call decreases by 50 cents. From column 3 to column 4, the decrease is 56 cents. From column 4 to column 5, the decrease is 67 cents. From column 5 to column 6, the decrease is 86 cents. And, finally, from column 6 to column 7, the decrease is 2.05. This increase in time decay for each 15-day period is reflected in the theta which decreases from column 1 to column 6 before going to zero at expiration in column 7.

  

The third guideline is that, **at some point, for in-the-money options and for out-of-the-money options, time decay increases for a while and then decreases as expiration approaches, which means that theta increases close to expiration**. Look across row 1 where the stock price is 90 and the 100 Call is out of the money. The value of the 100 Call in row 1 is 1.35 in column 1 and 1.05 in column 2. This is a decrease of 30 cents (0.30) in 15 days. Time decay then decreases from column 2 to column 3 (29 cents) and continues to decreases for the rest of row 4. From column 3 to column 4 the decrease is 28 cents. From column 4 to column 5 the decrease is 26 cents, and from column 5 to column 6 the decrease is 19 cents. Finally, the smallest amount of 15-day time decay occurs from column 6 to column 7 (3 cents).

  

This third guideline is especially important for option traders who have always heard — and who have always believed without question — that "options decay more as expiration approaches. Therefore, I should sell shorter-term options." While this statement is true for at-the-money options, many writers of covered calls do not sell at-the-money calls. Rather, they tend to sell out-of-the-money calls, for which this statement is not true!

  

Time decay for at-the-money calls (row 4 in Table 1) and for out-of-the-money calls (row 1 in Table 1) are graphed in Graph 1. If selling covered calls is one of your favorite strategies, Graph 1 is worth studying.  
   
**Conclusion**

  

Time decay is an important part of option pricing. Options traders, therefore, must understand it. Theta estimates how much option prices decrease when time to expiration decreases by "one unit." When using computer programs that calculate option values, be sure that you know how one unit of time is defined in the theta calculation. Also, theta is a negative number, and this can cause trouble when discussing how time decay increases or decreases.

  

For at-the-money and close-to-the-money options, time decay increases as expiration approaches. At some point, however, for in-the-money options and for out-of-the-money options, time decay increases for a while and then decreases as expiration approaches. Writers of covered calls who tend to sell out-of-the-money calls, therefore, might consider selling longer-term calls (60-90 days), rather than shorter-term calls (30 days or less). 




