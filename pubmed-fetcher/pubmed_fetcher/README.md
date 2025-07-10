# PubMed Research Paper Fetcher

A CLI tool that fetches research papers from PubMed using a user query, and identifies those with authors from pharmaceutical or biotech companies.

## Features
- Uses PubMed API
- Filters non-academic authors using affiliation heuristics
- Outputs to CSV or console

## Setup
```bash
poetry install
```

## Usage
```bash
poetry run get-papers-list "cancer therapy" --file results.csv
```

## Tools Used
- [Typer](https://typer.tiangolo.com/)
- [Requests](https://docs.python-requests.org/)
- [Pandas](https://pandas.pydata.org/)
- [PubMed API](https://www.ncbi.nlm.nih.gov/books/NBK25500/)
