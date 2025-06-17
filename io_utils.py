import json
from tree import Node  # Import the Node class to rebuild the tree from file data

# Saves the decision tree to a JSON file
def save_tree(node, filename="data/tree.json"):
    # Helper function to convert a Node into a serializable dictionary
    def to_dict(node):
        if not node:
            return None
        return {
            "data": node.data,  # Question or movie title
            "is_question": node.is_question,  # Flag to determine node type
            "yes": to_dict(node.yes),  # Recursively convert the "yes" branch
            "no": to_dict(node.no)     # Recursively convert the "no" branch
        }
    
    # Open the file and write the tree structure as a JSON object
    with open(filename, "w") as f:
        json.dump(to_dict(node), f, indent=2)  # Pretty-printed for readability

# Loads the decision tree from a JSON file
def load_tree(filename="data/tree.json"):
    # Helper function to recursively rebuild the Node structure from a dictionary
    def from_dict(data):
        if not data:
            return None
        node = Node(data["data"], data["is_question"])  # Create the node from dictionary values
        node.yes = from_dict(data["yes"])  # Rebuild the "yes" branch
        node.no = from_dict(data["no"])    # Rebuild the "no" branch
        return node

    try:
        # Attempt to load the tree data from file
        with open(filename, "r") as f:
            return from_dict(json.load(f))
    except FileNotFoundError:
        # Fallback: start with a default guess if no file exists yet
        return Node("Kiki's Delivery Service")
