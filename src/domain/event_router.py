from abc import ABC, abstractmethod
from typing import Any, Callable

from domain.emiter import BaseEmitter


class BaseEventRouter(ABC):
    def __init__(self) -> None: ...

    @abstractmethod
    def register_emiter(self, component_name: str, emitter: BaseEmitter) -> None: ...

    @abstractmethod
    def connect(
        self, component_name: str, event: str, target_handler: Callable[..., Any]
    ) -> None: ...
