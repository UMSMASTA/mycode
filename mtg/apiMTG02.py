import requests

API = "https://api.magicthegathering.io/v1/"

def main():

#the request object/sets
    resp = requests.get(f"{API}sets")

    print(dir(resp))

main()