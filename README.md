# AI-Powered Blog Generator with Daily Automation

This Python/Flask application generates SEO-optimized blog posts using AI technology. Given any keyword, it performs SEO research and creates structured blog drafts with affiliate link placeholders. The system automatically generates new content daily using a built-in scheduler.

## Features
- **SEO Research**: Fetches search volume, keyword difficulty, and CPC data
- **AI Content Generation**: Creates structured blog posts with OpenAI
- **Daily Automation**: Generates new posts automatically at 8:00 AM UTC
- **Affiliate Ready**: Includes {{AFF_LINK}} placeholders for monetization
- **Error Resilient**: Falls back to mock content when API limits are exceeded

## Technologies Used
- Python 3.11
- Flask (REST API)
- OpenAI API
- APScheduler (automation)
- JSON (data storage)

## Setup Instructions

### 1. Clone Repository
```bash
git clone https://github.com/<your-username>/ai-blog-generator-interview-<YourName>.git
cd ai-blog-generator-interview-<YourName>

