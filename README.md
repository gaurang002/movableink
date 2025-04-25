# movableink
## Table of Contents

- [Problem Statement](#problem_statement)
- [Architecture](#architecture)
  - [Notes](#notes)
- [Setup Local Env](#setup_local_env)
- [Schme Diagram](#schema_diagram)
- [References](#references)


## Problem Statement
As an interviewee, one need to present end to end data solution using given sample data to gain business insights.

## Architecture
<p align="center">
  <img src="images/architecture.png" width="400" alt="Architecture Diagram">
</p>

## Notes
- Just for the scope of this solution to run locally, tools and technologies used are represented by red color texxt.
- Other colored components are open for discussion during the review meeting.

## Setup Local Env
- Assumption is that env is clean i.e. no prior postgres or airflow docker images/container existis.
- Initialize the database
  - `docker compose up airflow-init`
- You should see something like this after successful initialization
  ```
  airflow-init-1  | User "airflow" created with role "Admin"
  airflow-init-1  | 3.0.0
  airflow-init-1 exited with code 0
  ```
- Running airflow
  - `docker compose up -d`
  - Below containers should be up and running
  ```
  % docker ps
  CONTAINER ID   IMAGE                  COMMAND                  CREATED          STATUS                    PORTS                    NAMES
  77425690ceac   apache/airflow:3.0.0   "/usr/bin/dumb-init …"   8 minutes ago    Up 28 seconds (healthy)   8080/tcp                 movableink-airflow-worker-1
  3344f5db4fa8   apache/airflow:3.0.0   "/usr/bin/dumb-init …"   8 minutes ago    Up 39 seconds (healthy)   8080/tcp                 movableink-airflow-dag-processor-1
  914b1352f81c   apache/airflow:3.0.0   "/usr/bin/dumb-init …"   8 minutes ago    Up 39 seconds (healthy)   8080/tcp                 movableink-airflow-scheduler-1
  9baf29859583   apache/airflow:3.0.0   "/usr/bin/dumb-init …"   8 minutes ago    Up 39 seconds (healthy)   8080/tcp                 movableink-airflow-triggerer-1
  6cea0173e58b   apache/airflow:3.0.0   "/usr/bin/dumb-init …"   8 minutes ago    Up 39 seconds (healthy)   0.0.0.0:8080->8080/tcp   movableink-airflow-apiserver-1
  3a0b66c281d4   postgres:13            "docker-entrypoint.s…"   12 minutes ago   Up 51 seconds (healthy)   5432/tcp                 movableink-postgres-1
  9efb255fa675   redis:7.2-bookworm     "docker-entrypoint.s…"   12 minutes ago   Up 51 seconds (healthy)   6379/tcp                 movableink-redis-1
  %
  ```
- Adding psql connection
  - ```
    ./airflow.sh connections add 'my_postgres_conn' \
    --conn-uri 'postgresql://airflow:airflow@postgres:5432/airflow'
    ```
- Clean up env
  - `docker compose down --volumes --remove-orphans`

## References
- [Running Airflow in Docker](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html#fetching-docker-compose-yaml)
- [Airflow docker-compose.yaml](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html#fetching-docker-compose-yaml)
