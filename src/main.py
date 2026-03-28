from src.libs.ui.console_input.console import Console

print("""Hello User,
    You have launched the unofficial Mindustry launcher.
    To exit the launcher type 'exit' or 'stop'.
    Or use Ctr+C(Windows) or Ctr+Z(Linux-like systems).

    gl bro <:
    
Made by HalvaNyashka""")

console = Console()
console.run()
"""exit()


import os
import json
from pathlib import Path

from .releases.responser import Responser
from .releases.parser import Parser

author = 'anuken'
repo = 'Mindustry'

responser = Responser(Responser.get_github_url(author, repo), 1)
parsed = responser.get_parsed()

assets = ['Mindustry.jar', 'desktop-release.jar']
for i in reversed(parsed):    
    if set(assets) & parsed[i]['assets'].keys():
        print("(Avaible)     ", end = '')
    else:
        print("(Not Avaible) ", end = '')
    
    print(parsed[i]['name'], end = '')
    print(f'\t Version - {i}')
    
    
version = Parser.get_version_number(input("input what version you want download(e.g.: 156, v74, v155.2):"))
folder_versions = Path('.').absolute() / Path('versions')
file = Path(folder_versions / Path('mindustry_' + str(version) + '.jar')).absolute()

if not os.path.isdir(folder_versions):
    os.mkdir(folder_versions)
responser.download(
    version, 
    file,
    assets
)"""