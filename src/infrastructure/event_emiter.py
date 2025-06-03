from collections import defaultdict
from typing import Any, Callable, DefaultDict

from domain.emiter import BaseEmitter


class SyncEventEmitter(BaseEmitter):
    def __init__(self) -> None:
        super().__init__()
        self._listeners: DefaultDict[str, list[Callable[..., Any]]] = defaultdict(list)
        self._events: list[str] = []

    def emit(self, event: str, *args: Any, **kwargs: Any) -> None:
        if event not in self._listeners:
            raise ValueError(f"Event '{event}' не зарегистрирован.")
        for cb in self._listeners.get(event, []):
            cb(*args, **kwargs)

    def subscribe(self, event: str, handler: Callable[..., Any]) -> None:
        if event not in self._events:
            raise ValueError(f"Event '{event}' не зарегистрирован.")
        self._listeners[event].append(handler)

    def create_event(self, event_name: str) -> None:
        self._events.append(event_name)

    @property
    def events(self) -> list[str]:
        return self._events
