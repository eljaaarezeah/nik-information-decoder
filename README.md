# NIK Information Decoder

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/eljaaarezeah/nik-information-decoder/blob/9f829b621b8e0127326857470bca5fab152d8d92/LICENSE)
![Python](https://img.shields.io/badge/Python-3.14-blue)

NIK Information Decoder is a Python-based CLI application for validating and decoding information from Indonesian National Identification Numbers (NIK). This project was developed as a learning project to apply programming concepts such as input validation, data processing, and CLI application development.

## Features

- NIK length validation
- Numeric-only NIK validation
- Regional code validation
- Province, regency/city, and district lookup
- Birth date decoding from NIK
- Gender identification from NIK
- Age calculation
- Total days lived calculation
- Birthday countdown
- Generation identification
- Age category identification
- Zodiac sign identification
- Current date and time display
- CAPTCHA verification
- Interactive CLI menu
- Program information through the About menu

## Tech Stack

- **Language:** Python 3.14
- **Data:** JSON
- **Dependency:** python-dateutil
- **Interface:** Command-Line Interface (CLI)

## Requirements

- Python 3.14

## Installation

### 1. Install Python
Make sure Python 3.14 is installed on your system.

### 2. Clone the repository
```bash
git clone https://github.com/eljaaarezeah/nik-information-decoder.git
```
### 3. Navigate to the project directory
```bash
cd nik-information-decoder
```
### 4. Install the required dependencies
```bash
python -m pip install -r requirements.txt
```

## Usage

Run the program with:
```bash
python main.py
```
The program provides the following menu options:
```text
[1] Decode NIK
[2] About
[3] Exit
```
Select an option by entering the corresponding number.

## Project Structure

```text
nik-information-decoder/
├── main.py
├── generate_database.py
├── wilayah.json
├── requirements.txt
├── README.md
└── LICENSE
```

## Database

The program uses `wilayah.json` as its regional code database.

The `generate_database.py` script is used to generate the regional database used by the program.

## Disclaimer

This project was developed for educational and programming purposes.

It is not an official government service, and the information provided by this program should not be used as official identity verification.

## License

This project is licensed under the MIT License. See the [MIT License](https://github.com/eljaaarezeah/nik-information-decoder/blob/9f829b621b8e0127326857470bca5fab152d8d92/LICENSE) file for details.