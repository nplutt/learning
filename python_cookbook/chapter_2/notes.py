from fnmatch import fnmatch
import re


def match_strings_at_start_or_end():
    print(match_strings_at_start_or_end.__name__)

    name = 'spam.txt'
    print(name.endswith('txt'))
    print(name.startswith('spa'))

    blah = 'http:'
    print(name.startswith(('http:', 'spam', 'hello')))
    print(blah.startswith(('http:', 'spam', 'hello')))
    print('junk'.startswith(('http:', 'spam', 'hello')))


def matching_strings_using_wildcard_patterns():
    print(match_strings_at_start_or_end.__name__)

    print(fnmatch('foo.txt', '*.txt'))
    print(fnmatch('foo.txt', '?oo.txt'))


def searching_and_replacing_text():
    print(searching_and_replacing_text.__name__)

    text = 'hello world nick'
    text.replace('nick', 'john')
    print(text)


def search_for_and_replace_case_insensitive_text():
    print(search_for_and_replace_case_insensitive_text.__name__)

    text = 'UPPER PYTHON lower python Mixed Python'
    print(re.findall('python', text, flags=re.IGNORECASE))

    print(re.sub('python', 'snake', text, flags=re.IGNORECASE))
    


if __name__ == '__main__':
    match_strings_at_start_or_end()
    matching_strings_using_wildcard_patterns()
