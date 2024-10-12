# Snake Game

# Import libraries
import pygame
import random

# Screen dimensions: Width  = 400, Height = 400
size = (400, 400)

# Background color
background_color = (0, 0, 0)

# Initialize pygame
pygame.init()

# Set the Height and the width of the game screen
screen = pygame.display.set_mode(size)

# Clock object to control the frame rate
clock = pygame.time.Clock()

# Snake speed (in frames per second)
snake_speed = 5

# Load a font for Heading
Heading_font = pygame.font.Font(None, 40)

# Load a font for score
score_font = pygame.font.Font(None, 20)

# Print: "Snake Game"
Hello_text1 = Heading_font.render("Welcome to Snake Game!!", True, "Blue")
Hello_text1_rect = Hello_text1.get_rect()
Hello_text1_rect.center = ((size[0] // 2), (size[1] // 2))

# Score
score = 0
temp_score = 0

# Print the score:
Score_text = score_font.render(f"Score: {score}", True, "White")
Score_text_rect = Score_text.get_rect()
Score_text_rect.topleft = (10, 10)

# Game over texts

# Print: "Game Over"
GameOver_text = Heading_font.render("Game Over!!!!!!!!!!!", True, "Red")
GameOver_text_rect = GameOver_text.get_rect()
GameOver_text_rect.center = ((size[0] // 2), (size[1] // 2))

# Init. position of food
food_position = ((size[0] // 2), (size[1] // 2))

# Init. snake position
snake_position = ((size[0] // 4), (size[1] //2))

# The snake body
snake = [[snake_position[0], snake_position[1]],
         [snake_position[0] - 10, snake_position[1]],
         [snake_position[0] - 20, snake_position[1]]]

# Init. snake direction
direction = pygame.K_RIGHT

# new head of the snake
new_head = [snake[0][0], snake[0][1]]

# Fill the screen with the background color 
screen.fill(background_color)
# Display Hello texts to the game screen
screen.blit(Hello_text1, Hello_text1_rect)
# Update the display
pygame.display.flip()
# Wait for 2 seconds 
pygame.time.delay(2000)

##### The Game Loop #####
while True:
    
    # Set the frame rate (snake speed)
    clock.tick(snake_speed)
    
    # Fill the screen with the background color 
    screen.fill(background_color)
    
    # Display caption for the game screen
    caption = "Snake Game By Eng.Bassant El-Bakry"
    pygame.display.set_caption(caption)
    
    # Print the score
    screen.blit(Heading_font.render(f"Score: {score}", True, "White"), 
                GameOver_text.get_rect())
    
    # Draw the food
    pygame.draw.rect(screen, (255, 0, 0), [food_position[0], food_position[1], 10, 10])
    
    # Draw the snake
    for position in snake:
        pygame.draw.rect(screen, (0, 0, 255), [position[0], position[1], 10, 10])
    
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
        # Control the snake movement
        elif event.type == pygame.KEYDOWN:
            if event.key == None:
                continue
            else:
                if event.key == pygame.K_UP:
                    direction = pygame.K_UP
                if event.key == pygame.K_DOWN:
                    direction = pygame.K_DOWN
                if event.key == pygame.K_LEFT:
                    direction = pygame.K_LEFT
                if event.key == pygame.K_RIGHT:
                    direction = pygame.K_RIGHT
    
    # Update the new head position            
    if direction == pygame.K_UP:
        new_head[1] -= 10
    elif direction == pygame.K_DOWN:
        new_head[1] += 10
    elif direction == pygame.K_LEFT:
        new_head[0] -= 10
    elif direction == pygame.K_RIGHT:
        new_head[0] += 10
                            
    # Insert new head to the snake:
    snake.insert(0, list(new_head)) 
    
    # Check if snake collides with the window or with itself
    if snake[0][0] < 0 or snake[0][0] >= size[0] or snake[0][1] < 0 or snake[0][1] >= size[1] or snake[0] in snake[1:]:
        # Fill the screen with the background color to clear the screen 
        screen.fill(background_color)
        # Display Game Over to the game screen
        screen.blit(GameOver_text, GameOver_text_rect)
        # Update the display
        pygame.display.flip()
        # Wait for 3 seconds the Quit the game
        pygame.time.delay(3000)
        pygame.quit()
        quit()
    
    # Check if the snake ate the food
    if snake[0][0] == food_position[0] and snake[0][1] == food_position[1]:
        # Generate food position that avoids walls and the top-left corner
        food_position = (random.randint(2, (size[0] // 10) - 2) * 10, random.randint(2, (size[1] // 10) - 2) * 10)
        # Increase the score by 10
        score += 10
        # Every time the score increases by 40, the snake's speed increases by 3
        if (score - temp_score) == 40:
            # Increase the snake speed by 3
            snake_speed += 3
            temp_score  = score  
    else:
        snake.pop()      
            
    # Update the display
    pygame.display.flip()
            
# Quit Pygame
pygame.quit()
quit()
    





