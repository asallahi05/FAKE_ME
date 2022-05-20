import requests
from json import loads
from time import sleep as wait
from sys import stderr, exit

def get_data(nat, number):
    url = "https://randomuser.me/api/?inc=gender,name,nat,email,login,location,phone,id&results={}&nat={}".format(number, nat)

    data = requests.get(url)
    return data.content
if __name__ == '__main__' :
    nat = input('Enter country code (ex: US):')
    try : number = int(input('How many data you need ? '))
    except :
        print('Not valid number', file=stderr)
        exit(1)
    data = loads(get_data(nat, number))
    for i in range(number) :
        
        print(f"Full name: {data['results'][i]['name']['first']} {data['results'][i]['name']['last']}")
        print(f"Gender   : {data['results'][i]['gender']}")
        print(f"Phone    : {data['results'][i]['phone']}")
        print(f"Email    : {data['results'][i]['email']}")
        print(f"Username : {data['results'][i]['login']['username']}")
        print(f"Password : {data['results'][i]['login']['password']}")
        print(f"Country  : {data['results'][i]['location']['country']}")
        print(f"Location : {data['results'][i]['location']['state']}, {data['results'][i]['location']['city']}, {data['results'][i]['location']['street']['name']} {data['results'][i]['location']['street']['number']} || Postcode: {data['results'][i]['location']['postcode']}\n")
        for x in range(85) :
            print('=', end='', flush=True)
            wait(0.002)
        print('\n')
        wait(0.05)