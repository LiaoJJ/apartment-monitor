## Abstract

Recently, I am looking for an apartment in Bay Area, but it proves the apartments 1b1b prices is skyrocket **HIGH!!!** Also, there are some luxury apartments that's out of rooms that I want. So, I develop this monitor to keep an eye on minimal prices as well as new apts released of these apartments.

## Ideas
- run every 30 minutes
- call floorplan endpoint of apartments to get the JSON availability data, 
- parse the json,
- when there is studio or low price available, play a music, send the e-mail, send the SMS message.

## Techniques
- Strategy pattern
- Object oriented design
- multi-threading
- HTTP request
- send e-mail

## Tech stacks:
- Python



running example:
```text
(base) abcdeg:apartment_monitor ljj$ python apt-monitor.py 
playsound is relying on a python 2 subprocess. Please use `pip3 install PyObjC` if you want playsound to run more efficiently.


Santa Clara Square Monitor: 2022-07-09 19:34:44.947284 HTTP Status: 200
Min Price: 3550
Studio: False

Lynhaven Monitor: 2022-07-09 19:34:45.381380 HTTP Status: 200
Min Price: 3209
num 1B1B: 26
email sent


Santa Clara Square Monitor: 2022-07-09 19:34:49.873867 HTTP Status: 200
Min Price: 3550
Studio: False

Lynhaven Monitor: 2022-07-09 19:34:50.242748 HTTP Status: 200
Min Price: 3209
num 1B1B: 26
```

The e-mail I got:
```text
Lynhaven min price: 3209 < 3660
Lynhaven new 1b1b is available, prev number: 0, now number: 26
Santa Clara Square min price: 3550 < 3660
```


## Future
- There is a bug with play sound in Python version issues
- Adding SMS module
