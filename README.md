# UMDdataChallenge21
UMD Data Challenge 2021 - COVID-19 Global Symptoms Tracker
Team42:
* Gabriel Sestieri
* Theodore Gaidis
* Manar Al-badarneh
* Brendan Goodhue

## Background
University of Maryland’s Joint Program in Survey Methodology and Carnegie Mellon
University’s Delphi Research Group, collaborated with Facebook to invite people
to participate in surveys that ask about how they are feeling, including any 
symptoms they or members of their household have experienced and their risk 
factors for contracting COVID-19. The surveys are designed to provide valuable
information to help monitor and forecast how COVID-19 may be spreading, 
without compromising the privacy of the people who took the surveys. Facebook
does not share who took the surveys with our academic partners, and the 
universities do not share individual survey responses with Facebook. With
over 2 billion people on Facebook, Data Challenge Competitors are in a 
unique position to use the data to study COVID-19, such as how the pandemic
is affecting population movement trends, and understand which areas may be
at risk of an outbreak based on population characteristics and symptoms. 


## Abstract
Our research aims to identify and analyse the relationships between COVID-19 
indicators from the UMD COVID-19 World Survey Data API to inform the audience 
about certain patterns and trends we found. The COVID-19 World Survey Data API
contains 21 indicators recorded from a Facebook survey answered from around the 
world. We automated a script to consolidate the data for each country through 
iterative API calls. Each CSV file contains 23 columns including fields such as
country name, date of each reporting, and the smoothed data for each of the 21 
indicators on each date.  We will cross compare the indicator values between 
countries to find insights into how their response to the pandemic affected 
these indicators, and how these indicators may uniquely impact one another in
each country we analyze. This format of data also allows us to perform time 
series analysis. Using data visualization tools will allow us the ability to 
express our findings of our technical work for the general public to easily 
understand and interpret. Our analysis can help to prepare for a rise or fall 
in people experiencing symptoms and ultimately help policymakers and Public 
health officials in determining which country or region would benefit the most
from added healthcare assistance.

## Summary
For the 2021 UMD Data Challenge our team chose to analyze the level three, 
COVID-19 World Survey Data API. In order to acquire data for this project we 
built a data scraper.  It used a series of loops to build the links necessary 
to call the API for every data point it contained.  The program built links for
each of the 21 indicators for every date and country available. After cleaning 
the data and getting it into workable CSV formatting we began to narrow down our 
problem statement. Our motivation to solve these problems came from wanting to
make an impact in the fight against COVID. People all over the world are dealing
with the impact and burden of disease that COVID-19 has left. Using the data
available to us we were motivated to help the general public and Public Health
officials with our data analysis and findings. 

Additional data analysis led us to focus on three primary questions for our problem
statement; the first being, for countries in the Schengen Area (the countries in
Europe that have open borders with one another), does a spike in COVID-19 related 
indicators in one country correlate to a delayed spike in indicators in their 
neighboring countries? The next question we posed was do the people’s trust in 
government, trust in healthcare officials, and trust in the WHO, have an effect
on the number of people willing to take a vaccine? To tie together the rest of 
our findings we asked how do social behaviors (contact with someone outside your
household) correlate to mask wearing habits, COVID-19 cases in the community, and financial worries?

In analysis of our first primary question we came to the conclusion that there is a correlation in COVID-19 spikes between neighboring countries in the Schengen region. All countries of the region had similar trends in the indicators we deemed most important to focus on. Next we strove to answer how notable figures and peoples' opinions of trust in the vaccine affect their peers' willingness to take the vaccine; we found healthcare officials garnered the most trust while politicians, the least. Finally, in our analysis of survey respondents mask wearing habits we found that in summer months mask wearing decreased however this did not lead to a notable increase in COVID-19 like symptoms.
