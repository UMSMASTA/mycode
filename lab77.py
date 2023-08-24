import requests
from datetime import datetime

resp = requests.get('http://api.open-notify.org/iss-now.json').json()

print(resp)
datetime_obj = datetime.fromtimestamp(resp['timestamp'])
print("CURRENT LOCATION OF THE ISS:\n")
print(f"Timestamp: {datetime_obj}")
print(f"Lon: {resp['iss_position']['longitude']}")
print(f"Lat: {resp['iss_position']['latitude']}")
