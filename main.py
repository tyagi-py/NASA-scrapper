import requests
from datetime import date, timedelta
start_date = date(2010, 1, 1)
end_date = date(2020, 1, 1)
delta = timedelta(days=1)
while start_date <= end_date:
    print (start_date.strftime("%Y-%m-%d"))  
    key = 'm3HD2Qq9yQXtkjG5cHQBVdJjJNz2GuAxHiCsFLzL'
    params = {'date': start_date.strftime("%Y-%m-%d") , 'hd': True, 'api_key': key }
    r = requests.get('https://api.nasa.gov/planetary/apod', params= params)
    r = r.json()
    import os
    import urllib.request
    print(r['title'])
    print()
    print(r['explanation'])
    print('*' * 50)
    urllib.request.urlretrieve(r['hdurl'], start_date.strftime("%Y-%m-%d")+'.jpg')
    start_date += delta