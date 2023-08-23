import requests
def main():

    #request object
    resp = requests.get("https://api.magicthegathering.io/v1/sets")

    #display the methods available
    print(dir(resp))

main()