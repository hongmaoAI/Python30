from flask import Flask, render_template, request
import os

app = Flask(__name__)


@app.route('/')
def home():
	techs = ['HTML', 'CSS', 'JavaScript', 'Python']
	name = '30天Python编程挑战'
	return render_template('home.html', techs=techs, name=name, title='主页')


@app.route('/about')
def about():
	name = '30天Python编程挑战'
	return render_template('about.html', name=name, title='关于我们')


@app.route('/post')
def post():
	name = '编程语言文章'
	path = request.path
	return render_template('post.html', name=name, path=path, title='文章')


@app.route('/result', methods=['POST'])
def result():
	first_name = request.form['first_name']
	last_name = request.form['last_name']
	old_job = request.form['old_job']
	current_job = request.form['current_job']
	country = request.form['country']
	print(request.form)
	result_data = {
		'first_name': first_name,
		'last_name': last_name,
		'old_job': old_job,
		'current_job': current_job,
		'country': country,
	}
	return render_template('result.html', result_data=result_data, title='表单数据收集结果')


if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(debug=True, host='0.0.0.0', port=port)
