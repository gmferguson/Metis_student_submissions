# MTA_TurnstileData_Analysis

## Exploratory Data Analysis: New York City Subway Traffic and Demographic
We hit the ground running in our first week at the Metis Data Science Bootcamp!
We had a pretty tight timeframe for our first project! It was assigned on Monday, and due on Friday.

We were given a scenario in which a ficticious non-profit company WomenTechWomenYes (WTWY) had asked us to perform some EDA to explore MTA turnstile data in NYC. WTWY wants to send out volunteer teams out to subway stations to promote their summer gala to increase their brand awareness, participation, and potentially increase donations.They are also interested in collecting email addresses.The main aim of this analysis was to provide recommendations on where to send WTWY's volunteer teams.

## Our Approach
Our strategy to provide valuable recommendations involved finding the top subway stations with respect to foot traffic, and then verifying that the population in the surrounding areas held demographics that could place them in WTWY's target audience.
**Our approach was as follows;**

**1** We analyzed MTA turnstile data for NYC to calculate the  number of people passing through a subway station in the 3-month period preceding the summer gala. **(Analysis_MTA_Turnstile_2018_data.ipynb)**

**2** Analyzed data on local technology companies and universities as a proxy for greater percentages of women and tech-involved individuals who may be especially receptive to the WTWY outreach efforts.**(Analysis_Techcenters_near_subways.ipynb)**  

**3** Analyzed data about WalkScore.com to identify which stations may have larger populations of non-subway riders walking past the subway entrances.**(Analysis_Walkscore_Data.ipynb)**

**4** Analyzed demographic information from the U.S. Census on local tech-centered companies and residences with greater affluence, as a proxy for a larger impact to the WTWY fundraising and outreach efforts.**(Analysis_Demographic_Data_code.ipynb)**

**5** Calculated a final "Final Score", summing the four normalized scores for the turnstile, technology, walking, and census data.



**In summary** we recommended these **top-five subway stations** for placing WTWY volunteers:

**1** Grand Central at 42nd St.

**2** World Trade Center at Cortlandt St

**3** 34th St at Herald Sq.

**4** Union Square and 14th St.

**5** Penn Station at 34th St.



This project was done on a pretty tight timeframe, and there was a lot more that we could have done!A few things that would be **next steps** in this analysis are:

**1** Analyze the outliers in depth

**2** Investigate the spike in number of subway users on certain days of the week.

**3** Try different values to filter outliers.

**4** Analyze traffic distribution by time of day 

**5** Incorporate a better weighting scheme to different factors ( location of tech centers, universities, demographic data) to calculate the final score for each station.

