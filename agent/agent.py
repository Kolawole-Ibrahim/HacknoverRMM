import requests, psutil, socket, time

SERVER = "http://127.0.0.1:8000/agents/register"

while True:
    data = {
        "hostname": socket.gethostname(),
        "ip": socket.gethostbyname(socket.gethostname()),
        "cpu": psutil.cpu_percent(),
        "mem": psutil.virtual_memory().percent
    }
    try:
        r = requests.post(SERVER, json=data, timeout=5)
        print("Reported:", r.json())
    except Exception as e:
        print("Error:", e)
    time.sleep(30)
