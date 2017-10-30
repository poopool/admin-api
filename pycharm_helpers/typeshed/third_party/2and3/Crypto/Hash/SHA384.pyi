# Stubs for Crypto.Hash.SHA384 (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from Crypto.Hash.hashalgo import HashAlgo

class SHA384Hash(HashAlgo):
    oid = ...  # type: Any
    digest_size = ...  # type: int
    block_size = ...  # type: int
    def __init__(self, data: Optional[Any] = ...) -> None: ...
    def new(self, data: Optional[Any] = ...): ...

def new(data: Optional[Any] = ...): ...

digest_size = ...  # type: Any
