README




For deployment on Heroku:

# create a requirements.txt
$ pip3 freeze > requirements.txt

# create file 'Procfile' with content:
web: gunicorn "app:create_app()"


# HEROKU
# create account
# install the Heroku CLI
$ brew tap heroku/brew & brew install heroku
# login for CLI
$ heroku login
+ press any key, this will open the Heroku login page in the browser. Then login. Then CLI logged in.

# create new app on Heroku webpage
create new app/

# Back on CLI:
# connect your git repository to the heroku new app
$ heroku git:remote -a fsnd-capstone-app-heroku

