# Day 30 - Errors, Exceptions, and JSON Data: Improving the Password Manager

This day we made 2 projects handling errors and manipulating JSON files.

## Project #1: Added error handling for NATO alphabet Project 

In this project, we used the same code for the project NATO Alphabet that we made on day 26 and we added the feature to handle the error when the user
enters a text with no letters characters, such as numbers, special characters, or blank spaces. To achieve this we just introduce the exceptions in the code as follows:

```python
keep_trying = True
while keep_trying:
    word = input("Enter a word: ").upper()

    #Create a list of the phonetic code words from a word that the user inputs.
    try:
        phonetic_word = [nato_alphabet[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(f"Your phonetic letters are: {phonetic_word}")
        keep_trying = False
```

The `try` block attempts to convert the input word into its phonetic alphabet equivalent. If the user inputs non-alphabetic characters, a `KeyError` is raised, 
and the program catches this exception, prompting the user to try again. This loop ensures that the user is continuously prompted until they enter a valid word 
consisting solely of alphabetic characters.

### Result: 

![image](https://github.com/cristobalgrau/100-days-of-python/assets/119089907/b2c539b7-5e41-40a6-b0e9-bee75b1ac1e6)

## Project #2: Improving the Password Manager

This update to the Password Manager project made on day 29, introduces error handling for file operations, the JSON file management,  and a search feature to quickly retrieve saved passwords. 
These enhancements improve the application's robustness and usability.

### Key Features added:

- **Data Persistence:** Save passwords in a JSON file format.
- **Error Handling:** Handle missing data files and empty input fields gracefully.
- **Password Retrieval:** Search for and display saved passwords for specific websites.

### Library added:

- `json`: Reads from and writes to a JSON file for data persistence.

### Implementation of the new features:

The updated Password Manager project incorporates error handling and a search functionality. 

Error handling is implemented to manage situations where the JSON data file might not exist. If the data.json file does not exist, the application creates a new file and saves the data. 
This prevents the application from crashing when attempting to read a non-existent file.

```python
        try:
            with open("data.json", "r") as file:
                # reading old data
                data = json.load(file)
        except FileNotFoundError:
            data = new_data
        else:
            # Updating old data with new data
            data.update(new_data)

        with open("data.json", "w") as file:
            # opening the json file and write the information with indent, so it's more readable
            json.dump(data, file, indent=4)
            website_entry.delete(0, END)
            password_entry.delete(0, END)
```

The new search feature allows users to quickly find saved passwords. When clicking the search button, it triggers reads the data.json file and retrieves the password and email associated with the
entered website. If the website is not found or the file does not exist, appropriate error messages are displayed. It was added the error handling here in case the user tries to search a website when there is no data file.

Here is the function `find_password()` for this new feature:
```python
def find_password():
    website = website_entry.get()

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found.")
    else:
        if website in data:
            messagebox.showinfo(title=website, message=f"Email: {data[website]["email"]}\n"
                                                       f"Password: {data[website]["password"]}")
        else:
            messagebox.showerror(title="Error", message=f"No details for {website} exists")

        # Another way to do it with exceptions
        # try:
        #     messagebox.showinfo(title=website, message=f"Email: {data[website]["email"]}\n"
        #                                                f"Password: {data[website]["password"]}")
        # except KeyError:
        #     messagebox.showerror(title="Error", message=f"No details for {website} exists")
```

### Result:

![image](https://github.com/cristobalgrau/100-days-of-python/assets/119089907/df6b4322-ceea-451c-b06f-fd8f691dde3f)

![image](https://github.com/cristobalgrau/100-days-of-python/assets/119089907/67871f95-4a79-47db-9acd-20f715c8a746)

![image](https://github.com/cristobalgrau/100-days-of-python/assets/119089907/a3d98229-221a-4af0-9a0f-81b599203c02)

