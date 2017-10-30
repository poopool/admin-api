from typing import Dict, Any, TypeVar, Mapping, List

__all__ = ...  # type: str

class BaseTransport:
    def __init__(self, extra: Mapping[Any, Any] = ...) -> None: ...
    def get_extra_info(self, name: Any, default: Any = ...) -> Any: ...
    def is_closing(self) -> bool: ...
    def close(self) -> None: ...

class ReadTransport(BaseTransport):
    def pause_reading(self) -> None: ...
    def resume_reading(self) -> None: ...

class WriteTransport(BaseTransport):
    def set_write_buffer_limits(
        self, high: int = ..., low: int = ...
    ) -> None: ...
    def get_write_buffer_size(self) -> int: ...
    def write(self, data: Any) -> None: ...
    def writelines(self, list_of_data: List[Any]): ...
    def write_eof(self) -> None: ...
    def can_write_eof(self) -> bool: ...
    def abort(self) -> None: ...

class Transport(ReadTransport, WriteTransport): ...

class DatagramTransport(BaseTransport):
    def sendto(self, data: Any, addr: str = ...) -> None: ...
    def abort(self) -> None: ...

class SubprocessTransport(BaseTransport):
    def get_pid(self) -> int: ...
    def get_returncode(self) -> int: ...
    def get_pipe_transport(self, fd: int) -> BaseTransport: ...
    def send_signal(self, signal: int) -> int: ...
    def terminate(self) -> None: ...
    def kill(self) -> None: ...
