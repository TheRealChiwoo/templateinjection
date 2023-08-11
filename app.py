import json
from flask import Flask, render_template_string, request

app = Flask(__name__)

# Load blog posts from the JSON file
with open("posts.json") as f:
    blog_posts = json.load(f)

# Route to render the index.html template
@app.route('/')
def index():
    query = request.args.get('query', '')
    with open('index.html') as f:
        template = f.read()
    if len(query) > 0:
        template = "<p>Your query: " + query + "</p><hr>" + template
        # Filter blog posts based on the search query
    matching_posts = [post for post in blog_posts if query.lower() in (post["title"] + post["text"]).lower()]

    return render_template_string(template, blog_posts=matching_posts, query_result=query)

if __name__ == "__main__":
    app.run(port=8000, debug=True, host="0.0.0.0")

