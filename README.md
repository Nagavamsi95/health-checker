&#x20;  # Health Checker



&#x20;  A small Python service that checks whether websites are up, records their response times, and exposes the results through a Flask API.



&#x20;  ## Features

&#x20;  - Reads a list of endpoints from `config.yaml`

&#x20;  - Reports status code and response time for each endpoint

&#x20;  - `/health` route for the checker itself

&#x20;  - `/status` route with results for all endpoints

&#x20;  - Unit tests with pytest



&#x20;  ## Setup

```bash

&#x20;  python -m venv venv

&#x20;  venv\\Scripts\\activate

&#x20;  pip install -r requirements.txt

```



&#x20;  ## Run

```bash

&#x20;  python checker.py    # print results in the terminal

&#x20;  python app.py        # start the Flask API on port 5000

```



&#x20;  ## Test

```bash

&#x20;  python -m pytest -v

```



&#x20;  ## Screenshots

&#x20;  !\[Health endpoint](screenshots/01-health-endpoint.png)

&#x20;  !\[Status endpoint](screenshots/02-status-endpoint.png)

&#x20;  !\[Checker output](screenshots/03-checker-output.png)

&#x20;  !\[Flask running](screenshots/04-flask-running.png)

