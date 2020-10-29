# Web Scraping using Beautiful Soup

## Summary

I am using Beautiful Soup for the this Python app. Beautiful Soup is a Python library for parsing data out of HTML and XML files (aka webpages). It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree. 

The major concept with Beautiful Soup is that it allows you to access elements of your page by following the CSS structures, such as grabbing all links, all headers, specific classes, or more. It is a powerful library. Once we grab elements, Python makes it easy to write the elements or relevant components of the elements into other files, such as a CSV, that can be stored in a database or opened in other software.

## Data source and verifications

The data I used came from the Public Health Agency of Canada and the data is the source for the visualization of the Epidemic curve related to COVID-19 cases in Canada by date of illness by exposure. The information also  inlcudes the period of time where it is expected that cases have occurred but have not yet been reported nationally. 

Reference: https://health-infobase.canada.ca/covid-19/epidemiological-summary-covid-19-cases.html

## Main goal

+ To access all of the content from the source code of the webpage.
+ Use with Python as a main webscraping tool.
+ Parse and extract data. 
+ Save the info in CSV file for further analysis.

## Methodology

1. Import Modules
2. Get the URL link
3. Navigate the URL Data Structure
4. Testing out data requests
5. Write data to a file in pseudo-code:
    + Open up a file to write in and append data.
    + Set up parameters for the while loop. 
    + Write headers
    + Run while loop that will write elements of the array to file
    + When complete, close the file
6. The output file in CSV format.

## Data info extracted.

Date of illness, Newly reported cases, Domestic - Contact with a COVID case,Domestic - Contact with a traveller, Domestic - Unknown, Travelled outside of Canada, Information pending

## Next Steps.

+ Establish a data visualization platform as dynamic dashboard for reporting in D3.js....[Pending]

