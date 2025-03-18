import os
import firebase_admin
from firebase_admin import credentials, firestore, auth
from flask import Flask, render_template, request, redirect, url_for, flash, session
from functools import wraps

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET")

# Initialize Firebase Admin SDK
cred = credentials.Certificate({
    "type": "service_account",
    "project_id": os.environ.get("FIREBASE_PROJECT_ID"),
    "private_key": os.environ.get("FIREBASE_PRIVATE_KEY").replace("\\n", "\n"),
    "client_email": os.environ.get("FIREBASE_CLIENT_EMAIL")
})
firebase_admin.initialize_app(cred)
db = firestore.client()

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('user_token'):
            flash('Please log in first.', 'warning')
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    return render_template('index.html',
                         firebase_api_key=os.environ.get("FIREBASE_API_KEY"),
                         firebase_project_id=os.environ.get("FIREBASE_PROJECT_ID"),
                         firebase_app_id=os.environ.get("FIREBASE_APP_ID"))

@app.route('/drivers/add', methods=['GET', 'POST'])
@login_required
def add_driver():
    if request.method == 'POST':
        driver_data = {
            'name': request.form['name'],
            'age': int(request.form['age']),
            'pole_positions': int(request.form['pole_positions']),
            'race_wins': int(request.form['race_wins']),
            'points_scored': int(request.form['points_scored']),
            'world_titles': int(request.form['world_titles']),
            'fastest_laps': int(request.form['fastest_laps']),
            'team': request.form['team']
        }
        
        # Check for duplicate names
        existing_driver = db.collection('drivers').where('name', '==', driver_data['name']).get()
        if len(list(existing_driver)) > 0:
            flash('A driver with that name already exists!', 'error')
            return redirect(url_for('add_driver'))
            
        db.collection('drivers').add(driver_data)
        flash('Driver added successfully!', 'success')
        return redirect(url_for('index'))
        
    teams = [doc.to_dict() for doc in db.collection('teams').get()]
    return render_template('drivers/add.html', teams=teams)

@app.route('/teams/add', methods=['GET', 'POST'])
@login_required
def add_team():
    if request.method == 'POST':
        team_data = {
            'name': request.form['name'],
            'year_founded': int(request.form['year_founded']),
            'pole_positions': int(request.form['pole_positions']),
            'race_wins': int(request.form['race_wins']),
            'constructor_titles': int(request.form['constructor_titles']),
            'previous_season_position': int(request.form['previous_season_position'])
        }
        
        # Check for duplicate names
        existing_team = db.collection('teams').where('name', '==', team_data['name']).get()
        if len(list(existing_team)) > 0:
            flash('A team with that name already exists!', 'error')
            return redirect(url_for('add_team'))
            
        db.collection('teams').add(team_data)
        flash('Team added successfully!', 'success')
        return redirect(url_for('index'))
        
    return render_template('teams/add.html')

@app.route('/drivers/query')
def query_drivers():
    attribute = request.args.get('attribute')
    comparison = request.args.get('comparison')
    value = request.args.get('value')
    
    if all([attribute, comparison, value]):
        query = db.collection('drivers')
        if comparison == 'gt':
            query = query.where(attribute, '>', float(value))
        elif comparison == 'lt':
            query = query.where(attribute, '<', float(value))
        else:
            query = query.where(attribute, '==', float(value))
        
        drivers = [doc.to_dict() for doc in query.get()]
    else:
        drivers = []
        
    return render_template('drivers/view.html', drivers=drivers)

@app.route('/teams/query')
def query_teams():
    attribute = request.args.get('attribute')
    comparison = request.args.get('comparison')
    value = request.args.get('value')
    
    if all([attribute, comparison, value]):
        query = db.collection('teams')
        if comparison == 'gt':
            query = query.where(attribute, '>', float(value))
        elif comparison == 'lt':
            query = query.where(attribute, '<', float(value))
        else:
            query = query.where(attribute, '==', float(value))
        
        teams = [doc.to_dict() for doc in query.get()]
    else:
        teams = []
        
    return render_template('teams/view.html', teams=teams)

@app.route('/auth/process', methods=['POST'])
def process_auth():
    token = request.form['token']
    try:
        decoded_token = auth.verify_id_token(token)
        session['user_token'] = token
        session['user_id'] = decoded_token['uid']
        flash('Successfully logged in!', 'success')
    except:
        flash('Authentication failed!', 'error')
    return redirect(url_for('index'))

@app.route('/auth/logout')
def logout():
    session.clear()
    flash('Successfully logged out!', 'success')
    return redirect(url_for('index'))
