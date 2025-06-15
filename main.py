from io_utils import load_tree, save_tree
from tree import Node

def print_tree(node, indent=""):
    if not node:
        return
    prefix = "Q: " if node.is_question else "🎬 "  # emoji = visual cue for movies
    print(f"{indent}{prefix}{node.data}")
    print_tree(node.yes, indent + "  ")
    print_tree(node.no, indent + "  ")

def main():
    print("🎬 Welcome to Scene It All!")
    root = load_tree()

    while True:
        command = input("\nType a command (play, print, save, quit): ").strip().lower()
        if command == "print":
            print_tree(root)
        elif command == "save":
            save_tree(root)
            print("Saved!")
        elif command == "quit":
            break
        elif command == "play":
            print("Coming soon!")
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()
