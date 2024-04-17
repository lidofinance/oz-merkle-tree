from abc import ABC, abstractmethod
from typing import Iterable


class MerkleTree(ABC):
    """Merkle Tree interface"""

    @property
    @abstractmethod
    def root(self) -> bytes: ...

    @abstractmethod
    def find(self, leaf: bytes) -> int: ...

    @abstractmethod
    def get_proof(self, index: int) -> Iterable[bytes]: ...

    @classmethod
    @abstractmethod
    def verify(cls, root: bytes, leaf: bytes, proof: Iterable[bytes]) -> bool: ...

    @classmethod
    @abstractmethod
    def __hash_leaf__(cls, leaf: bytes) -> bytes: ...

    @classmethod
    @abstractmethod
    def __hash_node__(cls, lhs: bytes, rhs: bytes) -> bytes: ...
