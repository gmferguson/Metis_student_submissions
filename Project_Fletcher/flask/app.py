from flask import Flask, make_response, request, abort, jsonify, render_template
from api import return_rec

app = Flask(__name__)
app.debug = True

@app.route('/recommendation', methods=['POST'])
def get_recommendation():
    if not request.json or ('resume' not in request.json):
        abort(400)

    resume = request.json['resume']
    company = request.json['company']
    location = request.json['location']
    job_title = request.json['job_title']
    # stars = request.json['stars']

    recommendation = return_rec(resume, company, location, job_title)

    response = {
        'resume': resume,
        'company': company,
        'location': location,
        'job_title': job_title,
        # 'stars': stars,
        'recommendation': recommendation
    }

    return jsonify(response), 201

@app.route('/')
def index():
    return render_template('index.html')
    
if __name__ == '__main__':
    app.run(debug=True)
