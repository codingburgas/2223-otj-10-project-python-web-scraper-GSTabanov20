import requests
from bs4 import BeautifulSoup

# Display menu
def display_menu():
    print("Menu:")
    print("1. Popular Cryptocurrencies")
    print("2. Trending Cryptocurrencies")
    choice = input("Enter your choice: ")
    print()
    
    if choice == "1":
        for i in range(0, 10):
            print(f'Cryptocurrency name: {cryptocurrency_names[i]}')
            print(f'Price: {prices[i]}')
            print(f'Volume (24h): {volumes[i]}')
            print()
    elif choice == "2":
        pass
    else:
        print("Invalid choice. Please try again.")
        display_menu()

url = 'https://coinmarketcap.com/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Lists for storing cryptocurrency data
cryptocurrency_names = []
prices = []
volumes = []

# Extract cryptocurrency names
name_elements = soup.find_all('p', class_='sc-4984dd93-0 kKpPOn')
for name_element in name_elements:
    cryptocurrency_names.append(name_element.text)

# Extract cryptocurrency prices
price_elements = soup.find_all('div', class_='sc-bc83b59-0 iVdfNf')
for price_element in price_elements:
    prices.append(price_element.text)

# Extract cryptocurrency volumes
volume_elements = soup.find_all('p', class_='sc-4984dd93-0 jZrMxO font_weight_500')
for volume_element in volume_elements:
    volumes.append(volume_element.text)

# Call the display_menu function
display_menu()