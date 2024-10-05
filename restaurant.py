# This project would allow you to get the menu of your local restaurants and use OpenAI to get
# the details about the menu items
# or we could also just ask directly what the location signifies

import googlemaps
import requests
#from bs4 import BeautifulSoup
import requests

def get_restaurant_menu(restaurant_name,apikey):
    search_url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={restaurant_name}&inputtype=textquery&fields=place_id&key={apikey}"
    search_response = requests.get(search_url)
    search_data = search_response.json()

    if 'candidates' in search_data and search_data['candidates']:
        place_id = search_data['candidates'][0]['place_id']

        # Step 2: Get place details, including the website
        details_url = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&fields=name,website&key={apikey}"
        details_response = requests.get(details_url)
        details_data = details_response.json()

        website = details_data['result'].get('website')

        if website:
            print(f"Menu URL: {website}")
        else:
            print("No website found for this restaurant.")
    else:
        print("Restaurant not found.")


# Example usage:
API_KEY = 'AIzaSyDptT4XC42oYL6D5VQYZfpa6EDVwDF6RlE'
# Input restaurant name here, possible to automate later

restaurant_name = "Via Locusta"
get_restaurant_menu(restaurant_name, API_KEY)

