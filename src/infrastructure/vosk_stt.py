from typing import Any

from domain.stt import STT


class VoskSTT(STT):
    def __init__(self, model: Any) -> None:
        super().__init__(model)

    def main_loop(self) -> None:
        raise NotImplementedError("main_loop from VoskSTT")
