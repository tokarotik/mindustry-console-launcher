from ....releases.responser import Responser

class SceneBase:
    def __init__(self, responser: Responser) -> None:
        self.responser: Responser = responser
    
    def run(self) -> None: pass