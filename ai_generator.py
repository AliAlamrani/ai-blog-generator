import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def generate_blog_post(keyword, seo_data):
    """
    Generate blog content with OpenAI API, falling back to mock content
    if API fails due to quota or other issues.
    """
    # First try to generate content with OpenAI
    try:
        # Only attempt if API key exists
        if os.getenv("OPENAI_API_KEY"):
            client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
            
            prompt = f"""
            Create a detailed 800-word blog post about '{keyword}' for an affiliate website.
            
            SEO DATA:
            - Monthly searches: {seo_data['search_volume']}
            - Competition: {seo_data['keyword_difficulty']}/100
            - Related terms: {', '.join(seo_data['related_keywords'][:3])}
            
            STRUCTURE:
            1. Engaging H1 title
            2. Introduction explaining why this matters
            3. Top 3 products comparison (table format)
            4. Detailed buying guide
            5. Conclusion with recommendations
            
            REQUIREMENTS:
            - Include 3 affiliate placeholder links: {{AFF_LINK_1}}, {{AFF_LINK_2}}, {{AFF_LINK_3}}
            - Use 2-3 H2 subheadings
            - Naturally include main keyword 5-7 times
            - Output in HTML format
            """
            
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=1500
            )
            return response.choices[0].message.content.strip()
    
    except Exception as e:
        print(f"OpenAI Error: {e}")

    # If OpenAI fails or no API key, use mock content
    print("Using mock content fallback")
    return get_mock_content(keyword)

def get_mock_content(keyword):
    """Generate mock blog content with the required structure"""
    return f"""
    <h1>Ultimate Guide to {keyword.title()}</h1>
    <p>This is a sample blog post about {keyword} generated as fallback content.</p>
    
    <h2>Top 3 {keyword} Products</h2>
    <ol>
        <li><a href="{{AFF_LINK_1}}">Premium {keyword}</a> - Best for professionals</li>
        <li><a href="{{AFF_LINK_2}}">Budget {keyword}</a> - Great value</li>
        <li><a href="{{AFF_LINK_3}}">Wireless {keyword}</a> - Top mobility</li>
    </ol>
    
    <h2>Buying Advice</h2>
    <p>When choosing {keyword}, consider durability and features. Always check reviews!</p>
    
    <p><strong>Note: Real AI content requires valid OpenAI API key and sufficient quota.</strong></p>
    """
