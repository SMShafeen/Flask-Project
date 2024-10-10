from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db, add_application_to_db

app = Flask(__name__)

@app.route("/")
def hello():
  jobs = load_jobs_from_db()
  return render_template("home.html", jobs=jobs)

@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)

@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db(id)
  if not job:
    return "Page not found!", 404
  return render_template('job_page.html', job=job)

@app.route("/job/<id>/apply", methods=['post'])
def apply_to_job(id):
  job = load_job_from_db(id)
  # data = request.args # for getting data from url
  data = request.form # for getting data from form
  add_application_to_db(id, data)
  return render_template('application_submitted.html', application=data, job=job)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)





# JOBS = [
#   {
#     'id': 1,
#     'title': 'Data Analyst',
#     'location': 'Mumbai, India',
#     'salary': 'RS. 10,00,000',
#   },
#   {
#     'id': 2,
#     'title': 'Data Scientist',
#     'location': 'Hyderabad, India',
#     'salary': 'RS. 15,00,000',
#   },
#   {
#     'id': 3,
#     'title': 'Forntend Engineer',
#     'location': 'Remote',
#     'salary': 'RS. 12,00,000',
#   },
#   {
#     'id': 4,
#     'title': 'Backend Engineer',
#     'location': 'Bengaluru, India',
#     'salary': 'RS. 13,00,000',
#   },
#   {
#     'id': 5,
#     'title': 'Software Engineer',
#     'location': 'San Francisco, USA',
#     'salary': '$15,000',
#   },
# ]