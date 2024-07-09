import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


response = requests.get(URL)

# Check the encoding of the response to avoid error due to special characters from HTML
response.encoding = response.apparent_encoding

soup = BeautifulSoup(response.text, "html.parser")

titles = soup.find_all(name="h3", class_="title")
movie_titles = [title.getText() for title in titles]
movie_titles.reverse()


# Write the movie titles to a text file with UTF-8 encoding to avoid special characters being wrote
with open("movies.txt", "w", encoding="utf-8") as file:
    for movie in movie_titles:
        file.write(f"{movie}\n")

print("txt file created successfully!")
