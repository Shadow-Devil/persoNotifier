import os
import sys

import requests

def main(passport_id: str):
    req = requests.post('https://www17.muenchen.de/Passverfolgung/', data={'ifNummer': passport_id, 'pbAbfragen' : 'Abfragen'})
    if 'noch nicht zur Abholung bereit.' in req.text:
        print('Noch nicht zur Abholung bereit.')
    elif 'Fehler:' in req.text:
        print(req.text)
        raise Exception('Fehler beim Abrufen der Passverfolgung.')
    else:
        print('Zur Abholung bereit.')
        raise Exception('Zur Abholung bereit.')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python main.py <User>')
        sys.exit(1)
    user = sys.argv[1]

    if user == 'FELIX':
        main(os.environ['FELIX_PASSPORT_ID'])
    elif user == 'CHRISSI':
        main(os.environ['CHRISSI_PASSPORT_ID'])
    else:
        print('Usage: python main.py <User>')
        sys.exit(1)