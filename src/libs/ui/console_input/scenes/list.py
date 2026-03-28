from ....releases.responser import Responser

from .scene_base import  SceneBase

class List(SceneBase):
    def __init__(self, responser: Responser) -> None:
        super().__init__(responser)