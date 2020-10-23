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
# TODO: then, write a route called "student". Use the user
# route above as an example, and then run the app and go to that
# route. Check database.db again and see if something new appeared.
# The entries in database.db will be nonsense: don't worry about
# trying to understand it (you really aren't supposed to).
# But you should be able to see the entry at the bottom in mostly
# gibberish. If a new line is there, you've succeeded!
# Hint: DON'T FORGET TO ADD AND COMMIT!


# TODO: Now, let's work on querying!

@app.route('/all_students')
def query_all():
    # This queries for all the students. You can use filter_by to filter them.
    # TODO: try filtering students by name.
    # Hint: it would look something like: Students.query.filter_by(name="name").all()
    students = Students.query.all()
    return render_template('index.html', students=students)

# TODO: write your own route to query for users
# Play around with adding more users, and filtering queries.
# These are hard coded right now, and that's annoying.
# Check the assignments for some stretch challenges to get more practice!

# TODO: Now write a route to delete users!
# Hint: The syntax for deleting items should look like this:
# Users.query.filter_by(name="name").delete()
# OR
# Users.query.all().delete()
# HINT: DON'T FORGET TO COMMIT!

# TODO: Run your app. We're going to be running and initializing
# our app in this file, for simplicity during this tutorial.
