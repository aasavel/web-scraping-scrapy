# Web Scraping Demo with Scrapy


This repository contains Python script to scrape a webpage (scrapethissite.com) that loads its data via AJAX using Scrapy. The scraper extracts film information (year, title, nominations, awards) for the years 2010 - 2015.


## Target website:

📌 https://www.scrapethissite.com/pages/ajax-javascript/


## Project Structure
```
web-scraping-scrapy/
│ .gitignore
│ README.me
│ pyproject.toml
└── scrapytutorial/
    ├── scrapy.cfg
    └── scrapytutorial/
        ├── __init__.py 
        ├── items.py
        ├── middlewares.py             
        ├── pipelines.py      
        ├── settings.py       
        └── spiders/
            ├── __init__.py 
            ├── filmscraper.py 
            ├── films.json
            └── films.xlsx 
```

## Installation
1. **Install dependencies**: 
   ```
   poetry install
   ```
2. **Run Scrapy through Poetry**: 
   ```
   poetry run scrapy
   ```
3. **Running the Spider**: 
   ```
   cd scrapytutorial/scrapytutorial/spiders
   poetry run scrapy runspider filmscraper.py
   ```

The output is automatically saved to:
- `films.json`
- `films.xlsx` 

## How the Spider Works
The spider iterates from **2010 to 2015**, requesting each year’s JSON endpoint and extracting:

- Year
- Title
- Number of Nominations
- Number of Awards

## Create your own Scrapy project 
1. Create your project using the command: 
   ```
   scrapy startproject scrapytutorial
   ```
2. This generates several folders:
   - **spiders** (empty for now)
   - **items**, **middlewares**, **pipelines** (optional)
   - **settings** (important for configuration)


## Create a spider
1. Use the command:
   ```
   scrapy genspider filmspider https://www.scrapethissite.com/pages/ajax-javascript/
   ```
   This generates a spider named `filmspider` to scrape this website.

## Use iPython with Scrapy
1. Run iPython through Poetry: 
   ```
    poetry run ipython
   ```
2. Add this line in `scrapy.cfg`:
   ```
   shell = ipython
   ```
3. Launch the shell in the terminal:
   ```
   scrapy shell
   ```