import json
from tree import Node


def save_tree(node, filename="data/tree.json"):
    def to_dict(node):
        if not node:
            return None
        return {
            "data": node.data,
            "is_question": node.is_question,
            "yes": to_dict(node.yes),
            "no": to_dict(node.no)
        }
    
    with open(filename, "w") as f:
        json.dump(to_dict(node), f, indent=2)

def load_tree(filename="data/tree.json"):
    def from_dict(data):
        if not data:
            return None
        node = Node(data["data"], data["is_question"])
        node.yes = from_dict(data["yes"])
        node.no = from_dict(data["no"])
        return node

    try:
        with open(filename, "r") as f:
            return from_dict(json.load(f))
    except FileNotFoundError:
        return Node("Kiki's Delivery Service")

