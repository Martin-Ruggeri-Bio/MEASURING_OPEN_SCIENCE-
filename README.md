# MEASURING-OPEN-SCIENCE
## Testing Paper Generator

The paper generator randomly generates the data of papers, their authors and their citations. This is done in order to test the data processing that we coded.
## Real Paper Processor

The search for papers should be done with web scraping in the public repositories of NASA, other space organisations and public entities such as google scholar.
The processing of the papers should be done with Natural Language Processing in python with the Pandas library, Scikit-learn, XGBoost, TextBlog, Keras among others in order to obtain from the pdf the necessary parameters to send to the Paper class to map the data.

## Papers

The Paper class is used to map the papers so that they have the necessary attributes to work.
When loading a citation in a paper, it saves a memory reference of the paper object that is citing and to that paper is loaded a memory reference of the paper object that cited it, through the attributes of country we will be able to know from which country is the cited paper and the citator as well as the category institution and contact information of the author.
## Paper upload service

This service makes 1000 calls to the paper processor to generate the parameters to create 1000 objects of the paper class.
Then each paper is loaded with the corresponding citations. This process not only modifies the content of the attribute that stores the citations of the paper but also modifies the citation attribute of the paper that was cited along with other quantitative and categorical measures of these citations such as the number of national and international citations and the country information of the paper that was cited.
It then generates a dataframe where it stores all the papers. It will send them to different functions that will apply data science to filter, sort and process the data to obtain valuable ouput.
## Data Science

Here the different filters are applied and open science metrics are created with different functions to create different dataframes and save them in csv files that will be sent to data analyst software such as data studio to generate graphs to represent the information in a user friendly way.
## Data Analist

Here are some graphs to represent some of the tables created, the link to data studio is attached.

Translated with www.DeepL.com/Translator (free version)
https://datastudio.google.com/reporting/c0b4b8df-5ac1-46fa-9aee-162b30a2d6fe
