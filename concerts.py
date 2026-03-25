import requests

API_KEY = "your_api"

def get_concerts(city, genre):
    url = "https://app.ticketmaster.com/discovery/v2/events.json"
    
    params = {
        "apikey": API_KEY,
        "city": city,
        "classificationName": genre,
        "locale": "en",
        "size": 20
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    if "_embedded" not in data:
        print("No concerts found.")
        return
    
    events = data["_embedded"]["events"]
    
    print(f"\n🎵 Concerts in {city} — {genre}")
    print("─" * 40)
    
    seen_artists = []

    for event in events:
        name = event["name"]
        
        if name in seen_artists:
            continue
        seen_artists.append(name)
        
        date = event["dates"]["start"]["localDate"]
        venue = event.get("_embedded", {}).get("venues", [{}])[0].get("name", "Unknown venue")
        print(f"\n🎤 {name}")
        print(f"   📅 {date}")
        print(f"   📍 {venue}")

city = input("Enter city: ")
genre = input("Enter genre: ")
get_concerts(city, genre)