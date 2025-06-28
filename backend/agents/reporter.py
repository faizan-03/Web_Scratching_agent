def generate_report(expanded_data: dict) -> str:
    ordered_sections = [
        "Introduction",
        "History",
        "Trends",
        "Challenges",
        "Solutions",
        "Applications",
        "Benefits",
        "Drawbacks",
        "Comparison",
        "Future Trends",
        "Key Players",
        "Regulations",
        "Ethics",
        "Societal Impact",
        "Technological Impact",
        "Case Studies",
        "Future"
    ]

    report = ""
    section_num = 1

    for section in ordered_sections:
        match = next(
            (key for key in expanded_data if section.lower() in key.lower()),
            None
        )
        content = expanded_data.get(match, "").strip() if match else ""

        if content:
            heading = f"{section_num}. {section}"
            underline = "=" * len(heading)
            report += f"\n\n{heading}\n{underline}\n{content}\n"
            section_num += 1

    return report.strip()
