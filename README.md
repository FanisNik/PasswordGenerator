# Password Generator with GUI

This is a simple password generator application built using Python and the Tkinter library. The application allows users to generate a secure password based on their desired length (between 4 and 25 characters). It includes additional functionality to copy the generated password to the clipboard.

## Features

- **Password Generation**: Generate a secure password with a combination of uppercase letters, lowercase letters, numbers, and symbols.
- **Customizable Length**: Users can input a custom password length (minimum 4 characters, maximum 25 characters).
- **Clipboard Support**: Copy the generated password to the clipboard with a button press.
- **Error Handling**: Displays error messages for invalid input (e.g., entering a non integer or invalid length).

## Requirements

To run this project, you need the following Python packages installed:

- `tkinter` 
- `pyperclip`
  
You can install the required external package with pip:

```bash
pip install pyperclip
