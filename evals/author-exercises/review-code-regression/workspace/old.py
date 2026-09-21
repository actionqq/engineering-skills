def display(fetch):
    try:
        return fetch()
    except TimeoutError:
        return 'unavailable'
