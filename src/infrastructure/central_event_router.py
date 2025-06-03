from typing import Any, Callable, Dict

from domain.emiter import BaseEmitter
from domain.event_router import BaseEventRouter


class SyncCentralEventRouter(BaseEventRouter):
    def __init__(self) -> None:
        super().__init__()
        self._registery: Dict[str, BaseEmitter] = {}

    def register_emiter(self, component_name: str, emitter: BaseEmitter) -> None:
        self._registery[component_name] = emitter

    def connect(
        self, component_name: str, event: str, target_handler: Callable[..., Any]
    ) -> None:
        emitter = self._registery.get(component_name, None)
        if not emitter:
            raise ValueError(f"Emitter '{component_name}' не зарегистрирован.")
        emitter.subscribe(event, target_handler)
