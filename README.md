# ThccWikiScrapoer
A web scraper designed to migrate pages from THCC's old website



## Dependencies

To run this project, you need to have the following dependencies installed:

- Python 3.x
- `requests`
- `beautifulsoup4`
- `json`

You can install the required Python packages using pip:

```sh
pip install -r requirements.txt
```

## Usage
The main script for this project is main.py. You can run it with different command line flags to perform various actions.

### Command Line Flags
```sh
--wikis: Scrape all wikis listed in Urls/all.json.
```

This will call the wikis function, which iterates over all URLs in Urls/all.json and scrapes each one.

```sh
--wiki <url>: Scrape a single wiki page specified by the URL.
```

This will call the wiki function, which scrapes the specified URL and saves the result in the Wikis directory.

```sh
--links <url>: Scrape all links from the specified URL and save them to Urls/all.json.
```

This will call the links function, which scrapes links from the specified URL and writes them to Urls/all.json.

```sh
--write2db: Write the scraped data to a database.
```

This will call the write2db function, which writes the scraped data to a database.

