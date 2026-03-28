from .parser import Parser, ParserResult
from .commander import Commander, CommanderResult

class Console:
    def __init__(self) -> None:
        self.parser = Parser()
    
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
        
        