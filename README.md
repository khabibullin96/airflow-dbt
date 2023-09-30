# airflow-dbt

## Install

1. `mkdir -p ./logs ./plugins ./config`

2. `echo -e "AIRFLOW_UID=$(id -u)" > .env`

3. `docker compose up airflow-init`

4. `docker compose up`

## Link

http://localhost:8080 - airflow-webserver <br>
http://localhost:80 - dbt docs
