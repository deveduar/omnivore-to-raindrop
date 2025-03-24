---
title: "Omnivore JSON to Raindrop.io CSV Converter"
description: "A Python script to convert Omnivore JSON exports to CSV format for easy migration to Raindrop.io."
imageSrc: "https://i.postimg.cc/HLT5MH2H/artem-sapegin-b18-TRXc8-UPQ-unsplash.jpg"
detailedDescription: "This Python script helps users convert JSON files exported from Omnivore into CSV format, making them compatible with Raindrop.io. It allows easy migration of data as Omnivore is scheduled to shut down."
technologies:
  - "Python"
  - "Scripting"
  - "Automation"
  - "Data Conversion"
links:
  - href: "https://github.com/deveduar/omnivore-to-raindrop"
    label: "GitHub"
features:
  - "Converts Omnivore JSON exports to CSV format."
  - "Supports UTF-8 encoding for correct display of text data."
  - "Batch processing of multiple JSON files based on filename pattern."
  - "Generates CSV file compatible with Raindrop.io for easy import."

---

# Omnivore JSON to Raindrop.io CSV Converter

This is a command-line Python script for converting JSON files exported from [Omnivore](https://docs.omnivore.app/using/exporting.html) to CSV format, making them compatible with [Raindrop.io](https://raindrop.io/). Omnivore is scheduled to shut down soon, so this tool helps users easily migrate their data.

## Prerequisites

- **Python 3**: Ensure that you have Python 3 installed. You can check your Python version by running:

  ```bash
  python3 --version
  ```

## Features

- Converts Omnivore JSON exports to a CSV file.
- Compatible with UTF-8 encoding, so text data displays correctly.
- Processes multiple JSON files based on a filename pattern, allowing batch conversion.

## Installation

1. Clone this repository or download the `convert.py` script.
2. Place the script in a directory where your exported JSON files from Omnivore are located.

## Usage

1. Open a terminal and navigate to the directory containing the script and your Omnivore JSON files.
2. Run the script with the following command:

   ```bash
   python3 convert.py "metadata_*.json"
   ```
   Replace `metadata_*.json` with the actual pattern matching your JSON files if needed.

### Output

- The script will generate a CSV file named `metadata.csv` in the same directory.
- This file can be imported into Raindrop.io or other applications that accept CSV imports.

## CSV Structure

The output CSV file includes the following columns:

| Column    | Description                       |
|-----------|-----------------------------------|
| url       | The URL associated with the item  |
| title     | The title of the item             |
| tags      | Comma-separated tags              |
| note      | Notes or description              |
| created   | The creation date of the item     |

## Example

Here’s how to use the script for multiple JSON files matching the pattern `metadata_*.json`:

```bash
python3 convert.py "metadata_*.json"
```

Upon successful completion, you should see a message indicating the total number of records processed and that `metadata.csv` has been created.

## Error Handling

- If a JSON file cannot be processed (for example, if it is corrupted), an error message will be displayed, and the script will continue processing the remaining files.

## Notes

- Ensure that all Omnivore export files are saved in UTF-8 format to avoid encoding issues.
- Open `metadata.csv` with a UTF-8 compatible editor, such as Excel or LibreOffice, to ensure proper display of special characters.

