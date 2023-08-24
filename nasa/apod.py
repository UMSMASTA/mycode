#!/usr/bin/python3

import urllib.request
import json

NASAAPI = "https://api.nasa.gov/planetary/apod?"

def main():
    with open("/home/student/nasa.creds") as mycreds:
        nasacreds = mycreds.read()

    nasacreds = "api_key=" + nasacreds.strip("\n")

    apodurlobj = urllib.request.urlopen(NASAAPI + nasacreds)

    apodread = apodurlobj.read()

    apod = json.loads(apodread.decode("utf-8"))

    print("\nConverted Python Data")
    print(apod)

    print()

    print(apod["title"] + "\n")

    print(apod["date"] + "\n")

    print(apod["explanation"] + "\n")

    print(apod["url"])


main()
