import subprocess
import os

# Define the source directory and destination
source_directory = '/home/mohammad/Desktop/New_Python_Project/'
destination = os.path.expanduser('/home/mohammad/Desktop/final')

# Use subprocess to execute the cp command
try:
    subprocess.run(['cp', '-r', source_directory, destination], check=True)
    print("Directory copied successfully.")
except subprocess.CalledProcessError as e:
    print(f"An error occurred: {e}")
    
