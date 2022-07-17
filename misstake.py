import re 

def extract_link(text):
    links = text.split()
    for link in links:
        link = re.findall(r'^http(?:s)?:\/\/[A-Za-z0-9]{56}\.onion\S+', link)
        if link != []:
            return link
    return 0
