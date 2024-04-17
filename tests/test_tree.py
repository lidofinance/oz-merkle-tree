from typing import TypeAlias

import pytest

from oz_merkle_tree import StandardMerkleTree

Tree: TypeAlias = StandardMerkleTree[list[str | int]]


@pytest.fixture
def tree() -> Tree:
    return StandardMerkleTree(
        [
            ["0x1111111111111111111111111111111111111111", 5000000000000000000],
            ["0x2222222222222222222222222222222222222222", 2500000000000000000],
            ["0x3333333333333333333333333333333333333333", 3500000000000000000],
            ["0x4444444444444444444444444444444444444444", 4500000000000000000],
            ["0x5555555555555555555555555555555555555555", 5500000000000000000],
        ],
        ("address", "uint256"),
    )


def test_creating_standard_tree(tree: Tree):
    assert tree.root.hex() == "8c6838966085373a17174cdbcad894c8c682dd22c4f5cb7d57284d3d447d4cc8"


def test_create_and_verify_proof(tree: Tree):
    for v in tree.values:
        leaf = tree.leaf(v["value"])
        assert tree.verify(tree.root, leaf, tree.get_proof(tree.find(leaf)))


def test_dump_and_load(tree: Tree):
    dump = tree.dump()
    assert Tree.load(dump).root == tree.root
