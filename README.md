# London Transport Status Tracker

Welcome to the London Transport Status Tracker project! This Python script fetches the current status of London transport lines using the TfL (Transport for London) API and logs the data into a Google Sheets document.

## Project Overview

This project allows users to track the status of various London transport lines, including tube lines, using real-time data provided by the TfL API. The script updates a Google Sheets document with information about line names, status descriptions, and any additional reasons for disruptions.

## Features

- **Real-Time Data Fetching**: Fetches the current status of London transport lines using the TfL API.
- **Google Sheets Integration**: Logs the fetched data into a Google Sheets document, enabling users to monitor transport line statuses over time.
- **Scheduled Data Updates**: Automatically updates the Google Sheets document with new transport line status information at regular intervals.

## How to Use

1. **Install Dependencies**: Ensure that you have installed the required Python libraries (`requests`, `google-auth`, `google-api-python-client`, `schedule`) using `pip install -r requirements.txt`.
   
2. **Obtain API Key**: You need to obtain an API key from TfL to access their API. Replace `'YOUR_TFL_API_KEY'` in the script with your actual API key.
   
3. **Set Up Google Sheets API**: Due to security concerns, Google Sheets API credentials (JSON key file) are not included in this repository. You can obtain and configure your own credentials following the instructions provided by Google.
   
4. **Run the Script**: Execute the `transport_status_tracker.py` script to start fetching and logging London transport line statuses to the specified Google Sheets document.
   
5. **Access the Google Sheets Document**: View the logged London transport line status data in the [Google Sheets document](https://docs.google.com/spreadsheets/d/1K9oFR8QaEm-eP0upgRl4BYr_f1_PlC2UQvt1RW6yTA4/edit#gid=0).

## Note

- **Google Credentials**: This repository does not include Google Sheets API credentials (`creds.json`) due to security reasons. You will need to obtain and configure your own credentials to use the Google Sheets API.
