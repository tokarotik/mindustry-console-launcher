from ....releases.responser import Responser

from .scene_base import  SceneBase

class Download(SceneBase):
    def __init__(self, responser: Responser) -> None:
        super().__init__(responser)