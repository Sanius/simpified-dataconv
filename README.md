# simpified DATA CONVERSION MYSQL TO MONGODB 

## Stack:
- python 3.8.13
- ckan 2.9.5
- postgres 13
- solr 6.6.6
- redis 6.2.6
- mysql 8.0.28
- mongodb 4.4.13
## Installation:
1. Install [pyenv](https://github.com/pyenv/pyenv)
1. Install and configure [CKAN](https://docs.ckan.org/en/2.9/maintaining/installing/install-from-source.html):
    - Install python virtual environment:
    ```bash
    pyenv install 3.8.13
    pyenv virtualenv 3.8.13 dataconv
    echo 'layout pyenv dataconv' > ../.envrc
    ```
    - To install CKAN 2.9.5 and ckanext_mysql2mongodb, run:
    ```bash
    python3 -m pip install -e 'git+https://github.com/ckan/ckan.git@ckan-2.9.5#egg=ckan[requirements]'
    python3 -m pip install -e 'git+https://github.com/ckan/ckan.git@ckan-2.9.5#egg=ckan[requirements,dev]'
    cd $PYENV_ROOT/versions/dataconv/src/ckan/ckanext/
    git clone https://github.com/Sanius/ckanext_mysql2mongodb && cd ckanext_mysql2mongodb
    python3 -m pip install -r requirements.txt
    poetry install
    python3 setup.py develop
    ln -s $PYENV_ROOT/versions/dataconv/src/ckan/ckanext/ckanext_mysql2mongodb ../ckanext_mysql2mongodb
    ```
    - Generate ckan config file:
    ```bash
    ckan generate config ./config/.ckan.ini
    ```
    - Compare **ckan.ini** with **.ckan.ini**
    - Edit **ckan.ini** (deprecated):
    ```
    sqlalchemy.url = postgresql://sandang:password@localhost:5432/dataconv_ckan
    ckan.datastore.write_url = postgresql://sandang:password@localhost:5432/dataconv_datastore
    ckan.datastore.read_url = postgresql://sandang:password@localhost:5432/dataconv_datastore
    ckan.site_url = http://localhost:5000
    ckan.site_id = default
    solr_url = http://localhost:11002/solr/dataconv_ckan
    ckan.redis.url = redis://localhost:11003/0
    ckan.plugins = stats text_view image_view recline_view datastore ckanext_mysql2mongodb
    ckan.storage_path = %(here)s/storage
    ```
    - Link to **who.ini**:
    ```bash
    ln -s $PYENV_ROOT/versions/dataconv/src/ckan/who.ini ./config/who.ini
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
    - Copy ./config/airflow.cfg paste to ~/airflow/airflow.cfg
    - Initialize airflow database and create airflow admin:
    ```bash
    python3 -m airflow db init
    python3 -m airflow users create --role Admin --username sandang -f san -l dang -e sandang@email.com
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
password: *****
```
- airflow:
```
username: sandang
password: *****
```
## Playground:
### MySQL:

### MongoDB:

### Postgresql: