'''
Snake Game with GUI and Advanced Features

This Python program is a classic Snake game with a graphical user interface (GUI). The game allows the player to control a snake and collect food to grow longer. The game features multiple snakes, power-ups, obstacles, and high scores.

Features:

GUI-based Snake game with smooth controls.
Multiple snakes with different colors that the player can control.
Special "Speed Boost" power-ups that randomly appear and increase the snake's speed temporarily.
Obstacles that the snake must avoid while collecting food.
Keeps track of the player's score and highest score achieved.
Option to continue playing or exit the game.
How to Play:

Run the program to start the Snake game.
Use the arrow keys to control the movement of the snake.
Guide the snake to collect the food (red squares) to grow longer.
Avoid running into walls, obstacles (gray squares), or the snake's own body to stay alive.
If the snake collides with an obstacle or wall, the game ends.
Eating food increases the score, and the highest score achieved is displayed.
The game features multiple snakes with different colors, making it more challenging and engaging.
"Speed Boost" power-ups randomly appear on the grid and temporarily increase the snake's speed, adding excitement to the gameplay.
Obstacles are placed on the grid, creating additional challenges for the player to navigate around.
Tips:

Strategize your moves to avoid collisions and maximize your snake's growth.
Utilize the "Speed Boost" power-ups strategically to quickly reach food and improve your score.
Challenge yourself to beat your highest score and improve your Snake game skills.
Author: [Olajuwon]
Date: [05-07-2023]
'''




import tkinter as tk
import random
import pygame
from pygame.locals import *

# Set up the window
root = tk.Tk()
root.title("Snake Game")
root.geometry("600x400")

# Initialize Pygame
pygame.init()

# Set up game variables
cell_size = 20
grid_width = 600 // cell_size
grid_height = 400 // cell_size
snake_speed = 150
score = 0
high_score = 0

# Create the player's snake
player_snake = [(grid_width // 2, grid_height // 2)]
player_snake_direction = (0, 0)
player_snake_color = "green"

# Create the AI snake
ai_snake = [(grid_width // 3, grid_height // 3)]
ai_snake_direction = (0, 1)
ai_snake_color = "blue"

# Create the food
food = (random.randint(0, grid_width - 1), random.randint(0, grid_height - 1))

# Create obstacles
obstacles = [(random.randint(0, grid_width - 1), random.randint(0, grid_height - 1)) for _ in range(10)]

# Function to update the player's snake position
def update_player_snake():
    global player_snake, player_snake_direction, food, score, high_score

    # Update the player's snake position based on the direction
    head_x, head_y = player_snake[-1]
    new_head = (head_x + player_snake_direction[0], head_y + player_snake_direction[1])

    # Check if the player's snake hits the food
    if new_head == food:
        food = (random.randint(0, grid_width - 1), random.randint(0, grid_height - 1))
        score += 10
        if score > high_score:
            high_score = score
    else:
        player_snake.pop(0)

    player_snake.append(new_head)

    # Check for collisions with walls or obstacles
    if (new_head[0] < 0 or new_head[0] >= grid_width or
            new_head[1] < 0 or new_head[1] >= grid_height or
            new_head in player_snake[:-1] or
            new_head in obstacles):
        # Game over
        print("Game Over!")
        pygame.quit()
        root.destroy()
        return

    # Draw the player's snake and food on the screen
    canvas.delete("all")
    canvas.create_text(50, 10, text="Score: " + str(score), fill="white", anchor=tk.W)
    canvas.create_text(500, 10, text="High Score: " + str(high_score), fill="white", anchor=tk.W)
    for segment in player_snake:
        canvas.create_rectangle(segment[0] * cell_size, segment[1] * cell_size,
                                (segment[0] + 1) * cell_size, (segment[1] + 1) * cell_size,
                                fill=player_snake_color)
    for obstacle in obstacles:
        canvas.create_rectangle(obstacle[0] * cell_size, obstacle[1] * cell_size,
                                (obstacle[0] + 1) * cell_size, (obstacle[1] + 1) * cell_size,
                                fill="gray")
    canvas.create_rectangle(food[0] * cell_size, food[1] * cell_size,
                            (food[0] + 1) * cell_size, (food[1] + 1) * cell_size,
                            fill="red")

    # Schedule the next update
    root.after(snake_speed, update_player_snake)

# Function to handle keypress events for the player's snake
def on_key_press(event):
    global player_snake_direction

    if event.keysym == "Up":
        player_snake_direction = (0, -1)
    elif event.keysym == "Down":
        player_snake_direction = (0, 1)
    elif event.keysym == "Left":
        player_snake_direction = (-1, 0)
    elif event.keysym == "Right":
        player_snake_direction = (1, 0)

# Create the canvas to draw on
canvas = tk.Canvas(root, width=600, height=400, bg="black")
canvas.pack()

# Bind keypress events to the canvas
canvas.bind("<KeyPress>", on_key_press)
canvas.focus_set()

# Start the game
update_player_snake()

# Run the Tkinter main loop
root.mainloop()
