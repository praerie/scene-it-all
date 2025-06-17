from tree import Tree, Node 
from io_utils import load_tree, save_tree 

# Recursive function to display the tree structure in a readable format
def print_tree(node, indent=""):
    if not node:
        return  # Base case: stop if the node is None
    prefix = "Q: " if node.is_question else "🎬 "  # Use emoji or 'Q:' to distinguish questions from film titles
    print(f"{indent}{prefix}{node.data}")  # Print the current node with indentation for tree structure
    print_tree(node.yes, indent + "  ")  # Recursively print the 'yes' branch with increased indent
    print_tree(node.no, indent + "  ")  # Recursively print the 'no' branch with increased indent

# Main function that drives the command interface
def main():
    print("🎬 Welcome to Scene It All!") 

    tree = Tree(load_tree())  # Load the saved decision tree into a Tree object

    # Command loop to handle user interactions
    while True:
        # Prompt user for a command and normalize input
        command = input("\nType a command (play, print, save, quit): ").strip().lower()

        if command == "play":
            tree.play()  # Begin the guessing game
        elif command == "print":
            print_tree(tree.root)  # Show the current structure of the tree
        elif command == "save":
            save_tree(tree.root)  # Save the current tree state to file
            print("Tree saved!")  
        elif command == "quit":
            break  # Exit the loop and end the program
        else:
            print("Unknown command.")  # Handle unrecognized commands

if __name__ == "__main__":
    main()
