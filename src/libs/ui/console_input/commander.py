from .parser import ParserResult
from .scenes.scene_base import SceneBase

from .scenes import Download, Play, List, Help

class CommanderResult:
    def __init__(self, parsed: ParserResult, command, error: str) -> None:
        self.__parsed = parsed
        self.__error = error
        self.__command = command
    
    def getParsed(self) -> ParserResult:
        return self.__parsed
    def getError(self) -> str:
        return self.__error
    def getCommand(self):
        return self.__command
    
    def isError(self) -> bool:
        return self.__error != ''


class Commander:
    COMMANDS = {
        'download': Download,
        'play': Play,
        'list': List,
        'help': Help
    }
    
    def handle(self, parsed: ParserResult) -> CommanderResult:
        error: str = ''
        command = SceneBase
        
        try:
            command_name: str = self._get_command(parsed.getCommandName())
            command = Commander.COMMANDS.get(command_name)
        except Exception as e:
            error = str(e)
        
        return CommanderResult(parsed, command, error)
    
    
    def _get_command(self, command_name: str) -> str:
        if command_name.lower() in list(self.COMMANDS.keys()):
            return command_name
        raise KeyError('doesn\'t exists typed command! For help type \'help\'')