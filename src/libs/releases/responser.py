import requests
from pathlib import Path

from .parser import Parser

class Responser:
    def __init__(self, url: str, timeout: int = 5) -> None:
        self.url: str = url
        self.timeout: int = timeout
        
        self.__old_response: list = []
        self.__old_parsed: dict = {}
    
    def request(self) -> list:
        if self.__old_response == None or self.__old_response == []:
            releases = []
            page = 1

            while True:
                response = requests.get(self.url, params={"page": page, "per_page": 100}, timeout = (5,self.timeout))
                
                data = response.json()
                if not data:
                    break
                if isinstance(data, dict):
                    if data.get('message') != None and data.get('documentation_url') != None:
                        break
                
                releases.extend(data)
                page += 1
            self.__old_response = releases
        return self.__old_response
        
    def get_parsed(self) -> dict:
        if self.__old_parsed == None or self.__old_parsed == {}:
            self.request()
            parser = Parser(self.__old_response)
            self.__old_parsed = parser.parse()
        return self.__old_parsed
    
    def download(self, version: float | int, filepath: Path, avaible_executables: list[str]) -> None:
        parsed = self.get_parsed()
        game_config = parsed.get(version)
        
        if not isinstance(game_config, dict): 
            raise KeyError(f"game version {version} was not found")
        assets = game_config.get('assets')
        
        if not isinstance(assets, dict): 
            raise KeyError("game config doesn't have assets urls")
        
        if not (set(avaible_executables) & assets.keys()):
            raise KeyError("game config doesn't contain avaible executables")
        
        url = ''
        for i in assets:
            if i in avaible_executables:
                url = assets[i]
                break
        
        Responser._download(url, filepath)
    
    @staticmethod
    def _download(url: str, filepath: Path) -> None:
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            
            with open(filepath, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
        
    
    @staticmethod
    def get_github_url(owner: str, repo: str) -> str:
        return f"https://api.github.com/repos/{owner}/{repo}/releases"