import requests

API = "https://api.magicthegathering.io/v1/"

def main():

    resp = requests.get(f"{API}sets")

    cardsets = resp.json().get("sets")
    #open a file
    with open("mtgsets.index", "w") as mtgfile:
        for cardset in cardsets:
            print(f"{cardset.get('name')} -- {cardset.get('code')}", file=mtgfile)

main()