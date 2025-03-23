# Phoneinfoga

# Overview
The "phoneinfogath.py" script is designed to gather and display information about a phone number, including its validity, geographical location, and carrier details. It utilizes two external APIs: NumVerify for phone number validation and OpenCage for geolocation based on the location name. Additionally, it retrieves the user's current IP-based geolocation.

# Key Features:

1. User Input for API Keys:
        The script prompts the user to input their NumVerify and OpenCage API keys for authentication.

2. Phone Number Validation:
        The get_number_info function checks if the provided phone number is valid using the NumVerify API.
        If valid, it returns details such as:
            International format of the number
            Country name
            Location
            Carrier
            Line type

3. Geolocation Retrieval:
        The get_location_coordinates function fetches latitude and longitude for the location associated with the phone number using the OpenCage API.
        It returns coordinates if the location is found.

4. IP Geolocation:
        The get_ip_geolocation function retrieves the user's current IP address and its associated geographical information using the IPinfo API.

5. Full Scan Functionality:
        The scan_phone_number function orchestrates the entire process:
            It scans the phone number and prints relevant details.
            It checks for real-time location coordinates.
            It retrieves and displays the user's IP-based geolocation.

6. Error Handling:

    The script includes error handling to manage API failures and invalid inputs, providing user-friendly error messages.

# Example Output:

  The script outputs detailed information about the phone number and the user's IP location. If an error occurs, it provides a clear message indicating the issue.

  Successful Scenario:
          
          Enter your NumVerify API Key: your_numverify_api_key
          Enter your OpenCage Geocoder API Key: your_opencage_api_key


          Enter the phone number (with country code): +14155552671


          [+] Scanning phone number: +14155552671

          Country: United States
          Location: California
          Carrier: Verizon Wireless
          Line Type: Mobile
          Coordinates: 36.7783, -119.4179


          [+] Checking IP-based Geolocation...

          IP: 192.0.2.1
          Location: San Francisco, California, US
          Coordinates: 37.7749, -122.4194
          
# Note:

  The script may fail if the API keys are invalid or if there are issues with the API services, as indicated by the error message received during execution. For example, an error response might look like this:
  

# Step-by-Step Guide to Download and Run phoneinfogath.py:
Step 1: Install Git

Windows:
    Download the Git installer from the official Git website.
    Run the installer and follow the prompts to complete the installation.

  
      
macOS:
        You can install Git using Homebrew. If you don't have Homebrew, install it from brew.sh.
        Open Terminal and run:

       

    brew install git
   

Linux:

  Most Linux distributions come with Git pre-installed. You can check by running:

 

    git --version

If it's not installed, you can install it using your package manager. For example, on Ubuntu:
   
    sudo apt update
    sudo apt install git

Step 2: Clone the Repository

  Open your command line interface (Command Prompt on Windows, Terminal on macOS/Linux).
  Navigate to the directory where you want to clone the repository. You can use the cd command. For example:

  
      cd path/to/directory

Clone the repository containing the phoneinfogath.py script. 


      git clone https://github.com/Lutkinxp/phoneinfogath.git

Navigate into the cloned repository:



      cd repository

Step 3: Install Required Libraries

The script uses the requests library to make API calls. You can install it using pip.

  Run the following command:

   

     pip install requests

Step 4: Run the Script

  In the command line, ensure you are still in the directory where phoneinfogath.py is located.
  Run the script using Python:

   

    python phoneinfogath.py

or, if you are using Python 3:

bash

    python3 phoneinfogath.py

Step 5: Input API Keys and Phone Number

    When prompted, enter your NumVerify API key and OpenCage API key.
    Enter the phone number you want to scan, including the country code (e.g., +14155552671).

Additional Notes

    API Keys: Make sure you have valid API keys for NumVerify and OpenCage. You can sign up for free accounts on their respective websites to obtain these keys.
    Internet Connection: Ensure you have an active internet connection, as the script makes API calls to external services.
    Error Handling: If you encounter any errors, check the error messages for guidance on what went wrong (e.g., invalid API keys, network issues).

