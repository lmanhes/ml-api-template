# ml-api-template
Production-ready template for ML-based RESTful API


## Installation

Create a new virtual environment with python 3.8x, then install the dependencies :
```
pip install -r requirements.txt
```

## How to use locally

```bash
# Start redis server
$ redis-server

# Start celery workers
$ celery -A app.background worker -l info -Q main-queue -c 1

# Run the app
$ uvicorn app.main:app