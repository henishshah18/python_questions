from collections import deque

class BrowserHistory:
    def __init__(self, max_size=5):
        self.history = deque()
        self.forward_stack = deque()
        self.max_size = max_size

    def visit(self, url):
        if len(self.history) == self.max_size:
            removed = self.history.popleft()
            print(f"Removed oldest page: {removed}")
        self.history.append(url)
        self.forward_stack.clear()
        print(f"Visited: {url}")
        self.print_state()

    def go_back(self):
        if len(self.history) > 1:
            last = self.history.pop()
            self.forward_stack.append(last)
            print(f"Back to: {self.history[-1]}")
        else:
            print("Cannot go back.")
        self.print_state()

    def go_forward(self):
        if self.forward_stack:
            restored = self.forward_stack.pop()
            self.history.append(restored)
            print(f"Forward to: {restored}")
        else:
            print("No forward history.")
        self.print_state()

    def print_state(self):
        print("History:", list(self.history))
        print("Forward Stack:", list(self.forward_stack))
        print("-" * 40)

# Sample Usage
bh = BrowserHistory()

bh.visit("google.com")
bh.visit("github.com")
bh.visit("stackoverflow.com")
bh.visit("openai.com")
bh.visit("reddit.com")
bh.visit("wikipedia.org")

bh.go_back() 
bh.go_back()

bh.go_forward()

bh.visit("news.ycombinator.com")
