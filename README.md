# concertscrapper
A command-line utility for Python that uses the Ticketmaster Discovery API to find upcoming shows.
## Before you start
You need:
* Python 3.x
* The library "requests"

You can grab the library with:
```pip install requests```

---

## Setup & Installation

1. Make a local copy of the repository.
2. Visit the [Ticketmaster Developer Portal](https://developer.ticketmaster.com/) to obtain an API key.
3. To configure the script, open `concerts.py` and use your real Ticketmaster API key in place of `API_KEY`.

---

## How to use it

Use your terminal to run the script:
```python concerts.py```

## The script will ask you for:
1. **City** (e.g., London, Berlin, New York)
2. **Genre** (e.g., Rock, Metal, Pop)

It’ll then list out unique upcoming events, dates, and venues. I added a small filter so you won't see the same show twice if they have multiple ticket types.

---



