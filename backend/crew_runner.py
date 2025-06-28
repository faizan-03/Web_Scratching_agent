from agents.query_analyzer import analyze_query
from agents.searcher import perform_search
from agents.classifier import classify_links
from agents.scrapper import scrape_content
from agents.reporter import generate_report

def run_research_pipeline(topic: str) -> str:
    try:
        print(f"\nStarting research pipeline for topic: '{topic}'\n")

        subtopics = analyze_query(topic)
        print(f"Subtopics identified:\n{subtopics}\n")

        search_results = perform_search(subtopics)
        print(f"Found {len(search_results)} total relevant links.\n")

        categorized_links = classify_links(search_results)
        print(f"Categorized into: {list(categorized_links.keys())}\n")

        scraped_content = scrape_content(categorized_links)
        print(f"Scraped content from {len(scraped_content)} pages.\n")

        report_sections = {}

        for subtopic in subtopics:
            normalized_key = subtopic.lower().strip()
            matched_section = next((k for k in scraped_content if k.lower() in normalized_key), None)

            content = scraped_content.get(matched_section) if matched_section else None

            if content and len(content.strip()) > 50:
                print(f"Using scraped content for: {subtopic}")
                print(f"Content Preview for '{subtopic}':\n{content[:300]}...\n")
                report_sections[subtopic] = content
            else:
                print(f"Skipping {subtopic} due to insufficient scraped content.\n")

        if not report_sections:
            print("No valid content available. Report will not be generated.")
            return ""

        print(f"\nFinalized {len(report_sections)} sections from scraped data.\n")

        full_report = generate_report(report_sections)

        print("\n===== FINAL REPORT PREVIEW (First 500 Chars) =====")
        print(full_report[:500] + "\n...")
        print("===== END OF PREVIEW =====\n")

        return full_report

    except Exception as e:
        print(f"Error during research pipeline: {e}")
        return ""
