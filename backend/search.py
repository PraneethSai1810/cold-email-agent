import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

JUNK_DOMAINS = ["instagram.com", "facebook.com", "linkedin.com/jobs", "indeed.com", "glassdoor.com"]

TRUSTED_DOMAINS = [
    "techcrunch.com", "theverge.com", "reuters.com", "bloomberg.com",
    "cnbc.com", "wsj.com", "ft.com", "engineering.", "blog.", "9to5google.com",
    "arstechnica.com", "wired.com", "forbes.com"
]

def domain_score(url: str) -> int:
    url_lower = url.lower()
    for domain in TRUSTED_DOMAINS:
        if domain in url_lower:
            return 10
    return 0


def search_company(company: str) -> list:
    try:
        query = f"{company} product launch OR engineering blog OR announcement 2026"

        response = client.search(
            query=query,
            search_depth="advanced",
            topic="news",
            days=60,
            max_results=8
        )

        results = response.get("results", [])

        filtered = [
            r for r in results
            if not any(junk in r.get("url", "") for junk in JUNK_DOMAINS)
            and company.lower() in r.get("title", "").lower()
        ]

        filtered = sorted(
            filtered,
            key=lambda x: x.get("score", 0) + domain_score(x.get("url", "")),
            reverse=True
        )

        all_sources = []
        for item in filtered[:4]:
            all_sources.append({
                "title": item.get("title", ""),
                "summary": item.get("content", "")[:200],
                "url": item.get("url", ""),
                "quality": item.get("score", 0) + domain_score(item.get("url", ""))
            })

        return all_sources

    except Exception as e:
        print(f"Tavily error: {e}")
        return []