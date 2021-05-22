# Birthday Logger

## Logic

- Get existing birthdays from the file
- Add data
  - Get data from the user
  - Append the new data to the existing file
- Print data
  - Sort the dictionary by using datetime objects
  - Print the result

## Assignment

Each time the program runs, `birthdays.json` file is read. If the file is
missing or empty, the program will error out. Fix this by creating a file with
the contents `{}` if it doesn't exist. If the file is empty, write `{}` to it.
