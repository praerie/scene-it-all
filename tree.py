class Node:
    def __init__(self, data, is_question=False):
        self.data = data
        self.is_question = is_question  # distinguishes between question node and guess/answer node (leaf)
        self.yes = None
        self.no = None