import requests

def StartGame():
    url = 'https://bdclubapps.memastermind.repl.co/send'
    headers = {
        'authority': 'bdclubapps.memastermind.repl.co',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'accept-language': 'en-US,en;q=0.6',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://bdclubapps.memastermind.repl.co',
        'referer': 'https://bdclubapps.memastermind.repl.co/',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Brave";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'sec-gpc': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    }
    data = {
        'discord': '@vantuz',
        'trophies': '45000',
        'playerID': '#8QQ',
        'username': 'Vantuz5ThTone',
        'brawlers': '60',
        'favbrawler': 'Hank',
        'highestrank': 'diamond 3',
        'remarks': 'no',
        'cl': 'on',
        'cq': 'on',
        'memberhelp': 'on',
        'activeBS': 'on',
        'e': 'on'
    }
    response = requests.post(url, headers=headers, data=data)