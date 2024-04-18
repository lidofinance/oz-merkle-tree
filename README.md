### `oz-merkle-tree`

**A Python library to generate Merkle trees and Merkle proofs.**

This is project is compatible with the [OpenZeppelin StandardMerkleTree](https://github.com/OpenZeppelin/merkle-tree).

#### Usage

**Building a tree**

```python
import json

from oz_merkle_tree import StandardMerkleTree

tree = StandardMerkleTree(
    [
        ["0x1111111111111111111111111111111111111111", 5000000000000000000],
        ["0x2222222222222222222222222222222222222222", 2500000000000000000],
    ],
    ("address", "uint256"),
)

print(f"Merkle root: {tree.root}")

def default(o):
    if isinstance(o, bytes):
        return f"0x{o.hex()}"
    assert False

with open("tree.json", "w", encoding="utf-8") as f:
    json.dump(tree.dump(), f, default=default)
```

**Obtaining a proof**

```python
from oz_merkle_tree import StandardMerkleTree

tree = StandardMerkleTree(
    [
        ["0x1111111111111111111111111111111111111111", 5000000000000000000],
        ["0x2222222222222222222222222222222222222222", 2500000000000000000],
    ],
    ("address", "uint256"),
)

for v in tree.values:
    proof = tree.get_proof(v["treeIndex"])
    print([f"0x{p.hex()}" for p in proof])
```

#### Standard Merkle Trees

This library works on "standard" merkle trees designed for Ethereum smart contracts. We have defined them with a few
characteristics that make them secure and good for on-chain verification.

- The tree is shaped as a complete binary tree.
- The leaves are sorted.
- The leaves are the result of ABI encoding a series of values.
- The hash used is Keccak256.
- The leaves are double-hashed to prevent second preimage attacks.

