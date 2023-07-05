import os
import requests
from bs4 import BeautifulSoup

# Display menu
def display_menu():
    # Print the menu options
    print('╔══════════════════════════════════════╗')
    print('║                 Menu                 ║')
    print('╠══════════════════════════════════════╣')
    print('║ 1. Popular Cryptocurrencies          ║')
    print('║ 2. Trending Cryptocurrencies         ║')
    print('║ 3. Top Gainers                       ║')
    print('║ 4. Top Losers                        ║')
    print('║ 5. Exit                              ║')
    print('╚══════════════════════════════════════╝')
    choice = input('Enter your choice: ')
    print()
    
    if choice == '1':
        # Print popular cryptocurrencies with their prices and volumes
        for i in range(0, 10):
            print(f'{cryptocurrency_names[i]} #{i + 1}')
            print(f'Price: {prices[i]}')
            print(f'Volume (24h): {volumes[i]}')
            print('---------------------------')
        print()
            
        print('1. Go back to menu')
        print('2. Exit')
        choice = input('Enter your choice: ')
        print()
        
        if choice == '1':
            os.system('cls')
            display_menu()
        elif choice == '2':
            exit()
        else:
            os.system('cls')
            print('Invalid choice.')
            print()
            display_menu()

    elif choice == '2':
        # Inform the user that this option is under development
        print('This option is currently under development. Please check back later.')
        print('1. Go back to menu')
        print('2. Exit')
        choice = input('Enter your choice: ')
        print()

        if choice == '1':
            os.system('cls')
            display_menu()
        elif choice == '2':
            exit()
        else:
            os.system('cls')
            print('Invalid choice.')
            print()
            display_menu()
    elif choice == '3':
        # Inform the user that this option is under development
        print('This option is currently under development. Please check back later.')
        print('1. Go back to menu')
        print('2. Exit')
        choice = input('Enter your choice: ')
        print()
        
        if choice == '1':
            os.system('cls')
            display_menu()
        elif choice == '2':
            exit()
        else:
            os.system('cls')
            print('Invalid choice.')
            print()
            display_menu()
    elif choice == '4':
        # Inform the user that this option is under development
        print('This option is currently under development. Please check back later.')
        print('1. Go back to menu')
        print('2. Exit')
        choice = input('Enter your choice: ')
        print()

        if choice == '1':
            os.system('cls')
            display_menu()
        elif choice == '2':
            exit()
        else:
            os.system('cls')
            print('Invalid choice. Please try again.')
            print()
            display_menu()
    elif choice == '5':
        # Exit the program
        exit()
    else:
        # Handle invalid choice
        os.system('cls')
        print('Invalid choice.')
        print()
        display_menu()

# Perform web scraping
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
