import tkinter as tk
import random

# Constants
WIDTH = 600
HEIGHT = 400
DELAY = 100
GRID_SIZE = 20
SNAKE_COLOR = "green"
FOOD_COLOR = "red"

class SnakeGame:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()

        self.snake = [(WIDTH/2, HEIGHT/2)]
        self.direction = "Right"
        self.food = self.create_food()
        self.score = 0
        self.game_over = False

        self.master.bind("<Key>", self.change_direction)
        
        self.restart_button = tk.Button(self.master, text="Restart", command=self.restart_game)
        self.restart_button.pack()

        self.update()

    def update(self):
        if not self.game_over:
            self.move_snake()
            self.check_collision()
            self.check_boundary()
            self.check_eat_food()
            self.draw_snake()
            self.draw_food()
            self.master.after(DELAY, self.update)
        else:
            self.canvas.create_text(WIDTH/2, HEIGHT/2, text=f"Game Over! Score: {self.score}", fill="white", font=("Arial", 24))
            self.restart_button.pack()

    def draw_snake(self):
        self.canvas.delete("snake")
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x+GRID_SIZE, y+GRID_SIZE, fill=SNAKE_COLOR, tags="snake")

    def move_snake(self):
        head_x, head_y = self.snake[0]
        if self.direction == "Up":
            head_y -= GRID_SIZE
        elif self.direction == "Down":
            head_y += GRID_SIZE
        elif self.direction == "Left":
            head_x -= GRID_SIZE
        elif self.direction == "Right":
            head_x += GRID_SIZE

        new_head = (head_x, head_y)
        self.snake = [new_head] + self.snake[:-1]

    def change_direction(self, event):
        if event.keysym in ["Up", "Down", "Left", "Right"]:
            if (event.keysym == "Up" and self.direction != "Down") or \
               (event.keysym == "Down" and self.direction != "Up") or \
               (event.keysym == "Left" and self.direction != "Right") or \
               (event.keysym == "Right" and self.direction != "Left"):
                self.direction = event.keysym

    def check_collision(self):
        head = self.snake[0]
        if head in self.snake[1:]:
            self.game_over = True

    def check_boundary(self):
        head_x, head_y = self.snake[0]
        if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
            self.game_over = True

    def create_food(self):
        while True:
            x = random.randint(0, int(WIDTH/GRID_SIZE) - 1) * GRID_SIZE
            y = random.randint(0, int(HEIGHT/GRID_SIZE) - 1) * GRID_SIZE
            if (x, y) not in self.snake:
                return (x, y)

    def draw_food(self):
        self.canvas.delete("food")
        x, y = self.food
        self.canvas.create_oval(x, y, x+GRID_SIZE, y+GRID_SIZE, fill=FOOD_COLOR, tags="food")

    def check_eat_food(self):
        if self.snake[0] == self.food:
            self.snake.append(self.snake[-1])
            self.food = self.create_food()
            self.score += 1

    def restart_game(self):
        self.snake = [(WIDTH/2, HEIGHT/2)]
        self.direction = "Right"
        self.food = self.create_food()
        self.score = 0
        self.game_over = False
        self.update()

def main():
    root = tk.Tk()
    root.title("Snake Game")
    game = SnakeGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
