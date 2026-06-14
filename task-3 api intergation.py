import requests

try:
    # Fetch data from a free API
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)

    # Check API status
    response.raise_for_status()

    # Convert JSON response to Python objects
    users = response.json()

    print("=== User List ===")

    # Filtering/Search Logic
    search_city = "Gwenborough"

    for user in users:
        if user["address"]["city"] == search_city:
            print(f"Name: {user['name']}")
            print(f"Email: {user['email']}")
            print(f"City: {user['address']['city']}")
            print("-" * 30)

except requests.exceptions.HTTPError as err:
    print("HTTP Error:", err)

except requests.exceptions.ConnectionError:
    print("Connection Error. Check Internet.")

except requests.exceptions.Timeout:
    print("Request Timed Out.")

except requests.exceptions.RequestException as err:
    print("Error:", err)
