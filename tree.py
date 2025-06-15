class Node:
    def __init__(self, data, is_question=False):
        self.data = data
        self.is_question = is_question  # distinguishes between question node and guess/answer node (leaf)
        self.yes = None
        self.no = None

class Tree:
    def __init__(self, root):
        self.root = root

    def play(self):
        print("Think of a film, and I'll try to guess it!")
        self.root = self._ask_questions(self.root)

    def _ask_questions(self, node):
        if not node.is_question:
            answer = input(f"Is your film {node.data}? (yes/no): ").strip().lower()
            if answer == "yes":
                print(f"You were thinking of {node.data}!")
                return node 
            else:
                return self._learn(node)
        else:
            answer = input(f"{node.data} (yes/no): ").strip().lower()
            if answer == "yes":
                node.yes = self._ask_questions(node.yes)
            else:
                node.no = self._ask_questions(node.no)
            return node
        
    def _learn(self, incorrect_node):
        correct = input("I'm stumped! Which film are you thinking of? ").strip()
        question = input(f"Help me out with a yes/no question to distinguish {correct} from {incorrect_node.data}: ").strip()
        answer = input(f"For {correct}, what is the answer? (yes/no): ").strip().lower()

        new_question = Node(question, is_question=True)
        new_movie = Node(correct)

        if answer == "yes":
            new_question.yes = new_movie
            new_question.no = incorrect_node
        else:
            new_question.no = new_movie
            new_question.yes = incorrect_node

        print("Got it! I'll remember that for next time.")
        return new_question