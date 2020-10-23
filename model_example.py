"""
Create our first database model.

If this file is showing errors,
check to make sure you created your
db in app.py first!
"""
from app import db


class User(db.Model):
    """Create class User."""

    # SQL automatically assigns sequential integer ids to each record
    name = db.Column(db.String(40), nullable=False)
    # This is a string with a maximum of 40 characters
    username = db.Column(db.String(40), nullable=False)
    # Nullable=False means that we have to set this property
    email = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(120), nullable=True)
    # We set a default here of "False" for all new users
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
