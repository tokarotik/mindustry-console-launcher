from ....releases.responser import Responser

from ..parser import ParserResult

class SceneBase:
    def __init__(self, responser: Responser, parsed: ParserResult) -> None:
        self.responser: Responser = responser
        self.parsed: ParserResult = parsed
    
    def run(self) -> None: pass
    
    @staticmethod
    def check_args(self, command_name: str, flag: str, additional_argument: str) -> bool: 
        return False