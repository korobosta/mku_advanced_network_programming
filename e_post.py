import requests

# URL to send the POST request
url = 'https://www.mku.ac.ke/'

# Data to be sent in the POST request (in JSON format)
data = {
    'name': 'Student 1',
    'admission_number': 'MIT/2023',
}

# Sending a POST request with the data
response = requests.post(url, json=data)

# Checking if the request was successful (status code 201 - Created)
if response.status_code == 201:
    # Accessing the response content
    created_post = response.json()
    print("Created Student:")
    print(created_post)
else:
    print(f"Failed to create student. Status code: {response.status_code}")
