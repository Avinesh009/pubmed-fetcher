import typer
from pubmed_fetcher.fetcher import fetch_papers
from pubmed_fetcher.filters import filter_non_academic_authors
from pubmed_fetcher.writer import save_to_csv

app = typer.Typer()

@app.command()
def main(query: str, file: str = "", debug: bool = False):
    if debug:
        typer.echo(f"Searching PubMed with query: {query}")

    papers = fetch_papers(query, debug)
    filtered = filter_non_academic_authors(papers, debug)

    if file:
        save_to_csv(filtered, file)
    else:
        for p in filtered:
            print(p)

# ✅ FIXED LINE
if __name__ == "__main__":
    app()
