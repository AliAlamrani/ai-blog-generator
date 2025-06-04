from flask import Flask, jsonify, request
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import json
import atexit
import socket

# Import modules
from seo_fetcher import get_seo_data
from ai_generator import generate_blog_post

app = Flask(__name__)

# Bypass security restrictions for local development
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'GET'
    return response

@app.route('/generate', methods=['GET'])
def generate_post():
    # Get keyword from URL or use default
    keyword = request.args.get('keyword', 'wireless earbuds')
    
    # Get SEO data
    seo_data = get_seo_data(keyword)
    
    # Generate content
    blog_content = generate_blog_post(keyword, seo_data)
    
    # Create result 
    result = {
        "keyword": keyword,
        "seo_data": seo_data,
        "content": blog_content,
        "timestamp": datetime.now().isoformat()
    }
    
    # Save to files
    safe_keyword = keyword.replace(' ', '_').lower()
    filename = f"blog_{safe_keyword}_{datetime.now().strftime('%Y%m%d_%H%M')}.json"
    with open(filename, 'w') as f:
        json.dump(result, f, indent=2)
    
    print(f"Generated blog post: {filename}")
    return jsonify(result)

def daily_job():
    print("\n Starting daily post generation...")
    with app.app_context():
        generate_post()
    print("Daily post saved!\n")

def get_local_ip():
    """Get your machine's local IP address"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

if __name__ == '__main__':
    # Setup scheduler
    scheduler = BackgroundScheduler()
    scheduler.add_job(daily_job, 'cron', hour=8, minute=0)
    scheduler.start()
    
    # Shut down scheduler when exiting the app
    atexit.register(lambda: scheduler.shutdown())
    
    local_ip = get_local_ip()
    
    print("="*50)
    print("AI Blog Generator Running!")
    print(f"Local access URL: http://127.0.0.1:5000/generate?keyword=test")
    print(f"Network access URL: http://{local_ip}:5000/generate?keyword=test")
    print("="*50)
    
    # Start Flask app with external access
    app.run(debug=True, host='0.0.0.0', port=5001, threaded=True)
