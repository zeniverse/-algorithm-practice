class Node(object):
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = self.current = Node(val=homepage)

    def visit(self, url: str) -> None:
        self.current.next = Node(val=url, prev=self.current)
        self.current = self.current.next
        return None

    def back(self, steps: int) -> str:
        while steps > 0 and self.current.prev != None:
            steps -= 1
            self.current = self.curret.prev
        return self.current.val

    def forward(self, steps: int) -> str:
        while steps > 0 and self.current.next != None:
            steps -= 1
            self.current = self.current.next
        return self.current.val