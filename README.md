# WC CLI Tool

A simple command-line tool to analyze text files and display various statistics, built using Python and Typer, based on the wc UNIX tool.

## Features

- Count the number of bytes in a file
- Count the number of lines in a file
- Count the number of words in a file
- Count the number of characters in a file

## Installation

Ensure you have Python installed on your system (Python 3.x recommended). Then, install Typer if you haven't already:

```
pip install typer
```

## Usage

Run the script using the following command:

```
python main.py [options] <filepath>
```

## Options

- `-c`: Show the total bytes in the file
- `-l`: Show the total number of lines in the file
- `-w`: Show the total number of words in the file
- `-m`: Show the total number of characters in the file

## Example Usage:

1. Get all statistics:\
   `python main.py example.txt`\
   **Output**:\
   `1234 56 7 example.txt`\
   _(Bytes, Lines, Words, Filename)_

2. Get only the word count:\
   `python main.py -w example.txt`\
   **Output**:\
   `123`

3. Get the line count and character count:\
   `python main.py -l -m example.txt`\
   **Output**:
   ```
   56
   1200
   ```

## Error Handling

The script gracefully handles the following errors:

- **File Not Found**: Displays an error message if the file does not exist.

- **Permission Denied**: Displays an error message if the file cannot be accessed due to permissions.

## License

This project is licensed under the MIT License.

## Author

Shubhankar Rai
