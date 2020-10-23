"""Import Flask, SQLAlchemy."""
# TODO: import flask, sqlalchemy
# TODO: import your config file
from model_example import User

# TODO: Initialize your flask application

# TODO: Here, you'll need to also initialize your database.
# Hint: it should look something like: db = SQLAlchemy(app)

# TODO: Set your SQLALCHEMY_DATABASE_URI
# Hint: check the config.py file
# Remember how we configured our app from config before?

# TODO: Check the instructions in assignments and don't forget to create your
# database. You should see a file called database.db appear in your file
# tree. If you don't, review the steps to make sure everything is
# configured correctly.


@app.route('/user')
def insert_user():
    """Insert user to database table."""
    user = User(
                name="Test",
                username="tester",
                email="test@test.com",
                password="1234"
                )
    # This line uses the SQLAlchemy session to add and commit user to the
    # table
    # We then commit, because SQL needs a commit statement to "finalize"
    # the changes
    # TODO: go to this route, and then open database.db and see if something
    # new appeared!
    # Hint: don't forget to initialize and run your app first.
    db.session.add(user)
    db.session.commit()


# TODO: in models.py, follow the instructions to create a "Student"
# database model.
# TODO: then, write a route called "insert_student". Use the user
# route above as an example, and then run the app and go to that
# route. Check database.db again and see if something new appeared.
# The entries in database.db will be nonsense: don't worry about
# trying to understand it (you really aren't supposed to).
# But you should be able to see the entry at the bottom in mostly
# gibberish. If a new line is there, you've succeeded!

# TODO: Run your app. We're going to be running and initializing
# our app in this file, for simplicity during this tutorial.
