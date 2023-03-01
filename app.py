from flask import Flask, render_template,jsonify

app = Flask(__name__)
JOBS=[
  {
    "id": "1",
    "position":"data analyst",
    "salary":"10,20,000",
    "location":"bengaluru"
  },
    {
    "id": 2,
    "position":"data scientist",
    "salary":"15,20,000",
    "location":"chennai"
  },
    {
    "id": "3",
    "position":"front end",
    "salary":"13,20,000",
    "location":"haryana"
    }
    
]

@app.route("/")
def hello_world():
  return render_template('home.html',jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host="0.0.0.0",debug=True)