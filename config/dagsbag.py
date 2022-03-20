""" add additional DAGs folders """
import os
from airflow.models import DagBag
dags_dirs = ['$PYENV_ROOT/versions/dataconv/src/ckan/ckanext/ckanext_mysql2mongodb/ckanext/mysql2mongodb/dataconv/dag']

for dir in dags_dirs:
    dag_bag = DagBag(os.path.expanduser(dir))

    if dag_bag:
        for dag_id, dag in dag_bag.dags.items():
            globals()[dag_id] = dag
