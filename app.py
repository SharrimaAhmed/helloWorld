from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World from Sharrima Ahmed! I am adding my first code change."

@app.route('/hello')
def hello_world():
    return render_template('hello.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/about-css')
def about_css():
    return render_template('about-css.html')

@app.route('/favorite-course')
def favorite_course():
    subject = request.args.get('subject')
    course_number = request.args.get('course_number')

    return render_template('favorite-course.html',
                             subject=subject,
                             course_number=course_number)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        return render_template('contact.html', form_submitted=True)
    else:
        return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
