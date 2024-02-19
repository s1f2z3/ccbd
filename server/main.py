from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from ccc.usersDataBase import check_user_credentials
from ccc.database import returnCursor, closeConn
from ccc.productDataBase import show_elements
import json

def showw_elements(limit=5):
    conn, cursor = returnCursor()
    products=json.loads(show_elements(cursor, limit,False))
    closeConn(conn)
    return products

products=showw_elements(12,pr=False)


app = Flask(__name__, template_folder="templates")
app.secret_key = 'Djihad'  # Change this to a secure secret key

# Placeholder for user authentication logic (replace with your actual implementation)
def authenticate_user(username, hashed_password):
    # Check if user exists in the database
    conn, cursor = returnCursor()
    user_exists = check_user_credentials(cursor, username, hashed_password)
    closeConn(conn)
    return user_exists

@app.route("/")
def hello():
    if 'user_id' in session:
        # User is already authenticated, redirect to the main page
        return redirect(url_for('main_page', user_id=session['user_id'], products=products))
    else:
        # User is not authenticated, render the login page
        return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    # Extract username and hashed password from the received data
    username = data.get('username')
    hashed_password = data.get('password')

    # Authenticate user
    user_id = authenticate_user(username, hashed_password)

    if user_id > 0:
        # Successful login, store user_id in the session
        session['user_id'] = user_id
        # Set SameSite=None and Secure attributes for the session cookie
        session.permanent = True
        app.config['SESSION_COOKIE_SECURE'] = True
        app.config['SESSION_COOKIE_SAMESITE'] = 'None'
        return jsonify({'success': True, 'user_id': user_id})
    elif user_id == 0:
        # Invalid credentials, return an error response
        return jsonify({'error': 'Invalid credentials'})
    else:
        # Invalid credentials, return an error response
        return jsonify({'error': 'Server error'})

@app.route('/main')
def main_page():
    if 'user_id' in session:
        # User is authenticated, render the main page with user ID
        user_id = session['user_id']
        return render_template('store.html', user_id=user_id, products=products)
    else:
        # User is not authenticated, redirect to the login page
        return redirect(url_for('hello'))
    

@app.route('/logout')
def logout():
    # Clear the session to log the user out
    session.pop('user_id', None)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
