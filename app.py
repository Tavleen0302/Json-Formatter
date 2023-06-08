from flask import Flask, request, redirect, render_template, jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/jsonformat', methods=["POST"])
def format():
    firstname = request.form.get('first-name')
    lastname = request.form.get('last-name')
    email = request.form.get('email')
    date = request.form.get('date-of-birth')
    data = {
        "first-name": firstname,
        "last-name": lastname,
        "email": email,
        "date-of-birth": date
    }
    try:
        # Load existing data from the JSON file
        with open('users.json', 'r') as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        # If the file doesn't exist, initialize an empty dictionary
        existing_data = {}

    # Append the new user data to the existing data under a single key
    existing_data.setdefault('formData', []).append(data)

    # Write the updated data back to the JSON file
    with open('users.json', 'w') as file:
        json.dump(existing_data, file)

    # Retrieve the most recently added person
    recent_person = existing_data['formData'][-1]

    return render_template('json_template.html', jsonformat=recent_person)

if __name__ == '__main__':
    app.run()
