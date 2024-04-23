import pygame
import webbrowser
import threading

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Set up the screen
screen_width = 1300
screen_height = 750
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Operating System Emulator")

# Load background image
background = pygame.image.load("1.png")
background = pygame.transform.scale(background, (screen_width, screen_height))

# Load icons
icon_images = [pygame.transform.scale(pygame.image.load(f"icon{i}.png"), (100, 100)) for i in range(1, 7)]
icon_positions = [(50 + i * 150, 550) for i in range(6)] + [(850, 550)]

# Load alarm sound
alarm_sound = pygame.mixer.Sound("alarm.mp3")

# Function to open new window with specified background image
def open_window(image_name):
    print("Opening window:", image_name)
    new_screen = pygame.display.set_mode((screen_width, screen_height))
    background = pygame.image.load(image_name)
    background = pygame.transform.scale(background, (screen_width, screen_height))
    new_screen.blit(background, (0, 0))
    pygame.draw.rect(new_screen, (255, 0, 0), (1050, 600, 50, 50))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if 1050 <= event.pos[0] <= 1100 and 600 <= event.pos[1] <= 650:
                        return

# Function to play alarm sound
def play_alarm_sound():
    print("Playing alarm sound")
    alarm_sound.play()
    pygame.time.wait(5000)
    alarm_sound.stop()

# Main loop
running = True
while running:
    screen.blit(background, (0, 0))
    for i, icon in enumerate(icon_images):
        screen.blit(icon, icon_positions[i])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                for i, pos in enumerate(icon_positions):
                    if pos[0] <= mouse_pos[0] <= pos[0] + 100 and pos[1] <= mouse_pos[1] <= pos[1] + 100:
                        if i == 1:  # Icon 2
                            threading.Thread(target=play_alarm_sound).start()
                            open_window(f"{i + 2}.png")  # Ensure the window opens
                        elif i == 5:  # Icon 6
                            webbrowser.open('https://nuclearsecrecy.com/nukemap/')
                        else:
                            open_window(f"{i + 2}.png")

    pygame.display.update()

pygame.quit()
