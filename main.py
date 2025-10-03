import configparser,json,requests,re,os,time
import urllib.parse as urllib
from sys import argv

scraped = open("scraped.txt","r+")
confparser = configparser.ConfigParser()
my_config = None
with open("config.json","r") as f:
    my_config = json.load(f)

def initodict(ini):
    # Totally not stolen from https://www.pythonforbeginners.com/basics/convert-ini-files-to-json-format-in-python
    config_object = configparser.ConfigParser()
    file =open(ini,"r")
    config_object.read_file(file)
    output_dict=dict()
    sections=config_object.sections()
    for section in sections:
        items=config_object.items(section)
        output_dict[section]=dict(items)
    file.close()
    return output_dict

if type(my_config["repositories"]) is str: my_config["repositories"] = initodict(my_config["repositories"])

filescrape = {}
repos = dict(
    sorted(my_config["repositories"].items(),
        key=lambda item: int(item[1]["priority"]),
        reverse=True
    )
)

def update_repos(m=0):
    global scraped
    def scrape_repo(repolink,repo,scrape_output):
        number = 0
        response = requests.get(repolink.strip("\""))
        if response.status_code != 200:
            print(f"PYMGR: Repository {repolink.strip()} is too busy dominating pymgr in a gay mating press and therefore cannot be scraped ({status_code})")
            return
        html = response.text
        file_urls = re.findall(fr'<a[^>]*\shref="({re.escape(repo['code'])}([^"]+))"',html)
        for file_url in file_urls:
            response = requests.get(repolink.strip("\""))
            print(f'{file_url}: scraped from link: {repo['nickname']}')
            scrape_output.write(f'{repo['base']}{file_url[0]}\n')
            number += 1
            if m!=0 and number>m: break
        print(f"PYMGR: Repository scrape for {repo['nickname']} completed")
    scraped.truncate(0)
    scraped.seek(0)
    for link,repo in repos.items():
        print(f"Scrapping {repo['nickname']}")
        scrape_repo(link,repo,scraped)
    print(filescrape)

if argv[-1].startswith("-"):
    parse = list(argv[-1][1:])
    if "s" in parse:
        parsenum = ''.join(char for char in parse if char.isdigit())
        count = int(parsenum if parsenum != '' else '0')
        print(count)
        update_repos()
for url in scraped.readlines():
        filescrape[os.path.basename(url.strip("/"))] = os.path.basename(url.strip("/"))
        
if argv[1] == "search":
    for name,url in filescrape.items():
        print(f'${name} ({url})')
scraped.close()