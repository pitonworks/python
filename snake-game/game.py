"""
Game Sınıfı - Snake Game'in ana oyun mantığını yönetir
Linked List kullanarak yılanı kontrol eder, yem yerleştirir,
çarpışma kontrolü yapar ve oyunu çizer.
Score, level ve high score sistemlerini yönetir.
"""
import random
import tkinter as tk
import os
from snake import Snake
from constants import *

class Game:
    def __init__(self):
        """
        Game constructor - Oyunu başlatır ve tüm bileşenleri hazırlar
        """
        # Create Tkinter window
        self.window = tk.Tk()
        self.window.title("Linked List Snake Game")

        # Create Canvas (drawing area)
        self.canvas = tk.Canvas(
            self.window,
            width=GRID_SIZE * CELL_SIZE,   # Genişlik: grid boyutu * hücre boyutu
            height=GRID_SIZE * CELL_SIZE,  # Yükseklik: grid boyutu * hücre boyutu
            bg="black"  # Arka plan rengi
        )
        self.canvas.pack()

        # Start snake in the center of the grid
        self.snake = Snake(GRID_SIZE // 2, GRID_SIZE // 2)
        self.direction = RIGHT  # Başlangıç yönü: sağ

        # Place first food
        self.food = self.place_food()

        # Score and level system
        self.score = 0  # Current score
        self.level = 1  # Current level
        self.high_score = self.load_high_score()  # Highest score (load from file)
        self.initial_speed = 150  # Initial speed (milliseconds)
        self.current_speed = self.initial_speed  # Current speed
        self.points_per_level = 5  # Every 5 points, level up

        # Bind keyboard keys
        self.window.bind("<Up>", lambda e: self.set_direction(UP))
        self.window.bind("<Down>", lambda e: self.set_direction(DOWN))
        self.window.bind("<Left>", lambda e: self.set_direction(LEFT))
        self.window.bind("<Right>", lambda e: self.set_direction(RIGHT))

        # Start game loop
        self.update()

        # Start Tkinter main loop
        self.window.mainloop()

    def load_high_score(self):
        """
        High score'u dosyadan yükler
        Eğer dosya yoksa veya okuma hatası olursa 0 döndürür
        
        Returns:
            int: Yüklenen high score değeri
        """
        high_score_file = "high_score.txt"
        if os.path.exists(high_score_file):
            try:
                with open(high_score_file, "r") as f:
                    return int(f.read().strip())
            except:
                return 0
        return 0

    def save_high_score(self):
        """
        Save high score to file
        If there is an error, it will be ignored (does not stop the game)
        """
        high_score_file = "high_score.txt"
        try:
            with open(high_score_file, "w") as f:
                f.write(str(self.high_score))
        except:
            pass

    def set_direction(self, d):
        """
        Set snake direction
        Prevent snake from going back on itself
        
        Args:
            d (tuple): New direction (UP, DOWN, LEFT, RIGHT constants)
        """
        # If trying to go back on itself, change direction
        # Example: Cannot go left while going right
        if (self.direction[0] + d[0], self.direction[1] + d[1]) == (0, 0):
            return
        self.direction = d

    def place_food(self):
        """
        Yemi rastgele bir pozisyona yerleştirir
        Yem, yılanın üzerinde olmayan bir konuma yerleştirilir
        
        Returns:
            tuple: (row, column) format of food position
        """
        # Get all positions of the snake as a set (for faster check)
        snake_positions = set(self.snake.get_positions())
        # Find a random position that is not on the snake
        while True:
            r = random.randint(0, GRID_SIZE - 1)  # Random row
            c = random.randint(0, GRID_SIZE - 1)  # Random column
            if (r, c) not in snake_positions:
                return (r, c)  # Found a suitable position

    def update(self):
        """
        Oyun döngüsü - Her frame'de çağrılır
        Yılanın hareketini, çarpışma kontrolünü ve yem yeme işlemlerini yönetir
        """
        # Calculate new head position of the snake
        head_r = self.snake.head.row + self.direction[0]
        head_c = self.snake.head.col + self.direction[1]

        # Wall collision check - Did the snake hit the wall?
        if not (0 <= head_r < GRID_SIZE and 0 <= head_c < GRID_SIZE):
            self.game_over()
            return

        # Self collision check
        if self.snake.collision_with_self(head_r, head_c):
            self.game_over()
            return

        # Food eating check
        if (head_r, head_c) == self.food:
            # Snake will grow
            self.snake.grow()
            self.snake.move(head_r, head_c)
            # Place new food
            self.food = self.place_food()
            
            # Score increase (snake length - 1, because initial length is 1)
            self.score = self.snake.get_length() - 1
            
            # Update high score
            if self.score > self.high_score:
                self.high_score = self.score
                self.save_high_score()  # Save to file
            
            # Level calculation (every 5 points, level up)
            new_level = (self.score // self.points_per_level) + 1
            if new_level > self.level:
                self.level = new_level
                # Speed increase (every level, speed up)
                # Every level, 10ms faster, minimum 50ms
                self.current_speed = max(50, self.initial_speed - (self.level - 1) * 10)
        else:
            # If no food, just move
            self.snake.move(head_r, head_c)

        # Draw screen
        self.draw()
        # Schedule next frame (current speed)
        self.window.after(self.current_speed, self.update)

    def draw(self):
        """
        Oyun ekranını çizer
        Yılanı, yemi ve skor bilgilerini ekrana yansıtır
        """
        # Clear previous drawings
        self.canvas.delete("all")

        # Show score, high score and level information
        info_text = f"Score: {self.score} | High Score: {self.high_score} | Level: {self.level}"
        self.canvas.create_text(
            10,  # X position (left top)
            10,  # Y position (left top)
            text=info_text,
            fill="white",
            font=("Arial", 12),
            anchor="nw"  # North-west alignment
        )

        # Draw food (red square)
        fr, fc = self.food
        self.canvas.create_rectangle(
            fc*CELL_SIZE, fr*CELL_SIZE,  # Left top corner
            fc*CELL_SIZE + CELL_SIZE, fr*CELL_SIZE + CELL_SIZE,  # Right bottom corner
            fill="red"
        )

        # Draw all segments of the snake (green squares)
        for r, c in self.snake.get_positions():
            self.canvas.create_rectangle(
                c*CELL_SIZE, r*CELL_SIZE,  # Left top corner
                c*CELL_SIZE + CELL_SIZE, r*CELL_SIZE + CELL_SIZE,  # Right bottom corner
                fill="green"
            )

    def game_over(self):
        """
        Oyun bittiğinde çağrılır
        Game over mesajını ve final skor bilgisini ekrana yazdırır
        """
        # Game over message (center of the screen, a bit above)
        self.canvas.create_text(
            GRID_SIZE*CELL_SIZE/2,  # Center of the screen (X)
            GRID_SIZE*CELL_SIZE/2 - 30,  # Center of the screen (Y) - 30 pixels above
            text="GAME OVER",
            fill="white",
            font=("Arial", 24)
        )
        # Final score information (center of the screen, a bit below)
        self.canvas.create_text(
            GRID_SIZE*CELL_SIZE/2,  # Center of the screen (X)
            GRID_SIZE*CELL_SIZE/2 + 10,  # Center of the screen (Y) + 10 pixels below
            text=f"Final Score: {self.score} | Level: {self.level}",
            fill="white",
            font=("Arial", 14)
        )
