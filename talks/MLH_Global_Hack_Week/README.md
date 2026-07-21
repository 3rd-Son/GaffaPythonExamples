# Gaffa at Major League Hacking's Global Hack Week

This folder contains the notebooks used as examples in Gaffa's presentation at Major League Hacking's Global Hack Week. You can read more about what we covered in the talk in the [accompanying blog post](https://gaffa.dev/blog/gaffa-at-major-league-hackings-global-hack-week).

## Notebooks

| Notebook | Description |
|---|---|
| `webpage_to_markdown_and_qa.ipynb` | Scrapes a Wikipedia page, converts it to clean Markdown with Gaffa's `generate_markdown` action, then asks GPT-4o questions about the content |
| `structured_data_extraction_with_parse_json.ipynb` | Uses Gaffa's `parse_json` action to extract structured data from a Wikipedia page and an academic PDF — no CSS selectors or HTML parsing required |
| `image_scraper.ipynb` | Discovers every page on a site via Gaffa's `site/map` endpoint, renders each page, and downloads images with the `download_file` action |

## Requirements

- Python 3.8+
- A Gaffa API key — sign up at [gaffa.dev](https://gaffa.dev) and create your key in the **API Keys** section of the dashboard
- An OpenAI API key (only needed for `webpage_to_markdown_and_qa.ipynb`)

## Usage

Open any notebook in Jupyter or Google Colab and run the cells in order — each one installs its own dependencies and walks through the example step by step.
