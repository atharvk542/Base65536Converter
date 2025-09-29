# Gunicorn configuration file
import os

bind = f"0.0.0.0:{os.environ.get('PORT', 5000)}"
backlog = 2048

workers = os.environ.get("WEB_CONCURRENCY", 4)
worker_class = "sync"
worker_connections = 1000
timeout = 30
keepalive = 2

# Restart workers after this many requests, to help control memory usage
max_requests = 1000
max_requests_jitter = 100

accesslog = "-"
errorlog = "-"
loglevel = "info"

proc_name = "base65536_converter"

preload_app = True
daemon = False
pidfile = None
user = None
group = None
tmp_upload_dir = None

