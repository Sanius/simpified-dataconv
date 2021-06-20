# simpified DATA CONVERSION MYSQL TO MONGODB 

## Stack:
- python 3.8.5
- ckan 2.9.2
- postgres 13
- solr 6.6.6
- redis 6.0.7
- mysql 8.0.22
- mongodb 4.4
## Installation:
1. Install [pyenv](https://github.com/pyenv/pyenv)
1. Install and configure [CKAN](https://docs.ckan.org/en/2.9/maintaining/installing/install-from-source.html):
    - Install python virtual environment:
    ```bash
    pyenv install 3.8.5
    pyenv virtualenv 3.8.5 ckan
    pyenv activate ckan
    ```
    - To install CKAN 2.9.2 and ckanext-mysql2mongodb, run:
    ```bash
    python3 -m pip install --upgrade pip
    python3 -m pip install -r ./config/requirements.txt
    python3 -m pip install -e 'git+https://github.com/ckan/ckan.git@ckan-2.9.2#egg=ckan[requirements]'
    python3 -m pip install -e 'git+https://github.com/Sanius/ckanext-mysql2mongodb@develop#egg=ckanext-mysql2mongodb' --no-cache-dir
    ```
    - Generate ckan config file:
    ```bash
    ckan generate config ./config/ckan.ini
    ```
    - Edit **ckan.ini**:
    ```
    sqlalchemy.url = postgresql://sandang:password@localhost:5432/ckan
    ckan.datastore.write_url = postgresql://sandang:password@localhost:5432/datastore
    ckan.datastore.read_url = postgresql://datastore_ro:password@localhost:5432/datastore
    ckan.site_url = http://localhost:5000
    ckan.site_id = default
    solr_url = http://localhost:8983/solr/ckan
    ckan.redis.url = redis://localhost:6379/0
    ckan.plugins = stats text_view image_view recline_view datastore ckanext-mysql2mongodb
    ckan.storage_path = %(here)s/storage
    ```
    - Link to **who.ini**:
    ```bash
    ln -s $PYENV_ROOT/versions/ckan/src/ckan/who.ini ./config/who.ini
    ```
    - Run docker inside **./compose**
    - Initialize ckan database and create sysadmin:
    ```bash
    ckan -c ./config/ckan.ini db init
    ckan -c ./config/ckan.ini sysadmin add sandang email=sandang@email.com name=sandang
    ckan -c ./config/ckan.ini seed gov
    ```
    - Setup datastore permission (copy below sql query, login to datastore postgres database then paste the query):
    ```bash
    ckan -c ./config/ckan.ini datastore set-permissions
    docker container exec -it postgresql psql -U sandang --password -h localhost -p 5432 -d datastore
    ```
1. Install and configure airflow:
    - Initialize airflow database and create airflow admin:
    ```bash
    python3 -m airflow db init
    python3 -m airflow users create --role Admin --username sandang -f san -l dang --password password -e sandang@email.com
    ```
    - Compare ~/airflow/airflow.cfg with ./config/airflow.cfg
    - Create **dags** directory inside $AIRFLOW_HOME and copy ./config/dagsbag.py into it.
    ```bash
    mkdir $AIRFLOW_HOME/dags
    cp ./config/dagsbag.py $AIRFLOW_HOME/dags/
    ```
1. Run system:
    ```bash
    ckan -c ./config/ckan.ini jobs worker
    ckan -c ./config/ckan.ini run
    python3 -m airflow scheduler
    python3 -m airflow webserver
    ```
## Login infos:
- ckan:
```
username: sandang
password: password
```
- airflow:
```
username: sandang
password: password
```
## Playground:
### MySQL:

### MongoDB:

### Postgresql: