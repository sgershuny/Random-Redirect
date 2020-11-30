import random
from flask import Flask, redirect

app = Flask(__name__)

# Note: http:// or https:// must be the prefix for proper redirection
websites = [
        "https://www.bbc.co.uk/sport/football",
        "google.com",
        "apple.com"
    ]

@app.route('/')
def index():
    website = random.choice(websites)
    return redirect(website)

if __name__ == "__main__":
    app.run()
