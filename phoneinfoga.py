import requests

# User inputs API keys
NUMVERIFY_API_KEY = input("Enter your NumVerify API Key: ")
OPENCAGE_API_KEY = input("Enter your OpenCage Geocoder API Key: ")

def get_number_info(phone_number):
    """Fetches phone number details from NumVerify API"""
    try:
        url = f"http://apilayer.net/api/validate?access_key={NUMVERIFY_API_KEY}&number={phone_number}"
        response = requests.get(url).json()
        
        if response.get("valid"):
            return {
                "Number": response["international_format"],
                "Country": response["country_name"],
                "Location": response["location"],
                "Carrier": response["carrier"],
                "Line Type": response["line_type"]
            }
        else:
            return {"Error": "Invalid phone number"}
    except Exception as e:
        return {"Error": f"NumVerify API failed: {e}"}

def get_location_coordinates(location):
    """Gets latitude & longitude using OpenCage Geocoder"""
    try:
        url = f"https://api.opencagedata.com/geocode/v1/json?q={location}&key={OPENCAGE_API_KEY}"
        response = requests.get(url).json()
        
        if response["results"]:
            coords = response["results"][0]["geometry"]
            return {"Latitude": coords["lat"], "Longitude": coords["lng"]}
        else:
            return {"Error": "Location not found"}
    except Exception as e:
        return {"Error": f"OpenCage API failed: {e}"}

def get_ip_geolocation():
    """Gets real-time IP-based geolocation"""
    try:
        response = requests.get("https://ipinfo.io/json").json()
        return {
            "IP": response.get("ip"),
            "City": response.get("city"),
            "Region": response.get("region"),
            "Country": response.get("country"),
            "Coordinates": response.get("loc")
        }
    except Exception as e:
        return {"Error": f"IP Geolocation API failed: {e}"}

def scan_phone_number(phone_number):
    """Runs a full scan for the given phone number"""
    print(f"\n[+] Scanning phone number: {phone_number}")
    
    # Get number details
    number_info = get_number_info(phone_number)
    if "Error" not in number_info:
        print(f"Country: {number_info['Country']}")
        print(f"Location: {number_info['Location']}")
        print(f"Carrier: {number_info['Carrier']}")
        print(f"Line Type: {number_info['Line Type']}")

        # Get real-time location coordinates
        location_data = get_location_coordinates(number_info["Location"])
        if "Error" not in location_data:
            print(f"Coordinates: {location_data['Latitude']}, {location_data['Longitude']}")
        else:
            print(location_data["Error"])
    else:
        print(number_info["Error"])

    # Get real-time IP-based geolocation
    print("\n[+] Checking IP-based Geolocation...")
    ip_location = get_ip_geolocation()
    if "Error" not in ip_location:
        print(f"IP: {ip_location['IP']}")
        print(f"Location: {ip_location['City']}, {ip_location['Region']}, {ip_location['Country']}")
        print(f"Coordinates: {ip_location['Coordinates']}")
    else:
        print(ip_location["Error"])

# User input
phone_number = input("\nEnter the phone number (with country code): ")
scan_phone_number(phone_number)
