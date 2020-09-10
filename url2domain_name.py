import re

url = input()


def domain_name(string):
    www_regex = '(?<=www\.)([a-zA-Z\-0-9]*)'
    http_regex = '(?<=://)([a-zA-Z\-0-9]*)'
    # The one below doesn't work - must be fixed
    no_prefix_regex = '([a-zA-Z\-0-9]+(?=\.))'
    new_string = ''
    if 'www' in string:
        new_string = re.findall(www_regex, string)
    elif 'http' in string:
        new_string = re.findall(http_regex, string)
    else:
        new_string = re.findall(no_prefix_regex, string)
    
   
    if len(new_string) > 1:
        new_string = new_string.pop(1)
    else:
        new_string = new_string.pop()


print(domain_name(url))
