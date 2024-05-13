import datetime
import requests
import schedule
import time
from google.oauth2 import service_account
from googleapiclient.discovery import build

# This function sets up the connection to Google Sheets using OAuth credentials
def authenticate_google_sheets():
    SERVICE_ACCOUNT_FILE = 'creds.json'  # File that stores authentication credentials
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']  # Specifies Google Sheets API scope
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('sheets', 'v4', credentials=credentials)
    return service

# Fetches the current status of London transport lines using the TfL API
def get_tfl_status(api_key):
    try:
        url = f'https://api.tfl.gov.uk/line/mode/tube/status?app_key={api_key}'  # API endpoint with API key
        response = requests.get(url)
        response.raise_for_status()  # Checks if the API request was successful
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data from TfL API: {e}")  # Prints out the error if the API call fails
        return None

# Updates the Google Sheet with the data fetched from the TfL API
def update_sheet(service, data, sheet_id):
    if data is None:
        print("No data to update.")  # Checks if there is data to update
        return
    try:
        values = [
            [datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 
             line['name'], 
             line['lineStatuses'][0]['statusSeverityDescription'], 
             line['lineStatuses'][0].get('reason', 'No additional info')]  # Prepares data for the sheet
            for line in data
        ]
        body = {'values': values}
        range_name = 'Sheet1!A:D'  # Specifies the range in the sheet where data will be written
        service.spreadsheets().values().append(
            spreadsheetId=sheet_id,
            range=range_name,
            valueInputOption='USER_ENTERED',
            body=body,
            insertDataOption='INSERT_ROWS'
        ).execute()
        print(f"Update completed at {datetime.datetime.now()}")  # Confirmation that the sheet was updated
    except Exception as e:
        print(f"Error updating Google Sheet: {e}")  # Catches any errors during the update process

# Scheduled job that runs the update process
def job():
    service = authenticate_google_sheets()
    sheet_id = '1K9oFR8QaEm-eP0upgRl4BYr_f1_PlC2UQvt1RW6yTA4'
    api_key = '318631baf6364851886c6aa03b22c2e4'
    tfl_data = get_tfl_status(api_key)
    update_sheet(service, tfl_data, sheet_id)

# Main function that schedules the job to run every minute
def main():
    schedule.every(1).minutes.do(job)  # Schedules the job to run every minute

    while True:
        schedule.run_pending()  # Keeps running the scheduled jobs
        time.sleep(1)  # Waits for 1 second before checking again

if __name__ == '__main__':
    main()
