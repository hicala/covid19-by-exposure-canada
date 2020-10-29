import requests
import bs4
from bs4 import BeautifulSoup as bs


# load and get the website
response = requests.get('https://health-infobase.canada.ca/covid-19/epidemiological-summary-covid-19-cases.html')

# create the soup
soup = bs4.BeautifulSoup(response.text, "html.parser")

###### Pending 

# 1. Import Modules................ [ DONE]
# 2. Get the URL link.......... [ DONE]
# 3. Navigate the URL Data Structure .......... [ DONE]
# 4. Testing out data requests
# 5. Write data to a file in pseudo-code:
    + Open up a file to write in and append data.
    + Set up parameters for the while loop. 
    + Write headers
    + Run while loop that will write elements of the array to file
    + When complete, close the file
# 6. The output file in CSV format.