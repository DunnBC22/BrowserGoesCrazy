import time
import webbrowser
import random


while True:
    list_of_sites = ['google.com', 'websudoku.com',
                     'youtube.com', 'indeed.com', 'linkedin.com', 'kaggle.com', 'weather.gov']
    site = random.choice(list_of_sites)
    visit = 'https://{}'.format(site)
    webbrowser.open(visit)
    seconds = random.randrange(3, 20)
    time.sleep(seconds)
