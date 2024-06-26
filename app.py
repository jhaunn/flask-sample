from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bengaluru, India',
        'salary': 'Rs. 10,00,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'San Francisco, USA',
        'salary': '$150,000'
    },
    {
        'id': 3,
        'title': 'Frontend Developer',
        'location': 'Bengaluru, India',
        'salary': 'Rs. 12,00,000'
    },
    {
        'id': 4,
        'title': 'Backend Engineer',
        'location': 'Remote',
        'salary': '$100,000'
    }
]

@app.route("/")
def hello_world():
    return render_template('home.html',
                          jobs = JOBS,
                          webpage_name = 'InnoWave Solutions')

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)