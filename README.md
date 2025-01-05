# Myntra Scraper

This is a web scraper designed to extract product data from Myntra, a popular online fashion and lifestyle store. It collects detailed product information like product name, price, brand, description, ratings, and other relevant details from Myntra’s product pages.

## Prerequisites

Before using this scraper, ensure you have the following installed on your system:

- Python 3.8 or higher
- pip (Python package installer)
- Required libraries in requirement.txt

To install these libraries, run the following:

```bash
pip install -r requirement.txt
```

## Installation

1. Clone or download the scraper repository:

```bash
git clone https://github.com/your-username/myntra-scraper.git
```

2. Navigate to the scraper directory:

```bash
cd myntra-scraper
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. (Optional) Set up a virtual environment for a cleaner setup:
```bash
conda create -p ./venv python=3.10 -y
source conda activate ./venv
```

## Usage

To scrape Myntra product data, follow these steps:

1. **Run the scraper**:
    - Navigate to the directory where the script is located.
    - Run the following command:

    ```bash
    python scraper.py
    ```

    This will start the scraper, and it will fetch product data from the provided URL(s).

2. **Command Line Arguments**:
    You can provide a Myntra product URL to scrape a specific product or pass a list of URLs to scrape multiple products. For example:

    ```bash
    python scraper.py --url "https://www.myntra.com/shirts"
    ```

3. **Save Scraped Data**:
    By default, the data will be saved in a CSV file (`output.csv`). You can specify the filename using the `--output` argument.

    ```bash
    python scraper.py --url "https://www.myntra.com/shirts" --output "shirts_data.csv"
    ```

