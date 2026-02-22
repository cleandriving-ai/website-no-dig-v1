import os
import sys
import json
from datetime import datetime
from dotenv import load_dotenv
from firecrawl import FirecrawlApp

# Load environment variables from .env file
load_dotenv()

def crawl_site(url, output_dir):
    api_key = os.getenv("FIRECRAWL_API_KEY")
    if not api_key:
        print("Error: FIRECRAWL_API_KEY not found in .env file.")
        return

    app = FirecrawlApp(api_key=api_key)

    print(f"Starting crawl for: {url}")
    
    try:
        # Crawl the website
        # Limit to 10 pages for now to avoid excessive usage during testing
        crawl_job = app.crawl(url, 
            limit=10,
            scrape_options={"formats": ["markdown"]}
        )

        # In the new SDK, it returns a job object with a 'data' attribute
        # We check if it's a list or has data
        pages = []
        if hasattr(crawl_job, 'data'):
            pages = crawl_job.data
        elif isinstance(crawl_job, dict):
            pages = crawl_job.get("data", [])

        if not pages:
            print(f"No pages found or crawl failed for {url}")
            return

        # Process and save results
        domain = url.split("//")[-1].split("/")[0].replace(".", "_")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{domain}_{timestamp}.md"
        filepath = os.path.join(output_dir, filename)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"# Competitor Crawl: {url}\n")
            f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            for page in pages:
                # Page can be a dict or an object
                if hasattr(page, 'get'): # It's a dict
                    metadata = page.get('metadata', {})
                    title = metadata.get('title', 'Untitled')
                    source_url = metadata.get('sourceURL', 'N/A')
                    content = page.get('markdown', 'No content found.')
                else: # It's an object
                    metadata = getattr(page, 'metadata', {})
                    title = getattr(metadata, 'title', 'Untitled')
                    source_url = getattr(metadata, 'sourceURL', 'N/A')
                    content = getattr(page, 'markdown', 'No content found.')

                f.write(f"## Page: {title}\n")
                f.write(f"URL: {source_url}\n\n")
                f.write(content)
                f.write("\n\n---\n\n")

        print(f"Successfully saved crawl results to: {filepath}")

    except Exception as e:
        import traceback
        print(f"An error occurred: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python crawl_competitors.py <url>")
        sys.exit(1)

    target_url = sys.argv[1]
    # Go up two levels from tools/firecrawl-researcher to project root, then into research/competitors
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    output_directory = os.path.join(project_root, "research", "competitors")
    
    crawl_site(target_url, output_directory)
