import requests

# URL to send the GET request
url = 'https://www.mku.ac.ke/'

# Sending a GET request
response = requests.get(url)

# Checking if the request was successful (status code 200)
if response.status_code == 200:
    # Accessing the response content
    data = response.json()  # Assuming the response contains JSON data
    print("Received data:")
    print(data)
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")