
from flask import Flask, jsonify, request
import os

app = Flask(__name__)

STUDENT_NAME = "Paclibar, Stephene Jeck"
STUDENT_ID = "24-00266"
PROGRAM = "BSIT"
YEAR_LEVEL = 3
SECTION = "Dijsktra"


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>My Flask API | Lab 4</title>
      <style>
        body {
          margin: 0;
          font-family: Arial, sans-serif;
          background: #0b1220;
          color: #f3f7ff;
          line-height: 1.6;
        }
        main { max-width: 900px; margin: auto; padding: 32px 20px; }
        h1 { font-size: 2.8rem; color: #70e0c6; }
        .profile, .card {
          background: #142137;
          border: 1px solid #2a3b55;
          border-radius: 16px;
          padding: 22px;
          margin: 16px 0;
        }
        .cards {
          display: grid;
          grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
          gap: 14px;
        }
        .card { margin: 0; }
        a { color: #70e0c6; font-weight: bold; }
        .muted { color: #afbed2; }
        .details { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
        @media(max-width: 500px) {
          .details { grid-template-columns: 1fr; }
          h1 { font-size: 2.1rem; }
        }
      </style>
    </head>
    <body>
      <main>
        <p class="muted">LABORATORY ACTIVITY 4 · PYTHON + FLASK</p>
        <h1>My Flask API</h1>
        <p class="muted">
          Welcome to my API dashboard. Choose an endpoint below
          to explore the live JSON responses.
        </p>

        <section class="profile">
          <h2>Student Profile</h2>
          <div class="details">
            <div><span class="muted">Full name</span><br>
              <strong>Paclibar, Stephene Jeck</strong></div>
            <div><span class="muted">Student ID</span><br>
              <strong>24-00266</strong></div>
            <div><span class="muted">Program / Year</span><br>
              <strong>BSIT · Year 3</strong></div>
            <div><span class="muted">Section</span><br>
              <strong>Dijsktra</strong></div>
          </div>
        </section>

        <h2>Explore API Endpoints</h2>
        <section class="cards">
          <article class="card">
            <h3>Student Profile</h3>
            <p class="muted">View your student information as JSON.</p>
            <a href="/student-profile">Open endpoint →</a>
          </article>
          <article class="card">
            <h3>Study Tip</h3>
            <p class="muted">Get a tip based on a subject.</p>
            <a href="/study-tip?subject=python">Try study tip →</a>
          </article>
          <article class="card">
            <h3>Grade Check</h3>
            <p class="muted">Check a score and receive a rating.</p>
            <a href="/grade-check?score=88">Check sample grade →</a>
          </article>
        </section>
      </main>
    </body>
    </html>
    """


@app.route("/student-profile")
def student_profile():
    return jsonify({
        "student_name": STUDENT_NAME,
        "student_id": STUDENT_ID,
        "program": PROGRAM,
        "year_level": YEAR_LEVEL,
        "section": SECTION
    })


@app.route("/study-tip")
def study_tip():
    subject = request.args.get("subject", "general").strip().lower()
    tips = {
        "python": "Practice by writing a small program and testing it.",
        "networking": "Draw a network diagram and label each device.",
        "database": "Practice writing SQL queries.",
        "web development": "Build one page at a time and test it.",
        "general": "Study in short sessions and review your notes."
    }
    return jsonify({
        "endpoint": "study-tip",
        "subject": subject,
        "tip": tips.get(subject, "Break the topic into smaller parts.")
    })


@app.route("/grade-check")
def grade_check():
    raw_score = request.args.get("score")
    if raw_score is None:
        return jsonify({"error": "Please provide a score, e.g. ?score=88"}), 400

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


@app.route("/health")
def health():
    return jsonify({"status": "ok", "message": "Flask API is running."})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
