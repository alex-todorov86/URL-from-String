import re

url = input()
def url_2_domainname(string):
    www_regex = '(?<=www\.)([a-zA-Z\-0-9]*)'
    http_regex = '(?<=://)([a-zA-Z\-0-9]*)'
    new_string = ''
    if 'www' in string:
        new_string = re.findall(www_regex, string)
    else:
        new_string = re.findall(http_regex, string)

    return str(new_string[0])

print(url_2_domainname(url))