Cushions is a lightweight data-collection tool that uses XForms and CouchDB.
It's meant to be a server-side backend to JavaRosa or ODK.

It's named for the way that artifacts like spare change collect in the cushions
of a couch. Your data is collected here for you to find and use later on.

It is currently an extremely bare proof-of-concept collection of tools. Sorry
about how ugly it is.

This assumes you have couchdb, setuptools and pip installed. The easiest way 
to get couch is to grab an installer from http://www.couch.io/get. We are 
compatible 1.0.1+. On Ubuntu, apt-get makes installation super easy:

$ sudo apt-get install couchdb

INSTALLATION

Download or clone the repository from git.

If needed, install setuptools and pip.

Initialize and update the submodules:

$ git submodule init
$ git submodule update

Install dependencies (must be run as root)

$ sudo pip install -r requirements.txt

If you run into problems when pip tries to install psycopg2, check out
the following solution on Stack Overflow:
http://stackoverflow.com/questions/5420789/how-to-install-psycopg2-with-pip-on-python/5450183#5450183

If you need to make any changes to settings please add a localsettings.py file 
to the root directory. This is a good place to configure your django and couch 
databases. You can use the localsettings.example.py to get you started

$ cp localsettings.example.py localsettings.py  

Finally, sync and run server.

$ python manage.py syncdb
$ python manage.py runserver

Cushions should be running at http://localhost:8000
