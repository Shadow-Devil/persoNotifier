import requests

def main():
    req = requests.post('https://www17.muenchen.de/Passverfolgung/', data={'ifNummer': '', 'pbAbfragen' : 'Abfragen'})
    if('noch nicht zur Abholung bereit.' in req.text):
        print('Noch nicht zur Abholung bereit.')
    else:
        print('Zur Abholung bereit.')
        raise Exception('Zur Abholung bereit.')

if __name__ == '__main__':
    main()
