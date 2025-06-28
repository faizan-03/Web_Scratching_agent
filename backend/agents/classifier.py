def classify_links(links: list) -> dict:
    sections = {
        "Introduction": [],
        "History": [],
        "Trends": [],
        "Challenges": [],
        "Solutions": [],
        "Applications": [],
        "Benefits": [],
        "Drawbacks": [],
        "Comparison": [],
        "Future Trends": [],
        "Key Players": [],
        "Regulations": [],
        "Ethics": [],
        "Societal Impact": [],
        "Technological Impact": [],
        "Case Studies": [],
        "Future": []
    }

    for link in links:
        lower = link.lower()

        if "intro" in lower or "overview" in lower:
            sections["Introduction"].append(link)
        elif "history" in lower or "background" in lower:
            sections["History"].append(link)
        elif "trend" in lower or "current" in lower:
            sections["Trends"].append(link)
        elif "challenge" in lower or "problem" in lower:
            sections["Challenges"].append(link)
        elif "solution" in lower or "solve" in lower:
            sections["Solutions"].append(link)
        elif "application" in lower or "use-case" in lower or "realworld" in lower:
            sections["Applications"].append(link)
        elif "benefit" in lower or "advantage" in lower:
            sections["Benefits"].append(link)
        elif "drawback" in lower or "limitation" in lower or "disadvantage" in lower:
            sections["Drawbacks"].append(link)
        elif "compare" in lower or "vs" in lower:
            sections["Comparison"].append(link)
        elif "future-trend" in lower or "evolution" in lower:
            sections["Future Trends"].append(link)
        elif "key-player" in lower or "industry-leader" in lower or "company" in lower:
            sections["Key Players"].append(link)
        elif "regulation" in lower or "policy" in lower or "legal" in lower:
            sections["Regulations"].append(link)
        elif "ethic" in lower or "bias" in lower:
            sections["Ethics"].append(link)
        elif "society" in lower or "social-impact" in lower:
            sections["Societal Impact"].append(link)
        elif "tech" in lower or "tool" in lower:
            sections["Technological Impact"].append(link)
        elif "case" in lower or "example" in lower:
            sections["Case Studies"].append(link)
        elif "future" in lower or "roadmap" in lower:
            sections["Future"].append(link)
        else:
            sections["Introduction"].append(link)

    return sections
