import bibtexparser
from pathlib import Path

# --- Configuration ---
bib_path = Path("_bibliography/publications.bib")
output_path = Path("_pages/publications.md")

# --- Load BibTeX ---
with open(bib_path, encoding="utf-8") as bibfile:
    bib_database = bibtexparser.load(bibfile)

# --- Prepare Markdown output ---
header = """---
layout: single
title: "Publications"
permalink: /publications/
author_profile: false
---

Below is a list of selected publications.

"""

def format_entry(entry):
    authors = entry.get("author", "").replace(" and ", ", ")
    title = f"{entry.get('title', 'Untitled')}"
    year = entry.get("year", "")
    journal = entry.get("journal", entry.get("booktitle", ""))
    vol = entry.get("volume", "")
    pages = entry.get("pages", "")
    doi = entry.get("doi", "")
    pdf = entry.get("pdf", "")

    links = []
    if pdf:
        links.append(f"[PDF]({pdf})")
    if doi:
        links.append(f"[DOI](https://doi.org/{doi})")
    
    # Use a middle dot separator instead of a raw pipe
    link_text = " • ".join(links)

    # ref = f"{authors}, *{title}*, {journal} **{vol}** {pages} ({year})."
        # --- Build publication reference dynamically ---
    parts = []
    if authors:
        parts.append(authors+",")
    if title:
        parts.append(f"*{title}*,")
    if journal:
        parts.append(journal)

    # Only add volume if it exists
    if vol:
        parts.append(f"**{vol}**")
    # Only add pages if it exists
    if pages:
        parts.append(pages)
    if year:
        parts.append(f"({year})")

    # Join all parts nicely with spaces
    ref = " ".join(parts) + "."

    if link_text:
        ref += f" {link_text}"

    return f"- {ref}"

entries = [format_entry(e) for e in bib_database.entries]
content = header + "\n".join(entries) + "\n"

# --- Write Markdown file ---
output_path.write_text(content, encoding="utf-8")
print(f"✅ Publications page generated: {output_path}")