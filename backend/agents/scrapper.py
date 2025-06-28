import requests
from bs4 import BeautifulSoup

def scrape_content(categorized_links: dict, min_words=1000, max_urls_per_section=5) -> dict:
    scraped_data = {}

    for section, urls in categorized_links.items():
        combined_text = ""
        total_words = 0
        url_count = 0

        for url in urls:
            if url_count >= max_urls_per_section:
                break

            try:
                print(f"Scraping: {url}")
                response = requests.get(url, timeout=10)
                soup = BeautifulSoup(response.text, "html.parser")

                for tag in soup(["script", "style", "nav", "footer", "header", "aside"]):
                    tag.decompose()

                paragraphs = soup.find_all("p")
                text = "\n".join([p.get_text() for p in paragraphs if len(p.get_text()) > 60])

                if len(text) > 500:
                    combined_text += text + "\n\n"
                    total_words += len(text.split())
                    url_count += 1

                if total_words >= min_words:
                    break

            except Exception as e:
                print(f"Error scraping {url}: {e}")
                continue

        if total_words >= min_words:
            scraped_data[section] = combined_text.strip()
        else:
            print(f"Skipping section '{section}' due to insufficient content ({total_words} words)")

    return scraped_data
