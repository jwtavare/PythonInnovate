import requests
import sys

modulename = 'requests'
if modulename not in sys.modules:
    print 'You have not imported the {} module'.format(modulename)

response = requests.get("http://api.open-notify.org/astros.json")
print(response)

alien_0 = {'color': 'goldish', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)