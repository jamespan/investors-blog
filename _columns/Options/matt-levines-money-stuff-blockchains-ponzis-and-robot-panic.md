---
layout: page
title: >-
  Matt Levine's Money Stuff: Blockchains, Ponzis and Robot Panic
date: 2016-02-01 17:45 -0800
author: BLOOMBERG NEWS
origin_url: https://www.investors.com/research/options/matt-levines-money-stuff-blockchains-ponzis-and-robot-panic/
---





*The opinions expressed in this article by Matt Levine are his and not those of Bloomberg News*.


Blythe Masters' Digital Asset Holdings continues to make blockchain inroads, and I continue not to quite understand it. The latest is "a trial project" with JPMorgan, which is "looking at several applications for the technology, including addressing liquidity mismatches in JPMorgan’s loan funds, which normally let investors take out their money at short notice -- even though the underlying assets can require much more time to sell." People are worried about loan market liquidity, but they are soothing their worries with the blockchain.


The traditional liquidity-mismatch worry is that you can take money out of a fund quickly, but it takes a longer time to find a buyer for the underlying assets at an acceptable price. This appears to address a slightly different worry, one of settlement timing: If you ask for your money back, and you get it in three days, and meanwhile JPMorgan was easily able to find a buyer for the underlying loan at a reasonable price, but it takes two weeks to settle that trade, then **JPMorgan** ([JPM](https://research.investors.com/quote.aspx?symbol=JPM)) is floating you money while it waits to get paid. Which is not optimal for JPMorgan. Still:


Mr. Pinto said loans were a good place to start trialing blockchain technology, because “the settlement process is complex with lots of manual intervention and multiple parties."


See, this is the part I don't understand. If you think the blockchain is a better database than other databases, then replacing other databases with blockchains is a good idea. If your settlement process, for legal or customary or whatever reasons, requires lots of manual intervention from multiple parties, then just looking into a mirror and saying "blockchain!" three times won't solve that. You have to go to all those multiple parties and convince them to stop intervening manually. Once you've done that, sure, set up an electronic database. Maybe a blockchain, why not. But the problems here seem to be prior to the choice of database architecture. The last time we talked about Digital Asset, just over a week ago, it was because it had won a contract with the Australian Stock Exchange, and the explanation of why that was an ideal place to start trying out blockchain was the opposite of what it is here: Stock settlement in Australia is not a complex process with lots of manual intervention; it's a fully dematerialized stock market with a single centralized repository of stock information. It's just an electronic database, and Digital Asset thinks it has a better database.


Meanwhile, bizarrely, "a unit of Depository Trust & Clearing Corp., the dominant processor of repurchase agreements, or repos, between securities dealers, has told traders it will stop facilitating certain interbank repos as of July 15." Specifically, dealers who clear through JPMorgan will no longer be able to do general collateral finance repos with dealers who clear through **Bank of New York Mellon** ([BK](https://research.investors.com/quote.aspx?symbol=BK)). The problem seems to be a ... failure of databases?


In an effort to align interdealer GCF trades and other repos, BNY, J.P. Morgan and DTCC set out to build new technology for swapping information about the cash and securities being exchanged between clients of the clearing banks.


J.P. Morgan completed a series of enhancements, and the DTCC unit completed the majority of its own, but BNY determined that the technology work would have taken too much time and resources, people familiar with the situation said.


If only JPMorgan had access to a magical kind of database that made clearing quick and easy while also somehow effortlessly solving interpersonal problems.


"Chinese police have arrested more than 20 people associated with 'a complete Ponzi scheme' that allegedly took more than 50 billion yuan ($7.6 billion) from investors," and I like the rigor there in distinguishing "a complete Ponzi scheme" from, you know, a little bit Ponzi. Lots of semi-to-not-at-all-legitimate businesses have a bit of a Ponzi to them; if you're running a fraud anyway, sometimes you might have to take money from a new investor to pay an old investor to go away. But the Ponzi as a complete business model, especially in enormous size, is less common. This alleged full Ponzi was called Ezubao; it was (ostensibly) a peer-to-peer lending platform, and its "risk controller, who is also under detention, was quoted by Xinhua as admitting that '95% of [our] projects are fake.' " I guess that leaves 5% of not-Ponzi though.


According to the SEC’s order instituting a settled administrative proceeding, QED Benchmark Management LLC and its founder/fund manager Peter Kuperman avoided disclosing heavy trading losses to investors by using a misleading mixture of hypothetical and actual returns when providing the fund’s performance history. After obtaining millions of dollars from investors based on these misrepresentations, QED Benchmark and Kuperman deviated from their stated investment strategy and poured most of the fund’s assets into a single penny stock.


I would score this one as about zero percent Ponzi, but it's very odd. From the Securities and Exchange Commission order, it seems that QED Benchmark poured a bunch of money into stock and convertible debentures of a company called Emo Capital Corp. Emo's stock did not trade much. QED Benchmark kept marking up its holdings. Then the stock started falling. QED Benchmark negotiated a "put option" with Emo's promoters, under which QED Benchmark could sell the stock to the promoters at 72 cents, even though the market price was in the mid-40-cents. QED Benchmark paid nothing for this in-the-money put. "The fund administrator accepted this document as evidence of the holdings’ value, and the fund’s statements to investors reflected a 72-cent valuation for the next six months." After that, with the stock now down to 4.3 cents per share, "Kuperman told the fund administrator that he and the put issuer would 'retire the existing March 72-cent put and replace it with (a) Dec. $1 put.' " At this point, the administrator had had enough:


So we are expected to believe that a third party would give you the right to sell nearly 4 million shares of a stock at $1 per share, even though its current price is roughly 4 cents per share, in exchange for absolutely nothing?


The “put” had an intrinsic value of nearly $3.7 million and a third party sold it to you for zero?


I don’t think so.


Right on, administrator. Who was scamming whom, exactly, here? Kuperman agreed to reimburse his investors and pay $75,000 to the SEC.


In other fraud news, Robert Bray was convicted of insider trading in a case that involved both golf and cocktail napkins:


As the government proved at trial, in June 2010, Bray was tipped by a friend who was an executive at Boston-based Eastern Bank Corp. (“Eastern Bank”) that Wainwright would be acquired. The tip -- more than two weeks before the acquisition was publicly announced -- was passed on a napkin slipped to Bray over drinks at a country club bar in Watertown where both men are members. On Monday, June 14, 2010, Bray called his broker to ask how he could buy 25,000 shares of Wainwright stock, which he acknowledged “kinda sounds crazy,” given how thinly the stock traded.


Turns out, it was. We discussed this case when Bray was charged in August 2014; it was the second insider trading case brought that summer at the same country club. There must be something in the water, or the cocktails, or the cocktail napkins.


Also there is this:


Last month, an undercover federal agent set up an account with Liberty Reserve, a virtual currency exchange based in Costa Rica. Registering online, the agent entered the name “Joe Bogus,” typed the account name as “tostealeverything,” and chose the address “123 Fake Main Street.”


And:


He transmitted hundreds of LR dollars between the Joe Bogus account and another undercover account, identifying one transaction as “your share of the cashout” and another “for the cocaine.”


I am tempted to say "if a user on your money-transfer site identifies a transaction as 'for the cocaine,' then he is a cop," but that's not right. That's how like half of transactions on Venmo are identified, and it never stops being hilarious. And I'm still writing dumb jokes in the "memo" field of my checks. But I like imagining these undercover FBI agents thinking hard about how real criminals would transfer money, and concluding that identifying the transfers as "for the cocaine" added exactly the right touch of verisimilitude.


Ahh, millennials.


Here's apparently an investing thesis?


“People want to buy happiness,” Huang said at a London cafe in January. “An experience is unique because it gives them that in three stages: the anticipation, the event itself, and the memories after. Not only does that final stage last forever, but you can also share it.”


The thesis that results from this is long companies that sell experiences (and happiness), short companies that sell goods. There is sort of a meta-thesis, though, which is that if the rising millennial generation is interested in authentic experiences and not the accumulation of wealth, won't that be bad for stock-market inflows? Anyway, in other news, "the biggest 'robo-advisers' are relying on old-school call centers and blog posts to calm anxious investors, trying to persuade them that there is no need to abandon the algorithms in times of heightened volatility." I hope the call center dialogue goes like this:


YOU: I'm panicking, I tell ya, panicking! Sell everything!


EERIE ROBOT VOICE: I'm sorry Dave, I'm afraid I can't do that.


YOU: Who is Dave?


Naked shorts.


People get really mad about naked short selling, so much so that Gretchen Morgenson wrote a column about **Goldman Sachs**' ([GS](https://research.investors.com/quote.aspx?symbol=GS)) naked-shorting settlement that ends with a quote from a guy who ... seems not to have read the settlement?


In an interview, Mr. Shapiro, a former federal prosecutor and United States attorney, questioned the recent SEC settlement. “I’m very curious to understand what Goldman Sachs admitted to the SEC,” he said, “and why $15 million was considered to be an adequate punishment.”


I mean, you can just read the settlement! (I wrote about it a couple of weeks ago.) Basically Goldman admitted that it used a dumb method for giving "locates" to clients that wanted to short stocks. This dumb method might, on the surface, look like it would allow an unacceptably large amount of naked shorting, but in fact it didn't -- "Goldman’s rate of failures remained low and did not substantially change" while it used the dumb method -- which might explain why $15 million was considered to be an adequate punishment.


Elsewhere in market-structure-ish stuff, the New York Stock Exchange and Nasdaq "are so upset the SEC didn’t offer either of them a seat on the agency’s Equity Market Structure Advisory Committee that they have spurned offers by the panel to participate in policy deliberations held by its members behind closed doors." And my Bloomberg View colleague Michael Lewis has extremely odd ideas about Occupy Wall Street and IEX.


Are bankers evil, etc.


Here is Elizabeth Warren's report on "Rigged Justice: 2016: How Weak Enforcement Lets Corporate Offenders Off Easy." It includes the claim that the foreign-exchange fixing scandal involved banks who "for more than five years manipulated exchange rates in a way that made the banks billions of dollars at the expense of clients and investors." That seems like a wild overestimate to me: I think the absolute cap on revenue from FX fixing is under $2 billion, and I suspect it's orders of magnitude less. It strikes me as unproductive to assume that all bank scandals are the same size. Libor manipulation was big! Mortgage fraud was bigger! FX was sort of medium-size at worst.


Here is a symposium at Concurring Opinions on the book "Better Bankers, Better Banks." Here is a story about how the outside monitor's report on **HSBC** ([HSBC](https://research.investors.com/quote.aspx?symbol=HSBC)) will be made public. Here is "Does Regulation Crowd out Private Ordering and Reputational Capital?" And Maureen Sherry, a former managing director at Bear Stearns who wrote an opinion piece titled "A Colleague Drank My Breast Milk and Other Wall Street Tales," has also written a novel about Wall Street, "a breezy comedy in the style of 'Bridget Jones’s Diary'":


In a good year, Isabelle earns $3 million. Ms. Sherry said she considered how that would play to readers, but she wanted to be realistic. “I hate the term ‘Manhattan poor,’ ” she said, but added that after taxes, as a couple with one income and three private-school tuitions, “They weren’t living large.”


People are worried about unicorns.


"There were no U.S. IPOs in January, the first monthlong drought since September 2011," and people are worried about unicorns that might not be able to do initial public offerings:


The fate of biotechnology companies is most in focus. While an IPO slowdown is problematic for all sorts of companies, including the technology sector in which dozens of companies have raised money privately at billion-dollar implied valuations, biotech is getting special scrutiny from investors because the sector is widely viewed as the most vulnerable to diminishing access to public funding.


Elsewhere, this possibly parodic essay about "How Soylent and Oculus Could Fix The Prison System" (samples: "I believe we could fix all of these problems using the Silicon Valley idea of 'first principles,' or boiling down a problem to its core and building a new solution from the ground up"; "I’d outsource the laundry to FlyCleaners to save on facilities and admin"; "You’d weigh in on a Fitbit Aria scale, so they could digitally track your weight alongside your other vitals") should make you worry about unicorns. Meanwhile at Bloomberg Gadfly, Rani Molla asks how big Uber could get.


People are worried about bond market liquidity.


Start your week of worrying off right with "'Seismic' shock awaits bond liquidity." The particular shock involved here is the European Mifid II pre-trade transparency rules, which worry people:


A senior executive at a large U.S. fund company, who requested anonymity, said: “Our head of fixed-income trading says that if he didn’t have young children, he would retire the day this comes in. It is not going to be pretty. It would undoubtedly affect liquidity.”


The concern is that the rules will treat many illiquid bonds as liquid, require pre-trade transparency and firm quotes, and generally make it hard to negotiate trades.


Things happen.




