from brave_search import search_brave

def perform_search(subtopics: list) -> list:
    all_links = []

    for subtopic in subtopics:
        print(f"Searching for: {subtopic}")
        links = search_brave(subtopic)
        all_links.extend(links)

    unique_links = list(set(all_links))

    return unique_links