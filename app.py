from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

history = []

def calculate_risk(data):
    score = 0

    if data.get("location") in ["Europe", "Russia", "Unknown", "Other"]:
        score += 25

    if data.get("device").lower() != "known":
        score += 20

    failed = int(data.get("failed_attempts", 0))
    score += min(failed * 8, 30)

    if data.get("time").lower() == "odd":
        score += 25

    return min(score, 100)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/evaluate", methods=["POST"])
def evaluate():
    data = request.json
    score = calculate_risk(data)

    if score < 30:
        decision = "Allow"
        color = "green"
    elif score < 60:
        decision = "MFA Required"
        color = "orange"
    else:
        decision = "Block"
        color = "red"

    history.append({
        "location": data.get("location"),
        "score": score,
        "decision": decision
    })

    if len(history) > 5:
        history.pop(0)

    return jsonify({
        "risk_score": score,
        "decision": decision,
        "color": color,
        "history": history
    })

if __name__ == "__main__":
    app.run(debug=True)