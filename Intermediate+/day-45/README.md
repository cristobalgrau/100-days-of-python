# Day 45: Web Scraping with Beautiful Soup

## Project: 100 movies that you must watch

The "100 Movies that You Must Watch" project is a Python script that scrapes the [empireonline.com](https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/) archive webpage for a list of top movies and saves the titles to a text file. This project introduces basic web scraping techniques using the requests and BeautifulSoup libraries and demonstrates how to handle HTML content and file operations.

### Key Features:

- **Web Scraping**: Fetches and parses HTML content from a webpage.
- **Data Extraction**: Extracts movie titles from the parsed HTML.
- **File Operations**: Writes the extracted movie titles to a text file.

## Libraries Used:

- `requests`: For making HTTP requests to fetch the HTML content of the webpage.
- `BeautifulSoup`: For parsing HTML content and extracting data

### Implementation:

#### Web Scraping with requests and BeautifulSoup

1. Fetch HTML Content:
- The `requests` library is used to send an HTTP GET request to the URL.
- The response encoding is set to the apparent encoding to handle special characters correctly.

2. Parse HTML Content:
```python
soup = BeautifulSoup(response.text, "html.parser")
```

- The HTML content is parsed using `BeautifulSoup` with the `html.parser` to create a BeautifulSoup object.

3. Extract Movie Titles:
```python
titles = soup.find_all(name="h3", class_="title")
movie_titles = [title.getText() for title in titles]
movie_titles.reverse()
```

- The find_all method is used to find all `<h3>` elements with the class title.
- The text content of each element is extracted and stored in a list, which is then reversed to get the correct order.


#### File Operations:

1. Write to Text File:
- The movie titles are written to a text file named `movies.txt` with UTF-8 encoding to handle special characters.

## Learning Objectives:

- **Web Scraping**: Learn to use the requests library to fetch HTML content from a webpage and the BeautifulSoup library to parse and extract data from the HTML.
- **Handling HTML Content**: Understand how to handle special characters in HTML content by setting the correct response encoding.
- **Data Extraction**: Practice extracting specific elements from HTML using BeautifulSoup methods like `find_all`.

## Result

### Watch the full web page scrapped [here](https://web.archive.org/web/20200518055830/https://www.empireonline.com/movies/features/best-movies-2/)

![image](https://github.com/cristobalgrau/100-days-of-python/assets/119089907/39ee2251-06b3-4d9f-b242-84953d25ea1a)

### Watch the txt file generated [here](https://github.com/cristobalgrau/100-days-of-python/blob/main/Intermediate%2B/day-45/movies.txt)
