
class ParserResult:
    def __init__(self, command_name: str, flag: str, additional_argument: str, is_error: bool) -> None:
        self.__command_name: str = command_name
        self.__flag: str = flag
        self.__additional_argument: str = additional_argument
        self.__is_error: bool = is_error
        
    def getCommandName(self) -> str:
        return self.__command_name
    def getFlag(self) -> str:
        return self.__flag
    def getAdditionalArgument(self) -> str:
        return self.__additional_argument
    def isError(self) -> bool:
        return self.__is_error

class Parser:
    def __init__(self) -> None:
        pass
    
    def parse(self, inp: str) -> ParserResult:
        splitted: list[str] = self._clear_splitted(inp.split())
        lenght: int = len(splitted)
        
        command_name = self._get_from_list(splitted, 0)
        is_error = False
        if command_name == None: is_error = True
        if lenght < 1 or lenght > 3: is_error = True
        
        return ParserResult(
            command_name,
            self._get_from_list(splitted,1, ''),
            self._get_from_list(splitted, 2, ''),
            is_error
        )
    
    def _clear_splitted(self, splitted: list[str]) -> list[str]:
        return [i for i in splitted if i != '' or i != ' ']
    
    def _get_from_list(self, ls: list, ind: int, default = None):
        try: return ls[ind]
        except IndexError: return default