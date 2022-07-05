import re 
import find

def check(urls):
    link = urls.split()
    for words in link:
        words = re.findall(r'http(?:s)?://\S+', words)
        if words != []:
            return words
        else:
            continue
    return 0
