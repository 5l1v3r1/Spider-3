import requests
print(requests.get('http://www.distancebetweencities.us/result.php?fromplace=new%20york&toplace=boston').text)