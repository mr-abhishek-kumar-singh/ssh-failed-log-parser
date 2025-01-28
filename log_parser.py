import re

def parse_logs(file_path):
    """
    Parses the log file to extract failed SSH password attempts.

    Args:
        file_path (str): Path to the log file.
    """
    try:
        with open(file_path, 'r') as file:
            logs = file.readlines()
        
        failed_attempts = []
        for log in logs:
            if "Failed password" in log:
                failed_attempts.append(log.strip())
        
        print("Failed SSH password attempts:")
        for attempt in failed_attempts:
            print(attempt)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist. Please provide a valid file path.")

# Get user input for log file path
log_file = input("Enter the path to the log file (e.g., auth.log): ")
parse_logs(log_file)
