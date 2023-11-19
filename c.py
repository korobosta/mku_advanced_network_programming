import requests

# API endpoint URL
api_url = 'https://jsonplaceholder.typicode.com/posts/1'

# Making a GET request to the API endpoint
response = requests.get(api_url)

# Checking if the request was successful (status code 200)
if response.status_code == 200:
    # Accessing JSON data from the response
    json_data = response.json()
    print("Received JSON data:")
    print(json_data)
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")