from flask import Flask, request

app = Flask(__name__)
@app.route('/params')
def params():
	arg1 = request.args['arg1']
	arg2 = request.args['arg2']
	return 'Arg1 :' + arg1 + 'Arg2 : ' + arg2
	
if __name__ == '__main__':
	app.run(debug=True)