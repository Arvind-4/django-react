echo "Starting the Django Server ..."
gunicorn -w 8 -k uvicorn.workers.UvicornWorker backend.asgi:application --bind=0.0.0.0