import pytest

from domain.emiter import BaseEmitter
from domain.event_router import BaseEventRouter
from infrastructure.central_event_router import SyncCentralEventRouter
from infrastructure.event_emiter import SyncEventEmitter


class SenderModule:
    def __init__(self, emitter: BaseEmitter) -> None:
        self.emitter = emitter

    def main_loop(self) -> None: ...


class GetterModule:
    def __init__(self, emitter: BaseEmitter) -> None: ...
    def test(self) -> None: ...


def test_event_hadler() -> None:
    test_sender = SenderModule(SyncEventEmitter())
    test_getter = GetterModule(SyncEventEmitter())
    router: BaseEventRouter = SyncCentralEventRouter()
    router.register_emiter("Test", test_sender.emitter)

    with pytest.raises(ValueError):
        router.connect(
            component_name="Test2", event="test2", target_handler=test_getter.test
        )
    with pytest.raises(ValueError):
        router.connect(
            component_name="Test", event="test2", target_handler=test_getter.test
        )
    test_sender.emitter.create_event("test2")
    test_sender.emitter.emit("test2")
