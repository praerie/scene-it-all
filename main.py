from tree import Tree, Node
from io_utils import load_tree, save_tree

def print_tree(node, indent=""):
    if not node:
        return
    prefix = "Q: " if node.is_question else "🎬 "  # emoji = marker for displaying film title 
    print(f"{indent}{prefix}{node.data}")
    print_tree(node.yes, indent + "  ")
    print_tree(node.no, indent + "  ")

def main():
    print("🎬 Welcome to Scene It All!")

    tree = Tree(load_tree())

    while True:
        command = input("\nType a command (play, print, save, quit): ").strip().lower()
        if command == "play":
            tree.play()
        elif command == "print":
            print_tree(tree.root)
        elif command == "save":
            save_tree(tree.root)
            print("Tree saved!")
        elif command == "quit":
            break
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()
