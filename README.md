# Git Auto Info Bot

A Python tool to automatically send WhatsApp notifications about Git events or custom messages to a list of contacts. This project uses `pywhatkit` to send instant WhatsApp messages.

## Features
- Send a predefined or custom message to multiple WhatsApp numbers instantly.
- Easily configurable via a JSON file.
- Command-line interface for version info and message override.

## Requirements
- Python 3.7+
- A known browser, Like Chrome, FireFox
- WhatsApp account logged in on WhatsApp Web
- Internet connection

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/neeraj-r-rugi/WhatsAPP-Bot
   ```
2. **(Optional) Create a virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install pywhatkit
   ```
   `Use the requirements.txt for testing and development. Not needed for running the Bot`

## Usage

### Command Line Arguments
- `-V`, `--version`: Display the current build version.
- `-m`, `--message`: Override the message in `whatsapp.json`.
- `-c`, `--country-code`: Change the country code for WhatsApp numbers (default: +91).


### Example
```bash
# Show version
python main.py -V

# Send a custom message
python main.py -m "Custom message to send"

# Change country code (e.g., to US)
python main.py -c "+1" -m "Hello from the US!"
```

## Configuration
### `whatsapp.json`
This file contains the message and the list of phone numbers to notify.
```json
{
    "message": "Hello From GIT BOT!",
    "numbers": [
        "123456789"
    ]
}
```
- **message**: The default message to send.
- **numbers**: List of phone numbers (without country code).

## How It Works
- The script loads the message and numbers from `whatsapp.json`.
- You can override the message using the `-m` argument.
- For each number, the script sends an instant WhatsApp message using `pywhatkit`.


## Notes
- The country code is set to `+91` (India) by default, but can be changed using the `-c` or `--country-code` argument.
- Make sure Chrome is installed and you are logged into WhatsApp Web.
- The script will open a browser tab for each message sent.

## Troubleshooting
- If messages are not sent, ensure Chrome is installed and WhatsApp Web is logged in.
- Check your internet connection.
- For issues with `pywhatkit`, refer to the [pywhatkit documentation](https://github.com/Ankit404butfound/PyWhatKit).

## License
GNU GPL V3.0

## Author
- [Neeraj R Rugi](https://github.com/neeraj-r-rugi/)
- [Hamza Sahapurwala](https://github.com/Hamza-Sahapurwala/Hamza-Sahapurwala)
