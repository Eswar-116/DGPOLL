from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        post = request.form["post"].lower()
        risk = 0
        reasons = []

        # Category detection
        if "vaccine" in post or "virus" in post:
            category = "Health Misinformation"
            risk += 1
            reasons.append("Health-related keywords detected")
        elif "election" in post or "vote" in post:
            category = "Political Misinformation"
            risk += 1
            reasons.append("Political keywords detected")
        elif "free" in post or "money" in post:
            category = "Scam"
            risk += 1
            reasons.append("Scam-related keywords detected")
        else:
            category = "Normal Content"

        # Emotion detection
        if "kill" in post or "danger" in post:
            risk += 1
            reasons.append("Fear-based language detected")

        # Urgency detection
        if "share" in post or "fast" in post:
            risk += 1
            reasons.append("Urgency manipulation detected")

        # Risk level
        if risk >= 3:
            risk_level = "HIGH"
        elif risk == 2:
            risk_level = "MEDIUM"
        else:
            risk_level = "LOW"

        result = {
            "category": category,
            "risk": risk_level,
            "reasons": reasons
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)

