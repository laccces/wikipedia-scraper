import requests
from bs4 import BeautifulSoup

# Send an HTTP request to the URL of the webpage you want to access
url = 'https://en.wikipedia.org/wiki/Persona_4'
response = requests.get(url)

# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(response.text, 'lxml')

# Specify the class name you want to reference
class_name = 'mw-parser-output'

# Find all the div elements with the specified class name
div_elements = soup.find_all('div', class_=class_name)

# Iterate through the elements and perform any desired operations
for div_element in div_elements:
    print(div_element)


