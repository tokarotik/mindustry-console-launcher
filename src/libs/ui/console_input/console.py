from .parser import Parser, ParserResult
from .commander import Commander, CommanderResult

class Console:
    def __init__(self) -> None:
        self.parser: Parser = Parser()
        self.commander: Commander = Commander()
    
    def run(self) -> None:
        while True:
            try: inp: str = input('>>')
            except KeyboardInterrupt:
                print()
                break
            if inp.lower() == 'exit' or inp.lower() == 'stop':
                break
            
            self._handle_input(inp)
    
    def _handle_input(self, inp: str) -> None:
        parsed: ParserResult = self.parser.parse(inp)
        if parsed.isError(): return
        
        command: CommanderResult = self.commander.handle(parsed)
        if command.isError():
            print(f'err: {command.getError()}')
            return
        