from flask import Flask, jsonify, request
import urllib.parse

app = Flask(__name__)

# Mock tweet database
ALL_TWEETS = [
    {
        "from_user_name": "example_user",
        "geo": {"lat": 45.4642, "lon": 9.19},
        "text": "Enjoying the sunshine in Milan! #travel #sunny",
        "created_at": "2025-07-04T10:23:00",
        "hashtags": ["travel", "sunny"]
    },
    {
        "from_user_name": "test_user",
        "geo": None,
        "text": "This is a mock tweet about testing.",
        "created_at": "2025-07-04T11:15:32",
        "hashtags": ["testing"]
    },
    {
        "from_user_name": "test_user",
        "geo": {"lat": 37.7749, "lon": -122.4194},
        "text": "Nothing to do with the test word.",
        "created_at": "2025-07-03T18:47:10",
        "hashtags": []
    },
    {
        "from_user_name": "user123",
        "geo": None,
        "text": "Totally unrelated tweet with no test.",
        "created_at": "2025-07-02T09:05:45",
        "hashtags": []
    },
    {
        "from_user_name": "alice",
        "geo": {"lat": 51.5074, "lon": -0.1278},
        "text": "Greetings from London! #uk #vacation",
        "created_at": "2025-07-01T20:00:00",
        "hashtags": ["uk", "vacation"]
    }
]


@app.route('/search.json')
def search():
    q = request.args.get('q', '')
    decoded_q = urllib.parse.unquote_plus(q).lower()

    if 'from:' in decoded_q:
        username = decoded_q.split('from:')[1].split()[0].strip()
        results = [t for t in ALL_TWEETS if t["from_user_name"].lower() == username]
    else:
        results = [t for t in ALL_TWEETS if decoded_q in t["text"].lower()]

    return jsonify({"results": results})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
