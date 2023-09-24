import multiprocessing

bind = '0.0.0.0:8000'  # Use the appropriate host and port
workers = multiprocessing.cpu_count() * 2 + 1
daemon = True
# errorlog = '/path/to/your/error.log'
# accesslog = '/path/to/your/access.log'
