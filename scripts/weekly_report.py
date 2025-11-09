"""Generate weekly stakeholder summary HTML from domain data."""

from pathlib import Path

import pandas as pd

DATA_PATH = Path("data/campaign_performance.csv")
OUTPUT_PATH = Path("reports/weekly_summary.html")


def main() -> None:
    df = pd.read_csv(DATA_PATH)
    summary = df.describe(include="all").to_html()
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    html = (
        "<!DOCTYPE html><html><head><title>Weekly Summary</title></head>"
        f"<body><h1>Weekly Stakeholder Summary</h1>{summary}</body></html>"
    )
    OUTPUT_PATH.write_text(html, encoding="utf-8")
    print(f"Wrote {{OUTPUT_PATH}}")


if __name__ == "__main__":
    main()
