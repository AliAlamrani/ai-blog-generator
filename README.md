# AI-Powered Blog Generator with Daily Automation

A Python/Flask application that transforms keywords into SEO-optimized blog posts. Automates content creation with daily publishing - perfect for affiliate marketers and content creators.

## ✨ Features
- **SEO Research**: Fetches keyword metrics (search volume, difficulty, CPC)
- **AI Content Generation**: Creates structured blog drafts with OpenAI
- **Daily Automation**: Publishes new posts automatically at 8 AM daily
- **Affiliate-Ready**: Includes {{AFF_LINK}} placeholders for monetization
- **Error Resilient**: Falls back to mock content when API limits are hit

## 🛠️ Technologies Used
- **Backend**: Python 3.11, Flask
- **AI**: OpenAI GPT-3.5/GPT-4
- **Scheduling**: APScheduler
- **Data Handling**: JSON
- **Environment**: Python-dotenv

### 1. Clone the repository
```bash
git clone https://github.com/AliAlamrani/ai-blog-generator.git
cd ai-blog-generator-interview-AliAlamrani

python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate    # Windows

pip install -r requirements.txt

## put this in the .env file
OPENAI_API_KEY="your-api-key-here" 

python app.py

Visit this URL in your browser:
http://localhost:5000/generate?keyword=your-topic
