# Article-Preview-Webscrap
This opensource project is a web scraping tool that automatically downloads and extracts text previews from a list of news article URLs stored in a JSON file. It uses the newspaper3k library to fetch and parse web content, making it easy to generate datasets for NLP and machine learning applications.

## How It Works
1. Input: The script reads an input JSON file containing entries with fields like is_sarcastic, headline, and article_link.

2. Processing: For each article link, the script:

  > Downloads and parses the article using newspaper3k.

  > Extracts the first 500 characters of the article text as a "preview".

  > Handles errors gracefully, recording any issues encountered during processing.

3. Efficiency: Utilizes Python's concurrent.futures.ThreadPoolExecutor to process multiple articles in parallel, significantly speeding up the workflow. Progress is displayed via a progress bar (tqdm).

4. Output: Saves a new JSON file where each entry contains the original data plus a "preview" field (and an "error" field if any issues occurred).
![![output](https://github.com/user-attachments/assets/07d52441-0b9e-44a0-b52d-b17986d440d0)

## Usage
1. Install dependencies:

```bash pip install newspaper3k tqdm ```

  > Place your input JSON file (e.g., input.json) in the project directory.

2. Run the script:

```bash python process_articles.py ```

The script will generate output_with_previews.json with the extracted previews.

## Author - Sumit S. 
