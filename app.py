from flask import Flask, redirect, request
import requests
import datetime

app = Flask(__name__)

# Log file path (change this to your desired log file)
LOG_FILE = "access.log"

def log_to_file(data):
    with open(LOG_FILE, 'a') as log_file:
        log_file.write(data)

@app.route('/')
def home():
    # Get the client's public IP address using httpbin
    try:
        response = requests.get('https://httpbin.org/ip')
        public_ip = response.json().get('origin', request.remote_addr)
    except Exception as e:
        public_ip = request.remote_addr

    # Log the client's public IP address and current date/time
    log_data = f"Client Public IP: {public_ip}, Date/Time: {datetime.datetime.now()}\n"
    log_to_file(log_data)

    # Redirect to the desired website
    return redirect('https://google.com')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
