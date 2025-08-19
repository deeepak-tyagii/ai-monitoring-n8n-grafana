import logging
from flask import Flask, jsonify
import sys
import os

# Define the directory for logs
log_dir = 'logs'

# Create the full path for the log file
log_file = os.path.join(log_dir, 'app.log')

# Create the log directory if it does not exist
# The 'exist_ok=True' argument prevents an error if the directory already exists.
os.makedirs(log_dir, exist_ok=True)


# Configure logger to output to stdout
logging.basicConfig(
    filename=log_file,
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%Ss'
)

app = Flask(__name__)

@app.route('/')
def index():
    logging.info("Accessed the root endpoint successfully.")
    return "Hello, World! Check the logs."

@app.route('/error')
def trigger_error():
    try:
        # Simulate a real error
        result = 1 / 0
    except Exception as e:
        # Log the exception with traceback information
        logging.error("A critical error occurred: Failed to perform division.", exc_info=True)
        return "An error has been logged!", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)