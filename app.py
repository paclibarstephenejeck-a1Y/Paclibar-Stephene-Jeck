from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# Student information for Laboratory Activity 4
STUDENT_NAME = "Paclibar, Stephene Jeck"
STUDENT_ID = "24-00266"
PROGRAM = "BSIT"
YEAR_LEVEL = 3
SECTION = "Dijsktra"


@app.route("/")
def home():
    return (
        "<h1>My Flask API</h1>"
        "<p>Laboratory Activity 4: Deploying a Flask API Online</p>"
        "<p>Student: Paclibar, Stephene Jeck</p>"
        "<p>Available endpoints:</p>"
        "<ul>"
        "<li><a href='/student-profile'>/student-profile</a></li>"
        "<li><a href='/study-tip?subject=python'>/study-tip?subject=python</a></li>"
        "<li><a href='/grade-check?score=88'>/grade-check?score=88</a></li>"
        "</ul>"
    )


@app.route("/student-profile")
def student_profile():
    """Return the student's profile details as JSON."""
    return jsonify({
        "student_name": STUDENT_NAME,
        "student_id": STUDENT_ID,
        "program": PROGRAM,
        "year_level": YEAR_LEVEL,
        "section": SECTION
    })


@app.route("/study-tip")
def study_tip():
    """Return a study suggestion based on the subject passed in the URL."""
    subject = request.args.get("subject", "general").strip().lower()

    tips = {
        "python": "Practice by writing a small program and testing it.",
        "networking": "Draw a network diagram and label each device.",
        "database": "Practice writing SQL queries with a small sample table.",
        "web development": "Build one page at a time and test it in a browser.",
        "general": "Study in short sessions and review your notes regularly."
    }

    return jsonify({
        "endpoint": "study-tip",
        "subject": subject,
        "tip": tips.get(subject, "Break the topic into smaller parts and practice each part.")
    })


@app.route("/grade-check")
def grade_check():
    """Classify a numeric score supplied through the URL query string."""
    raw_score = request.args.get("score")

    if raw_score is None:
        return jsonify({
            "error": "Missing score parameter",
            "usage": "/grade-check?score=88"
        }), 400

    try:
        score = float(raw_score)
    except ValueError:
        return jsonify({"error": "Score must be a number."}), 400

    if not 0 <= score <= 100:
        return jsonify({"error": "Score must be between 0 and 100."}), 400

    if score >= 90:
        rating = "Excellent"
    elif score >= 85:
        rating = "Very Good"
    elif score >= 80:
        rating = "Good"
    elif score >= 75:
        rating = "Passed"
    else:
        rating = "Needs Improvement"

    return jsonify({
        "endpoint": "grade-check",
        "score": score,
        "rating": rating
    })


if __name__ == "__main__":
    # Render supplies PORT in production; local testing defaults to port 5000.
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
