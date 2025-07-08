from flask import Flask, render_template, request

app = Flask(__name__)

# Hardcoded credentials
VALID_USERNAME = "hiren.p"
VALID_PASSWORD = "HrN!38xk@2024"

@app.route('/', methods=['GET', 'POST'])
def login():
    message = ''
    color = ''
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')
        if username == VALID_USERNAME and password == VALID_PASSWORD:
            message = '✅ Login successful!'
            color = 'green'
        else:
            message = '❌ Invalid username or password.'
            color = 'red'
    return render_template('login.html', message=message, color=color)

if __name__ == '__main__':
    app.run(debug=True)