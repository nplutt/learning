def urlify(url_str, length):
    url_arr = url_str.split(' ')
    url = ''

    for index, word in enumerate(url_arr):
        url += word
        if index < len(url_arr) - 1 and len(word) > 0:
            url += '%20'

    if url[-3:] == '%20':
        url = url[:-3]

    return url


if __name__ == "__main__":
    print(urlify("hello world    ", 1))
