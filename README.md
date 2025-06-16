# Web-Scraping
This is a simple web application built using Flask that allows users to input a URL and retrieve all <a> (anchor) tags (i.e., hyperlinks) from that web page. The links are scraped using BeautifulSoup and then displayed in a neat, user-friendly format.

📸 Demo
Users enter a website URL like https://example.com, and the app displays a list of all the hyperlinks found on that page.

📦 Technologies Used
Python 🐍

Flask 🌐

BeautifulSoup4 🍜

HTML / Jinja2 🧩

requests 🔗

🧰 Setup Instructions
Clone the Repository

bash
Copy
Edit
git clone https://github.com/your-username/web-scraper-flask.git
cd web-scraper-flask
Create and Activate a Virtual Environment

bash
Copy
Edit
python3 -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate
Install the Required Packages

bash
Copy
Edit
pip install -r requirements.txt
Run the App

bash
Copy
Edit
python app.py
Access in Browser
Go to http://127.0.0.1:5000/

🧪 Features
🔗 Accepts user input for a URL

🔍 Fetches and parses HTML using BeautifulSoup

📄 Extracts all <a> tags with their text and href

🖼 Displays the data cleanly on the frontend

📁 Project Structure
graphql
Copy
Edit
web-scraper-flask/
│
├── app.py                 # Main Flask app
├── templates/
│   └── index.html         # HTML form and results
├── requirements.txt       # Required dependencies
└── README.md              # This file
✅ Example URLs to Test
https://example.com

https://news.ycombinator.com

https://wikipedia.org

⚠️ Notes
Ensure you enter a full URL starting with http:// or https://.

Some websites may block bots or require headers (already handled).

🙋 Author
Made with ❤️ by MAITAI