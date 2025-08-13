from stack import Stack

class BrowserHistory:
    def __init__(self):
        self.back_stack = Stack()
        self.forward_stack = Stack()
        self.current_page = None
    
    def visit(self, url):
        if self.current_page :
            self.back_stack.push(self.current_page)
        self.current_page = url
        self.forward_stack = Stack() #清空 forward
        print(f"訪問:{url}")
    
    def back(self):
        if self.back_stack.isempty():
            print("沒有上一頁")
            return
        self.forward_stack.push(self.current_page)
        self.current_page = self.back_stack.pop()
        print(f"回到:{self.current_page}")

    def forward(self):
        if self.forward_stack.isempty():
            print("沒有下一頁")
            return
        self.back_stack.push(self.current_page)
        self.current_page = self.forward_stack.pop()
        print(f"前進到:{self.current_page}")

if __name__ == "__main__":

    bh = BrowserHistory()
    bh.visit("google.com")
    bh.visit("youtube.com")
    bh.visit("github.com")
    bh.back()
    bh.back()
    bh.forward()
    
