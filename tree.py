# Node represents a single point in the decision tree.
class Node:
    def __init__(self, data, is_question=False):
        self.data = data  # The text content: either a question or a film title
        self.is_question = is_question  # True if the node is a question, False if it's a film guess
        self.yes = None  # Reference to the next node if the answer is "yes"
        self.no = None   # Reference to the next node if the answer is "no"

# Tree represents the entire decision tree for the guessing game.
class Tree:
    def __init__(self, root):
        self.root = root  # The root node of the tree

    def play(self):
        print("Think of a film, and I'll try to guess it!")
        # Start asking questions from the root and update it in case learning occurs
        self.root = self._ask_questions(self.root)

    def _ask_questions(self, node):
        # Base case: if node is a guess (leaf), ask if it's correct
        if not node.is_question:
            if self._get_yes_no_input(f"Is your film {node.data}?"):
                print(f"⭐ Guessed it! You were thinking of {node.data}!")
                return node  # Keep the node unchanged if correct
            else:
                return self._learn(node)  # Learn a new film if the guess was wrong
        else:
            # Recursive case: ask the current question and follow the branch based on answer
            if self._get_yes_no_input(node.data):
                node.yes = self._ask_questions(node.yes)  # Traverse "yes" branch
            else:
                node.no = self._ask_questions(node.no)    # Traverse "no" branch
            return node

    def _learn(self, incorrect_node):
        # Ask the user for the correct film
        correct = input("❔ I'm stumped! Which film are you thinking of? ").strip()
        # Ask for a yes/no question that distinguishes the new film from the incorrect guess
        question = input(f"Help me out with a yes/no question to distinguish {correct} from {incorrect_node.data}: ").strip()
        # Ask for the correct answer to the question for the new film
        answer = input(f"For {correct}, what is the answer? (yes/no): ").strip().lower()

        # Create a new question node
        new_question = Node(question, is_question=True)
        # Create a node for the correct film
        new_movie = Node(correct)

        # Attach the new nodes to the question based on the answer
        if answer == "yes":
            new_question.yes = new_movie
            new_question.no = incorrect_node
        else:
            new_question.no = new_movie
            new_question.yes = incorrect_node

        print("Got it! I'll remember that for next time.")
        return new_question  # Return the new question node to replace the old guess

    def _get_yes_no_input(self, prompt):
        # Continuously prompt the user until a valid yes/no answer is given
        while True:
            answer = input(f"{prompt} (yes/no): ").strip().lower()
            if answer in ("yes", "y"):
                return True
            elif answer in ("no", "n"):
                return False
            else:
                print("Please enter 'yes' or 'no'.")
