import requests

API = "https://api.magicthegathering.io/v1/"

def main():

    setcode = input("What is the code of the set you are trying to lookup?".lower())

    resp = requests.get(f"{API}cards?set={setcode}")

    cards = resp.json().get("cards")

    print(cards)    

    with open("4DE_cards.set", "w") as card_file:
        for cardset in cards:
            print(f"{cardset.get('format')} -- {cardset.get('name')}", file = card_file)


main()