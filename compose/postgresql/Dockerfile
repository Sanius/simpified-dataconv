FROM postgres:13

# Allow connections; we don't map out any ports so only linked docker containers can connect
RUN echo "host all  all    0.0.0.0/0  md5" >> /var/lib/postgresql/data/pg_hba.conf

# Customize default user/pass/db
ARG POSTGRES_DB=${POSTGRES_DB}
ARG POSTGRES_USER=${POSTGRES_USER}
ARG POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
ARG DS_DB=${DS_DB}
ARG DS_RO_PASS=${DS_RO_PASS}
ARG DS_RO_USER=${DS_RO_USER}
ARG AIRFLOW_USER=${AIRFLOW_USER}
ARG AIRFLOW_PASSWORD=${AIRFLOW_PASSWORD}
ARG AIRFLOW_DB=${AIRFLOW_DB}

# Include datastore setup scripts
ADD ./postgresql/docker-entrypoint-initdb.d /docker-entrypoint-initdb.d
