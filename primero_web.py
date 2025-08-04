class WebBrowser:
    def __init__(self):
        self.back_stack = []
        self.forward_stack = []

    def load_page(self, url):
        if self.back_stack:
            self.forward_stack.clear()
        self.back_stack.append(url)

    def go_back(self):
        if len(self.back_stack) > 1:
            self.forward_stack.append(self.back_stack.pop())
            return self.back_stack[-1]
        return None

    def go_forward(self):
        if self.forward_stack:
            page = self.forward_stack.pop()
            self.back_stack.append(page)
            return page
        return None
