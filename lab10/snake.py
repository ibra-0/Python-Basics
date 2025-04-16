import psycopg2
import pygame
import random
import time

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="postgres"
    )

def get_or_create_user(username):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    user = cur.fetchone()

    if user:
        user_id = user[0]
        print(f"Добро пожаловать обратно, {username}!")
    else:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        conn.commit()
        print(f"Создан новый пользователь: {username}")

    cur.close()
    conn.close()
    return user_id

def save_score(user_id, score, level):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO user_score (user_id, score, level)
        VALUES (%s, %s, %s)
        ON CONFLICT (user_id)
        DO UPDATE SET score = EXCLUDED.score, level = EXCLUDED.level
    """, (user_id, score, level))

    conn.commit()
    cur.close()
    conn.close()


pygame.init()

WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
FPS = 10

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()


class Snake:
    def __init__(self):
        self.body = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = RIGHT
        self.growing = 0

    def move(self):
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0] * CELL_SIZE, head_y + self.direction[1] * CELL_SIZE)

        if (new_head in self.body or
            new_head[0] < 0 or new_head[1] < 0 or
            new_head[0] >= WIDTH or new_head[1] >= HEIGHT):
            return False

        self.body.insert(0, new_head)

        if self.growing > 0:
            self.growing -= 1
        else:
            self.body.pop()

        return True

    def grow(self, amount):
        self.growing += amount

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))


class Food:
    def __init__(self):
        self.spawn()

    def spawn(self):
        while True:
            self.position = (
                random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
                random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
            )
            self.weight = random.choice([1, 2, 3])
            self.color = RED if self.weight == 1 else BLUE if self.weight == 2 else YELLOW
            self.timer = random.randint(30, 50)

            if self.position not in snake.body:
                break

    def update(self):
        self.timer -= 1
        if self.timer <= 0:
            self.spawn()

    def draw(self):
        pygame.draw.rect(screen, self.color, (*self.position, CELL_SIZE, CELL_SIZE))


def main():
    global snake
    snake = Snake()
    food = Food()
    running = True
    current_score = 0
    current_level = 1

    font = pygame.font.SysFont(None, 24)

    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and snake.direction != DOWN:
            snake.direction = UP
        elif keys[pygame.K_DOWN] and snake.direction != UP:
            snake.direction = DOWN
        elif keys[pygame.K_LEFT] and snake.direction != RIGHT:
            snake.direction = LEFT
        elif keys[pygame.K_RIGHT] and snake.direction != LEFT:
            snake.direction = RIGHT

        if not snake.move():
            break

        if snake.body[0] == food.position:
            snake.grow(food.weight)
            current_score += food.weight
            food.spawn()

            if current_score % 10 == 0:
                current_level += 1

        food.update()
        food.draw()
        snake.draw()

        text = font.render(f"Счёт: {current_score}  Уровень: {current_level}", True, (0, 0, 0))
        screen.blit(text, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)

    save_score(user_id, current_score, current_level)
    pygame.quit()


if __name__ == "__main__":
    username = input("Введите имя пользователя: ")
    user_id = get_or_create_user(username)
    print("Игра начнётся через 3 секунды...")
    time.sleep(5)
    main()
