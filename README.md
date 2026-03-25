# concertscrapper
A Python-based command-line tool to discover upcoming concerts using the Ticketmaster Discovery API.

---

## Prerequisites

* Python 3.x
* `requests` library

To install the required library, run:
```bash
pip install requests
```

---

## Installation & Setup

1. **Clone the repository** to your local machine.
2. **Obtain an API Key** from the [Ticketmaster Developer Portal](https://developer.ticketmaster.com/).
3. **Configure the script**: Open `concerts.py` and replace `"your_api"` with your actual Ticketmaster API key.

---

## Usage

Run the script from your terminal:

```bash
python concerts.py
```

1. Enter the **City** when prompted (e.g., London).
2. Enter the **Genre** when prompted (e.g., Rock).
3. The script will display a list of unique upcoming events including dates and venues.

---

## Technical Details

* **Duplicate Prevention**: The script filters the results to ensure each artist/event name is only displayed once per search.
* **Data Source**: Live data fetched via Ticketmaster Discovery API v2.

---

## License
This project is open-source and available under the MIT License.
