import re 
import find

def extract_links(text):
    links = text.split()
    for link in links:
        link = re.findall(r'http(?:s)?://\S+', link)
        if link != []:
            if ".onion" in link: # TOR link ?
                if len(link) > 56: # v3 link ?
                    return link
    return 0
