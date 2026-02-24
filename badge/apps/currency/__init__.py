from badgeware import io, brushes, shapes, screen, PixelFont, run, Matrix
from urllib.request import urlopen, Request
import json
import gc

# Fonts
small_font = PixelFont.load("/system/assets/fonts/ark.ppf")
large_font = PixelFont.load("/system/assets/fonts/absolute.ppf")

# Colors
white = brushes.color(235, 245, 255)
background = brushes.color(13, 17, 23)
gray = brushes.color(100, 110, 120)

# Define GitHub-themed colors
github_blue = brushes.color(36, 41, 46)
github_dark_gray = brushes.color(22, 27, 34)
github_light_gray = brushes.color(88, 96, 105)
github_green = brushes.color(46, 160, 67)

# State
exchange_data = {}
loading = False
last_update = None

# Constants
API_URL = "https://api.frankfurter.dev/v1/latest?base=GBP&symbols=INR,USD,CAD,CHF"
CURRENCIES = ["GBP", "INR", "USD", "CAD", "CHF"]
REFRESH_INTERVAL = 60  # seconds
API_KEY = "YOUR_ACCESS_KEY"

# Add state to track the current base currency
current_base_index = 0

def fetch_exchange_rates():
    """Fetch exchange rates for the current base currency."""
    global exchange_data, loading, last_update
    loading = True
    try:
        base_currency = CURRENCIES[current_base_index]
        symbols = ",".join([c for c in CURRENCIES if c != base_currency])
        api_url = f"https://api.frankfurter.dev/v1/latest?base={base_currency}&symbols={symbols}"

        # Add User-Agent header to the request
        request = Request(api_url, headers={"User-Agent": "GitHub-Universe-Badge/1.0"})
        response = urlopen(request)
        raw_data = response.read().decode('utf-8')  # Read and decode response
        print("Raw API Response:", raw_data)  # Debugging log

        # Parse JSON safely
        data = json.loads(raw_data)
        if 'rates' in data:
            rates = data['rates']
            exchange_data = {currency: rates.get(currency, 1.0 if currency == base_currency else None) for currency in CURRENCIES}
            print("Parsed Exchange Data:", exchange_data)  # Debugging log
        else:
            print("Error: 'rates' field not found in API response.")
            exchange_data = {}

        last_update = io.ticks
    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {e}")
        exchange_data = {}
    except Exception as e:
        print(f"Error fetching exchange rates: {e}")
        exchange_data = {}
    finally:
        loading = False
        gc.collect()

def draw_exchange_rates():
    """Draw the exchange rates on the screen with GitHub-themed UI and subtle background effects."""
    # Background with subtle gradient effect
    for y in range(0, 120, 2):
        gradient_color = brushes.color(22 + y // 6, 27 + y // 6, 34 + y // 6)
        screen.brush = gradient_color
        screen.draw(shapes.rectangle(0, y, 160, 2))

    # Header
    screen.font = large_font
    screen.brush = github_blue
    screen.draw(shapes.rectangle(0, 0, 160, 20))
    screen.brush = white
    base_currency = CURRENCIES[current_base_index]
    screen.text(f"1 {base_currency} in Others", 5, 3)

    # Content with subtle shadow effect
    screen.font = small_font
    y = 30
    for currency, rate in exchange_data.items():
        if rate is not None:
            screen.brush = github_light_gray
            screen.text(f"{currency}: {rate:.2f}", 6, y + 1)  # Shadow
            screen.brush = github_green
            screen.text(f"{currency}: {rate:.2f}", 5, y)
        else:
            screen.brush = github_light_gray
            screen.text(f"{currency}: Error", 6, y + 1)  # Shadow
            screen.brush = github_light_gray
            screen.text(f"{currency}: Error", 5, y)
        y += 15

    # Footer
    if last_update:
        elapsed = (io.ticks - last_update) / 1000
        if elapsed < REFRESH_INTERVAL:
            screen.brush = github_light_gray
            screen.text(f"Refresh in: {int(REFRESH_INTERVAL - elapsed)}s", 5, 110)

def update():
    """Update function called every frame."""
    global current_base_index

    # Check for button press to change base currency
    if io.BUTTON_A in io.pressed:
        current_base_index = (current_base_index + 1) % len(CURRENCIES)
        fetch_exchange_rates()

    if not loading and (last_update is None or (io.ticks - last_update) / 1000 >= REFRESH_INTERVAL):
        fetch_exchange_rates()
    draw_exchange_rates()

def init():
    """Initialize the app."""
    fetch_exchange_rates()

def on_exit():
    """Cleanup when exiting the app."""
    gc.collect()

# Run the app
run(update)