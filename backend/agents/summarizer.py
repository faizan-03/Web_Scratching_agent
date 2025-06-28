from gemini_client import summarize_with_gemini 

def summarize_content(scraped_data: dict) -> dict:
    summarized = {}

    for section, raw_text in scraped_data.items():
        print(f"Summarizing section: {section}")

        prompt = (
            f"You are an academic researcher. Summarize the following content into a formal, "
            f"well-structured explanation suitable for a thesis report section titled '{section}':\n\n{raw_text}"
        )

        summary = summarize_with_gemini(prompt)
        summarized[section] = summary.strip()

    return summarized
