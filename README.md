# Anime Scraper Project

This project is a Python-based web scraping application designed to scrape anime data from the `samehada` website. It uses the Scrapy framework and incorporates features like auto-rotating proxies and fake user-agent headers to enhance scraping capabilities.

---

## Features
- Scrapes detailed anime information including title, Japanese and English names, status, type, and release date.
- Retrieves a list of episodes with details such as:
  - Episode thumbnails
  - Release dates
  - Streaming links
  - Download links in multiple resolutions (360p, 480p, 720p, 1080p)
- Utilizes proxy rotation and fake user-agent headers to bypass scraping restrictions.

---

## Configuration
### API Keys and Endpoints
To enable proxy rotation and user-agent spoofing, configure the following variables:

```python
# ScrapeOps API key
SCRAPEOPS_API_KEY = 'a497fde8-67fa-47a1-8e95-c15fc53f147e'

# Fake User-Agent Endpoint
SCRAPEOPS_FAKE_USER_AGENT_ENDPOINT = 'https://headers.scrapeops.io/v1/user-agents'

# Proxy Rotation Endpoint
ROTATE_PROXY_ENDPOINT = 'https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies&proxy_format=protocolipport&format=text'

# Enable Fake User-Agent
SCRAPEOPS_FAKE_USER_AGENT_ENABLE = True
```

---

## Sample Scraped Data
The scraper extracts data in JSON format. Below is an example of the output:

```json
[
    {
        "title": "Detail Anime 100-man no Inochi no Ue ni Ore wa Tatteiru 2nd Season",
        "detail": {
            "Japanese": "100\u4e07\u306e\u547d\u306e\u4e0a\u306b\u4ffa\u306f\u7acb\u3063\u3066\u3044\u308b",
            "Synonyms": "I'm standing on 1,000,000 lives. Season 2",
            "English": "I’m Standing on a Million Lives Season 2",
            "Status": "Completed",
            "Type": "TV",
            "Source": "Manga",
            "Duration": "Unknown",
            "Total Episode": "12",
            "Season": "",
            "Studio": "",
            "Producers": "",
            "Released:": "Jul 10, 2021 to Sep 25, 2021"
        }
    },
    {
        "listeps": {
            "100-man no Inochi no Ue ni Ore wa Tatteiru 2nd Season Episode 8": {
                "thumbnail": "https://samehadaku.email/wp-content/uploads/2021/08/100manS2-08-v1.jpg",
                "relesed": "28 August 2021",
                "link_sreaming": "https://samehadaku.email/100-man-no-inochi-no-ue-ni-ore-wa-tatteiru-2nd-season-episode-8/",
                "link_download": {
                    "360p ": {
                        "Zippyshare": "https://www62.zippyshare.com/v/NQ8OJxXC/file.html"
                    },
                    "480p ": {
                        "Zippyshare": "https://www62.zippyshare.com/v/Qj0aMq9b/file.html"
                    },
                    "720p ": {
                        "Zippyshare": "https://www3.zippyshare.com/v/1HOjexJv/file.html"
                    },
                    "1080p ": {
                        "Zippyshare": "https://www66.zippyshare.com/v/imQtWMPk/file.html"
                    }
                }
            }
        }
    }
]
```

---

## How to Run
### Prerequisites
- Python 3.8 or higher
- Scrapy library
- Internet access

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables or update the configuration in the script:
   ```python
   SCRAPEOPS_API_KEY = '<your-api-key>'
   SCRAPEOPS_FAKE_USER_AGENT_ENDPOINT = '<fake-user-agent-endpoint>'
   ROTATE_PROXY_ENDPOINT = '<proxy-rotation-endpoint>'
   SCRAPEOPS_FAKE_USER_AGENT_ENABLE = True
   ```

### Running the Scraper
Run the scraper using the Scrapy CLI:
```bash
scrapy crawl anime_spider
```

---

## Technologies Used
- **Python**: Core programming language.
- **Scrapy**: Web scraping framework.
- **ScrapeOps**: Proxy and user-agent rotation.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for more information.
