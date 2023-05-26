from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Bengaluru',
  'salary': 'Rs 1,00,000'
}, {
  'id': 2,
  'title': 'Web Dev',
  'location': 'Kolkata',
  'salary': 'Rs 1,20,000'
}, {
  'id': 3,
  'title': 'AI Engineer',
  'location': 'New Delhi',
  'salary': 'Rs 2,00,000'
}, {
  'id': 4,
  'title': 'UI UX Designer',
  'location': 'Remote',
  'salary': 'Rs 1,30,000'
}, {
  'id': 5,
  'title': 'System Analyst',
  'location': 'USA',
  'salary': 'Rs 1,90,000'
}]


@app.route('/')
def Hello_World():
  return render_template('home.html', jobs=JOBS)


@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
