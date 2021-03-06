# JobHopper - README (v1)

## General Information

Jobhopper is an application for analyzing and querying career mobility and outside options data set to help workers, public sector professionals, and policymakers to improve career training, career paths, and career mobility options. GERONIMO!

## Scope & Problem Statement

Many workers have limited outside options for career and wage progression outside their current occupations. The quality of outside options matter for workers’ wages but limited data exists to provide guidance and training to workers on occupational mobility and outside-options (Monopsony and Outside Options. Schubert, Stansbury,and Taska. Harvard University, March 2020). The problem that we are tryingto solve is to provide better insight than standard data sets for improving occupational mobility options, improving worker wages, and improving policies related to investments and training.

## How to Install the Database and Analysis Tools

1. Install [Python 3.7](https://www.python.org/downloads/release/python-378/).

2. Install [virtualenv](https://pypi.org/project/virtualenv/) from `pip`:

   ```sh
   python3.7 -m pip install virtualenv

   OR on Windows 

   python -m pip install virtualenv
   ```

3. Clone this repo to local:
   ```sh
   git clone https://github.com/codeforboston/jobhopper.git
   ```
4. Create a virtual environment of Python 3.7 in the root of the local repo:
   ```sh
   cd jobhopper
   python3.7 -m virtualenv --python=3.7 venv

   OR on Windows 

   cd jobhopper
   python -m virtualenv --python=3.7 venv
   ```
5. Activate venv:
   ```sh
   . ./venv/bin/activate

   OR on Windows 

   ./venv/Scripts/activate
   ```
6. Install project dependencies from `requirements.txt`:
   ```sh
   pip install -r requirements.txt
   ```
7. Create a personal `.env` file to include environment variables for the app:
   (Note: Don't include `.env` in commit, thus it's in `.gitignore`):

   ```sh
   SECRET_KEY='[generated key]'
   ```

   You can get your own 50 character secret key from [here](https://miniwebtool.com/django-secret-key-generator/).

8. Create Postgres DB:

   a. Install [Postgres 12](https://www.postgresql.org/download/)

   b. Start postgresql service and check if clusters are running.

   ```sh
   sudo service postgresql start
   pg_lsclusters
   ```

   If the text is green, it's working.

   c. Run `psql` through the newly created `postgres` user.

   ```sh
   sudo -i -u postgres
   psql
   ```

   d. Create a new user/role for the site to access the database to. Name it
   however you like as long as you note the username and password for putting
   it in `.env`.

   ```sql
   CREATE ROLE [user]
   SUPERUSER
   LOGIN
   PASSWORD '[password]';
   ```

   e. Create a new database for the site to access. Name it however you like
   (preferably 'jobhopperdatabase') as long as you note the name of the
   database for putting it in `.env`.

   ```sql
   CREATE DATABASE [database name]
     WITH OWNER = [user];
   ```

   f. Exit out of `psql` and `postgres` user with the `exit` command for both
   cases.

   g. Add those information you written into the `.env` file.

   ```sh
   SECRET_KEY='[generated key]'

   DB_NAME='[database name]'
   DB_USER='[user/role name]'
   DB_PASSWORD='[password]'
   DB_HOST='127.0.0.1'  # Localhost IP
   ```

9. Follow instructions in [Data Readme](./Data/README.md) to load data prior to doing migrations described below and in DjangoData documetation.

10. Migrate from `manage.py` in root.

```sh
python manage.py migrate
```

Before proceeding, review this: [DjangoData](./References/DjangoData.md)

11. Now run the server via this script:

    ```sh
    python manage.py runserver
    ```

12. Go to the URL `http://127.0.0.1:8000/api/v1/jobs/`. From there there will be other links underneath that can be tested.
13. Go to the url `http://127.0.0.1:8000/api/v1/health` and ensure it returns json data.

## Technologies Used

| Front End          | Logic & Data Processing: | Database: |
| ------------------ | ------------------------ | --------- |
| React (JavaScript) | Django (Python 3.7)      | Postgres  |

For more details, see [Architecture](./References/Architecture.md)

## Additional Resources

[Data References](./References/References.md)
