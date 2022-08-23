# Simple Kafka Demo

## Prerequisite

- Python 3.10+
- Python Virtual Environments
- Pip
- Docker

## Project Setup

- Setup python virtual environment
  
  ```
  python -m venv db-env
  ```

- Then, activate the `db-venv`  
  
  ```
  # (Windows 10)
  db-env\Scripts\activate 
  ```

- Install python dependencies
  
  ```
  pip install -r requirements.txt
  ```  

- Setup docker-compose (assuming Docker is installed)
  
  ```
  docker-compose up
  ```

## Kafka Simulation

- Run the python scripts in different terminals
  
  ```sh
  # consumers
  python email.py
  python transactions.py

  # publisher
  python customer_service.py
  ```