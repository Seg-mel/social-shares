import re


def fetch(session, url):
    return session.get(
        'http://vk.com/share.php',
        params={'url': url, 'act': 'count', 'index': 1},
    )

def parse(response):
    if response.status_code != 200:
        raise IOError()

    return re.findall(r'\d+', response.text)[1]
