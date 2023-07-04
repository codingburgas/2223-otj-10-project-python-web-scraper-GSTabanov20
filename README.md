## Cryptocurrency Data Display

This Python script fetches data from the CoinMarketCap website and displays information about popular cryptocurrencies, trending cryptocurrencies, top gainers, and top losers. The data is scraped using the `requests` library and parsed using the `BeautifulSoup` library.

## Installation

To run this script, you need to have Python installed on your system.

### Dependencies

The following libraries are required to run the script:

- `requests`: Used to send HTTP requests and fetch the webpage content.
- `beautifulsoup4`: Used to parse the HTML content and extract data from it.

You can install these libraries using the following command:

pip install requests beautifulsoup4

Make sure you have pip installed and it is up to date. If you don't have pip installed, you can refer to the official Python documentation for instructions on how to install it.

## Usage

Once you have installed the required libraries, you can run the script by executing the following command:

```python
python main.py
```
The script will fetch the data from the CoinMarketCap website and display a menu with the following options:

1. Popular Cryptocurrencies
2. Trending Cryptocurrencies (currently under development)
3. Top Gainers (currently under development)
4. Top Losers (currently under development)

To select an option, enter the corresponding number and press Enter.

Option 1 will display information about popular cryptocurrencies, including their names, prices, and 24-hour trading volumes. After displaying the information, you will be prompted with two options: to go back to the menu or exit the script.
Options 2, 3, and 4 are currently under development and will display a message indicating that. You will be presented with the same options to go back to the menu or exit the script.
If you enter an invalid choice, an error message will be displayed, and you will be prompted to enter a valid choice.

## Disclaimer
This script fetches data from the CoinMarketCap website, which is a third-party platform. The availability and accuracy of the data depend on the CoinMarketCap website's stability and functionality. OpenAI and the author of this script do not guarantee the availability or accuracy of the data displayed by the script.

Please use this script responsibly and adhere to any applicable terms of service or usage guidelines provided by CoinMarketCap.

## Contributions
Contributions to this script are welcome. If you have any suggestions or improvements, feel free to fork the script's repository and submit a pull request with your changes.
