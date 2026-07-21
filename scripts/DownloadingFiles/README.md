# Download Files with Gaffa, No Matter How They're Served

This folder contains Python scripts that demonstrate how to use Gaffa's [`download_file`](https://gaffa.dev/docs/features/browser-requests/actions/download-file) action to download files through the [Browser Requests API](https://gaffa.dev/docs/features/browser-requests) — whether they download straight to disk, render inline in the browser, or only appear after filling out and submitting a form. For more information, read the [accompanying blog post](https://gaffa.dev/blog/how-to-download-files-from-any-website-with-gaffa).

## What It Does

- **`gaffa_download_both_scenarios.py`**: Downloads a file that saves directly to disk and a file that renders inline in the browser, using the exact same `download_file` action for both — no extra configuration needed to tell them apart.
- **`gaffa-form-file-pdf-download.py`**: Fills out and submits a web form (typing fields, clicking submit, waiting for the page to update), then downloads the resulting generated PDF.

In both cases, Gaffa returns the downloaded file as a hosted URL, which the script fetches and saves locally.

## How to Run

First, make sure you have the required libraries installed and your `GAFFA_API_KEY` environment variable set.

Required libraries:

```bash
pip install requests
```

```bash
export GAFFA_API_KEY="your_api_key_here"
```

Then, run either script:

```bash
python gaffa_download_both_scenarios.py
python gaffa-form-file-pdf-download.py
```

## Why Use Gaffa for This?

- **One Action, Any Delivery Method**: `download_file` handles direct downloads and browser-rendered files identically — no need to detect which pattern a site uses
- **Handles JavaScript**: Forms, modals, and dynamically-loaded content are rendered before the download is triggered
- **Automatic Format Detection**: Correct file extension provided in the download URL — no content-type parsing needed
- **Configurable Timeout**: Increase the `timeout` on `download_file` for larger files that take longer to generate or download

For more information, see the [Gaffa documentation](https://gaffa.dev/docs).
