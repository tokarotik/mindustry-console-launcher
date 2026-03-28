
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
        self.splitted: list[str] = []
        self.lenght: int = -1
        self.command_name: str = ''
        
        self.is_error: bool = False
        
        self.cur_index: int = 0
        
    def parse(self, inp: str) -> ParserResult:
        self._splitted(inp)
        self._lenght()
        self._command_name()
        
        self._check_errors()
        
        return ParserResult(
            self.command_name,
            self._get_from_splitted(''),
            self._get_from_splitted(''),
            self.is_error
        )
    
    def _splitted(self, inp: str) -> None:
        self.splitted = self._clear_splitted(inp.split())
    
    def _lenght(self) -> None:
        self.lenght = len(self.splitted)
    
    def _command_name(self) -> None:
        self.cur_index = 0
        self.command_name = self._get_from_splitted()
    
    def _check_errors(self) -> None:
        if self.command_name == None: self.is_error = True
        if self.lenght < 1 or self.lenght > 3: self.is_error = True
    
    def _clear_splitted(self, splitted: list[str]) -> list[str]:
        return [i for i in splitted if i != '' or i != ' ']
    
    def _get_from_splitted(self, default = None):
        output = None
        try: output = self.splitted[self.cur_index]
        except IndexError: output = default
        
        self.cur_index += 1
        return output