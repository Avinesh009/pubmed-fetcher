from typing import List, Dict


NON_ACADEMIC_KEYWORDS = ["pharma", "biotech", "inc", "llc", "gmbh", "ltd", "corporation", "company"]


def filter_non_academic_authors(papers: List[Dict], debug: bool = False) -> List[Dict]:
    filtered = []
    for paper in papers:
        non_academic_authors = []
        companies = set()
        corresponding_email = ""

        for author in paper.get("Authors", []):
            affil = author["affiliation"].lower()
            if any(keyword in affil for keyword in NON_ACADEMIC_KEYWORDS):
                non_academic_authors.append(author["name"])
                companies.add(author["affiliation"])
                if not corresponding_email:
                    corresponding_email = author["email"]

        if non_academic_authors:
            filtered.append({
                "PubmedID": paper["PubmedID"],
                "Title": paper["Title"],
                "Publication Date": paper["PublicationDate"],
                "Non-academic Author(s)": "; ".join(non_academic_authors),
                "Company Affiliation(s)": "; ".join(companies),
                "Corresponding Author Email": corresponding_email
            })

    return filtered
