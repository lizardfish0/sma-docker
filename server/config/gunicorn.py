import multiprocessing

bind = "0.0.0.0:9090"
workers = multiprocessing.cpu_count()
loglevel = "info"
worker_class = "uvicorn.workers.UvicornWorker"