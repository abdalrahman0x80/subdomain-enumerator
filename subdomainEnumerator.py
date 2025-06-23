import argparse
import requests
class SubdomainEnumerator:
    def __init__(self, target, wordlist):
        self.target = target
        self.wordlist = wordlist
        self.session = requests.Session()
    def enumerate(self):
        with open(self.wordlist, 'r') as file:
            for line in file:
                subdomain = line.strip()
                if not subdomain:
                    continue
                url = f"https://{subdomain}.{self.target}"
                try:
                    response = self.session.get(url, timeout=5)
                    if response.status_code == 200:
                        print(f"Found subdomain: {url}")
                except requests.RequestException as e:
                    continue
class ArgumentParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Subdomain Enumerator")
        self.parser.add_argument("target", help="Target domain to enumerate subdomains for")
        self.parser.add_argument("wordlist", help="Path to the wordlist file containing subdomains")
    def parse_args(self):
        return self.parser.parse_args()
    
args = ArgumentParser().parse_args()
subdomain = SubdomainEnumerator(args.target, args.wordlist)
subdomain.enumerate()
