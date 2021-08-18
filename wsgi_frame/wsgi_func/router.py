from urls import urls

urls_dict = dict(urls)


def route(url, urls_dict=urls_dict):
    return urls_dict.get(url)