
from flask import Flask, render_template, request, redirect, url_for, flash, send_file
from modules.email_helper import send_email
from modules.pdf_generator import generate_pdf
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    treatment = request.form['treatment']
    cost = request.form['cost']
    
    # Generate PDF
    pdf_path = generate_pdf(name, treatment, cost)
    
    # Send Email (mock function)
    send_email(email, "Your Treatment Plan", "Please find attached.", pdf_path)
    
    flash('Treatment plan has been sent successfully!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
