class Snake:
    def __init__(self, block_size, initial_x, initial_y):
        self.block_size = block_size
        self.snake_body = [
            (initial_x, initial_y),
            (initial_x - block_size, initial_y),
            (initial_x - 2 * block_size, initial_y)
        ]
        self.direction = "right"
        self.head = self.snake_body[0]

    def move(self):
        if self.direction == "up":
            new_head = (self.head[0], self.head[1] - self.block_size)
        elif self.direction == "down":
            new_head = (self.head[0], self.head[1] + self.block_size)
        elif self.direction == "left":
            new_head = (self.head[0] - self.block_size, self.head[1])
        elif self.direction == "right":
            new_head = (self.head[0] + self.block_size, self.head[1])

        self.snake_body.insert(0, new_head)
        self.head = self.snake_body[0]

    def remove(self):
        if len(self.snake_body) > 0:
            self.snake_body.pop()