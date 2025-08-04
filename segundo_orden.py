class Queue:
    def __init__(self):
        self.queue = []

    def add_customer(self, customer_id):
        self.queue.append(customer_id)

    def serve_customer(self):
        if self.queue:
            return self.queue.pop(0)
        return None
