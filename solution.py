import geocoder
import requests



destinations = [
    "Space Needle",
    "Crater Lake",
    "Golden Gate Bridge",
    "Yosemite National Park",
    "Las Vegas, Nevada",
    "Grand Canyon National Park",
    "Aspen, Colorado",
    "Mount Rushmore",
    "Yellowstone National Park",
    "Sandpoint, Idaho",
    "Banff National Park",
    "Capilano Suspension Bridge",
]
API_BASE_URl = "redacted"
for point in destinations:
    g = geocoder.arcgis(point)
    full_api_url = f'{API_BASE_URl}{g.lat},{g.lng}'
    result = requests.request('GET', full_api_url).json()
    currently = result['currently']['summary']
    temperature = result['currently']['summary']
    print(f'{point} is located at {g.latlng} \n The weather is currently {currently} with a temperature of {temperature}')