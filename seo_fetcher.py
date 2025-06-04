import random

def get_seo_data(keyword):
    """Generate mock SEO data for any keyword"""
    return {
        "search_volume": random.randint(1000, 50000),
        "keyword_difficulty": round(random.uniform(1.0, 100.0), 1),
        "avg_cpc": round(random.uniform(0.5, 15.0), 2),
        "related_keywords": [
            f"{keyword} reviews",
            f"best {keyword}",
            f"buy {keyword}",
            f"{keyword} 2024"
        ]
    } 
