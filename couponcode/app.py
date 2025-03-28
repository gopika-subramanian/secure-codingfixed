#{{url_for.__globals__.current_app.config}}-->payload
from flask import Flask, url_for,render_template,request,render_template_string,jsonify
app = Flask(__name__)
app.config['FLAG']=''



@app.route('/flag')
def flag():
	return render_template('flag.html')
	pass
@app.route('/')
def login():
	return render_template('login.html')

@app.route('/profile',methods=['POST','GET'])
def profile():
	if request.method=='POST':
		name=request.form['Uname']
		

		rendered_template=render_template('login.html',name=name)
		return render_template_string(rendered_template)
	else:
		return render_template('login.html')


@app.errorhandler(400)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

@app.errorhandler(500)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

@app.errorhandler(500)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
'''
@app.route('/login'))
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(username)


with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))

'''
if __name__ == "__main__":
    app.run(debug=True)