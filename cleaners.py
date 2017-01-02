from bs4 import BeautifulSoup


def attr(data, item):
    results = []
    if data is not None:
        for d in data:
            attr = d[item]
            results.append(attr)
    else:
        results.append('no results found')
    return results


def text(data, item):
    results = []
    if data is not None:
        for d in data:
            text = d.string
            results.append(text)
    else:
        results.append('no results found')
    return results


cleaners = {
    'attr': attr,
    'text': text, 
}
