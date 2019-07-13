from app import app
from db import db

db.init_app(app)

# Flask decorator - run the following function before anything else in the app
@app.before_first_request
def create_tables():
    db.create_all()
