import requests
import xml.etree.ElementTree as ET
from typing import List, Dict

BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"


def fetch_papers(query: str, debug: bool = False) -> List[Dict]:
    search_url = f"{BASE_URL}esearch.fcgi"
    fetch_url = f"{BASE_URL}efetch.fcgi"

    search_params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": 20
    }

    search_resp = requests.get(search_url, params=search_params)
    ids = search_resp.json()["esearchresult"]["idlist"]

    fetch_params = {
        "db": "pubmed",
        "id": ",".join(ids),
        "retmode": "xml"
    }

    fetch_resp = requests.get(fetch_url, params=fetch_params)
    root = ET.fromstring(fetch_resp.text)
    
    papers = []
    for article in root.findall(".//PubmedArticle"):
        paper = {
            "PubmedID": article.findtext(".//PMID"),
            "Title": article.findtext(".//ArticleTitle"),
            "PublicationDate": article.findtext(".//PubDate/Year") or "Unknown",
            "Authors": []
        }
        authors = article.findall(".//Author")
        for author in authors:
            affil = author.findtext("AffiliationInfo/Affiliation")
            name = (author.findtext("LastName") or "") + ", " + (author.findtext("ForeName") or "")
            email = ""
            if affil and "@" in affil:
                email = affil.split(" ")[-1]
            paper["Authors"].append({"name": name, "affiliation": affil or "", "email": email})
        papers.append(paper)

    return papers