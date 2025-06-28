from gemini_client import summarize_with_gemini

def expand_summary(summarized_data: dict) -> dict:
    expanded = {}

    for section, summary in summarized_data.items():
        print(f"Expanding section: {section}")

        prompt = (
            f"You are a thesis assistant. Take the following summary from a research report section titled '{section}' "
            f"and expand it into 2–3 detailed paragraphs. Add real-world examples, statistics, and deeper analysis:\n\n"
            f"{summary}"
        )

        expanded_text = summarize_with_gemini(prompt)
        expanded[section] = expanded_text.strip()

    return expanded
