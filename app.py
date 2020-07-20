from astrology import horoscope_info
from flask import Flask, make_response, render_template, request, Response
app = Flask(__name__)

signs = [
    'aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra',
    'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces'
]

days = [
        'today', 'tomorrow', 'yesterday'
]

@app.route('/')
def display_home():
    headers = {'Content-Type': 'text/html'}
    return make_response(render_template('index.html'), 200, headers)

@app.route('/portfolio')
def show_portfolio():
    headers = {'Content-Type': 'text/html'}
    return make_response(render_template('portfolio.html'), 200, headers)

@app.route('/about')
def show_about():
    headers = {'Content-Type': 'text/html'}
    return make_response(render_template('about.html'), 200, headers)


@app.route('/contact', methods=['POST','GET'])
def show_contact():
    if request.method == 'POST':
        contact_name = request.form['Name']
        print(contact_name)
        # your code
        return Response(response=render_template('thankyou.html'))
    else:
        return Response(response=render_template('thankyou.html'))


@app.errorhandler(404)
def page_not_found(e):
    return Response(response=render_template('404.html'))

@app.errorhandler(405)
def method_not_allowed(e):
    return Response(response=render_template('error.html'))

@app.route('/detailedforecast',methods=['POST','GET'])
def show_astrodetails():
    if request.method == 'POST':
        sign = request.form['sunShineID'].lower()
        day = request.form['dayId']
        timezone = request.form['timeID']
    else:
        sign = request.args['sign'].lower()
        day = request.args.get('day', 'today').lower()
        timezone = request.args.get('tz')
    try:
        if (sign not in signs) or (day not in days):
            raise Exception('Wrong sign or day passed.')

        response = horoscope_info(sign=sign, day=day, tz=timezone)
        return render_template("details.html",result=response)
    except Exception as e:
        return {'message': str(e)}, 400

@app.route('/api/forecastdetails', methods=['GET','POST'])
def api_response():
    if request.method == 'POST':
        sign = request.form['sign'].lower()
        day = request.form.get('day', 'today').lower()
        timezone = request.form.get('tz')
    else:
        sign = request.args['sign'].lower()
        day = request.args.get('day', 'today').lower()
        timezone = request.args.get('tz')
    try:
        if (sign not in signs) or (day not in days):
            raise Exception('Wrong sign or day passed.')

        response = horoscope_info(sign=sign, day=day, tz=timezone)
        return response, 200
    except Exception as e:
        return {'message': str(e)}, 400


if __name__ == '__main__':
    app.run()


