import requests
from bs4 import BeautifulSoup

# URL to be scrapped
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Send a GET request to the URL
response = requests.get(URL)

# Create a BeautifulSoup object for parsing the HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Find all elements with class 'title' and name 'h3'
titles = soup.findAll(class_='title', name='h3')

# Extract the text from each title element
movies = []
for title in titles:
    movies.append(title.getText())

# Reverse the list of movies
movies.reverse()

# Write the reversed list of movies to a file
with open('movies.txt', 'w') as file:
    for movie in movies:
        file.write(f'{movie}\n')
