# micro-logistics

### a small web service for tracking shipping info using flask and mysql

Final work setup

A database user is configured for remote use by the webapp:

```
user: web
pass: CSE345Def@ult
```

`/sql` contains the SQL and Python scripts for creating the database schema and filling it.

`/sql/gen-fill-tables.py` can be run with `python` to generate a randomized SQL file to import into the database. There are some issues with some logic behind it (instances of multiple tracking processes for a single package), but it obeys all relational constraints and imports correctly for test use. 

To generate a randomized data file and create/import to database, run the following in the `/sql` directory:

```bash
python gen-fill-tables.py > fill-tables.sql
mysql -h cse345.carrio.me -D project -u web -p < create-tables.sql
mysql -h cse345.carrio.me -D project -u web -p < fill-tables.sql
```

`/python` contains the web server code for our application

Uses Flask, MySQLdb, and Jinja2 web templates. 

To run the application, go to the `/python` directory and run the following: 

```bash
pip2 install Flask MySQLdb
export FLASK_APP=serve.py
flask run
 * Running on http://127.0.0.1:5000/
```

`sudo` will be required for pip2 (or just pip if you use a default python2 distro) unless you create a `virtualenv`, which is outside the scope of these instructions. 
