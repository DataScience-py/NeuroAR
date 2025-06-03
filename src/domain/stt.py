from abc import ABC, abstractmethod
from typing import Any


class STT(ABC):
    @abstractmethod
    def __init__(self, model: Any) -> None:
        self.model = model

    @abstractmethod
    def main_loop(
        self,
    ) -> None: ...
