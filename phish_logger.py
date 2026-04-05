from datetime import datetime
import csv

LOG_FILE = "captured_credentials.csv"

def log_credentials(username, password):
    with open(LOG_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), username, password])

def main():
    username = input("Enter username: ")
    password = input("Enter password: ")

    log_credentials(username, password)
    print("Saved to CSV.")

if __name__ == "__main__":
    main()
