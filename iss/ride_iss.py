import urllib.request
import json

MAJORTOM = "http://api.open-notify.org/astros.json"

def main():
    #reading json from the api
    groundctrl = urllib.request.urlopen(MAJORTOM)

    #strip off attachment and read
    helmet = groundctrl.read()

    #show data, it is a string and need to convery to list/dict
    helmetson = json.loads(helmet.decode("utf-8"))
    print(helmet)
    print(type(helmet))
    print(type(helmetson))

    #return list of people
    print(helmetson["number"])
    print(helmetson["people"])

    print(helmetson["people"][0])

    print(helmetson["people"][-1])

    #display every item in list
    for astro in helmetson["people"]:
        print(astro)
    
    for astro in helmetson["people"]:
        print(astro['name'])
        

main()