import requests

MAJORTOM = 'http://api.open-notify.org/astros.json'

def main():

    #runtime code

    groundctrl = requests.get(MAJORTOM)

    helmetson = groundctrl.json()

    #print data
    print('\n]nConverted Python data')
    print(helmetson)

    print('\n\nPeople in Space: ', helmetson['number'])
    people = helmetson['people']
    print(people)

    for iss_key in people:
        if iss_key['craft'] == 'ISS':
            print(iss_key['name'], "on the", iss_key['craft'])

if __name__ == '__main__':
    main()