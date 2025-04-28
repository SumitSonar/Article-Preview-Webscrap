import json
from newspaper import Article
from newspaper import Config
import concurrent.futures
from tqdm import tqdm

# Configure newspaper with custom settings
config = Config()
config.browser_user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
config.request_timeout = 10

def process_article(entry):
    try:
        article = Article(entry["article_link"], config=config)
        article.download()
        article.parse()
        
        return {
            "is_sarcastic": entry["is_sarcastic"],
            "headline": entry["headline"],
            "article_link": entry["article_link"],
            "preview": article.text[:500] if article.text else ""
        }
    except Exception as e:
        return {
            "is_sarcastic": entry["is_sarcastic"],
            "headline": entry["headline"],
            "article_link": entry["article_link"],
            "preview": "",
            "error": str(e)
        }

# Load your input JSON
with open('E:/SA/Sarcasm_Headlines_Dataset_fixed.json', 'r') as f:
    data = json.load(f)

# Process articles with threading
results = []
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
    futures = [executor.submit(process_article, entry) for entry in data]
    for future in tqdm(concurrent.futures.as_completed(futures), total=len(data)):
        results.append(future.result())

# Save output
with open('output_with_previews.json', 'w') as f:
    json.dump(results, f, indent=2)

print(f"Processed {len(results)} articles. Preview saved to output_with_previews.json")
