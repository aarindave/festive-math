# This imports the Pygame module and its pre-made constants.
import pygame
from pygame.locals import *

# This initializes the font module.
pygame.font.init()

# This creates a basic Pygame window.
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Festive Math")

# This defines the dimensions of the screen.
WIDTH = screen.get_width()
HEIGHT = screen.get_height()

# This loads the images.
background = pygame.image.load("Images/background.jpeg")

check_mark = pygame.image.load("Images/check_mark.png")
check_mark = pygame.transform.scale(check_mark, (WIDTH // 20, WIDTH // 20))

distance_image = pygame.image.load("Images/distance_image.jpeg")
distance_image = pygame.transform.scale(distance_image, (WIDTH // 3, WIDTH // 3))

time_image = pygame.image.load("Images/time_image.jpeg")
time_image = pygame.transform.scale(time_image, (WIDTH // 3, WIDTH // 3))

discount_image = pygame.image.load("Images/discount_image.jpeg")
discount_image = pygame.transform.scale(discount_image, (WIDTH // 3, WIDTH // 3))


answer = ""
mouse_down = False
stage = "main"

# These represent the text for the lessons.

DISCOUNT_LESSON = """To figure out the cost of an item after
discount, we need to figure out what the
discount value will be. We subtract the
discount from the original value to get
our result. Alternatively, we could find
the percentage of the original value that
is not discounted and multiply that
percentage by the original value.

Prompt: Adams was searching through a 
Christmas store to buy golden Christmas 
ornaments at a holiday-exclusive 
discounted price. One ornament that used to 
cost $20 has a 40% markdown. Figure out how 
many dollars Adams has to pay.

Hint: What is the percentage left over? What is
the value of the discount?
"""

DISTANCE_LESSON = """To measure the straight-line distance between 
two particular points, you have to measure the 
horizontal and vertical difference between the 
coordinates. After doing so, you can apply the 
Pythagorean Theorem (a² + b² = c²) to find the 
straight line distance.

Prompt: Lucy's family was planning to travel
to the southern tip of Lake Algae. If the 
family has to drive sixty miles east and 
eighty miles north to reach the southern tip, 
how many miles northeast can Lucy travel?

Hint: Find the horizontal and vertical shifts.
Is it possible to apply the Pythagorean Theorem?
"""

TIME_LESSON = """Figuring out the total time may sound like a
tedious task to perform. Luckily, we can reuse 
the standard addition method to work for time.
For example, if we wanted to add 7:30 to 1:50,
we can add the number of minutes. We find there
are eighty minutes, but there are sixty minutes 
in an hour. This means we have to carry over 
those sixty minutes to our next calculation of 
adding up the hours. All in all, our result is
9:20.

Prompt: Jesse was attempting to stay on vacation
for no more than ten hours. His first stay will
take two hours. The next stay will take 150
minutes. He has to stay four hours and fifteen
minutes at his third stay. In minutes, how long 
can he stay at his final trip?

Hint: Add up the total known time. Use common 
sense to figure out the remaining time he has.
"""


# This defines a lesson class to make it easier to create lessons.
class Lesson:

    # This is the initialization function. This runs upon using the class.
    def __init__(self, title, text, image, solution):
        
        # This sets some information regarding the lesson.
        self.title = title
        self.text = text
        self.image = image
        self.solution = solution

        # This sets the font sizes.
        self.title_size = 60
        self.text_size = 24

    # This is the open method. This opens the lesson.
    def open(self):

        # This makes the global variable stage accessible to the function.
        global answer, stage

        # This will display the title.
        display_text(self.title, WIDTH // 2, HEIGHT // 10, "white", self.title_size)

        # This will display the back button.
        back_button = draw_center_rect("maroon", WIDTH // 10 * 9, HEIGHT // 10 * 9, 100, 50, 5)
        display_text("Back", *back_button.center, "white", 20)

        # This will display the textbox.
        textbox = pygame.draw.rect(screen, "white", (WIDTH // 2, back_button.y, WIDTH // 5, back_button.height),
                                   border_radius=5)
        display_text(answer, textbox.left * 1.01, textbox.top, "black", 36, center=False)

        # This will display the image.
        screen.blit(self.image, (WIDTH // 4 - self.image.get_width() // 2, HEIGHT // 2 - self.image.get_height() // 2))

        # This will display the check button.
        submit_button = screen.blit(check_mark, (WIDTH // 4 * 3, back_button.y))

        # This will display the text.
        for line_number, line_text in enumerate(self.text.split("\n")):
            display_text(line_text, WIDTH // 2, HEIGHT // 5 + line_number * self.text_size, "white", self.text_size,
                         center=False)

        # Runs if the mouse is currently down.
        if mouse_down:
            # This collects the mouse position
            mouse_position = pygame.mouse.get_pos()
            # This detects if the mouse is touching the back button.
            if back_button.collidepoint(*mouse_position):
                # This switches to the main screen.
                stage = "main"
            # This detects if the mouse is touching the submit button, and the answer is numerical.
            elif submit_button.collidepoint(*mouse_position) and answer.isnumeric():
                if self.solution == answer:
                    answer = "Correct!"
                else:
                    answer = "Incorrect!"


def display_text(text, x, y, color, size, center=True):
    font_object = pygame.font.Font("/System/Library/Fonts/Avenir Next.ttc", size)
    text_object = font_object.render(text, False, color)

    # This will run if the text is meant to be in the center.
    if center:
        screen.blit(text_object, (x - text_object.get_width() // 2, y - text_object.get_height() // 2))
    # This will run if the text is meant to be in the top-left.
    else:
        screen.blit(text_object, (x, y))


def draw_center_rect(color, x, y, width, height, border_radius=5):
    return pygame.draw.rect(screen, color, (x - width // 2, y - height // 2, width, height),
                            border_radius=border_radius)


def main():
    global stage

    # This displays the title.
    display_text("Festive Math", WIDTH // 2, HEIGHT // 10, "white", 60)

    # These display your math lessons.
    travel_lesson = draw_center_rect("orange", WIDTH // 4, HEIGHT // 2, WIDTH // 5, HEIGHT // 5, 10)
    vacation_lesson = draw_center_rect("seagreen", WIDTH // 2, HEIGHT // 2, WIDTH // 5, HEIGHT // 5, 10)
    holidays_lesson = draw_center_rect("purple", WIDTH // 4 * 3, HEIGHT // 2, WIDTH // 5, HEIGHT // 5, 10)

    display_text("Discounts", *holidays_lesson.center, "white", 36)
    display_text("Distance", *travel_lesson.center, "white", 36)
    display_text("Time", *vacation_lesson.center, "white", 36)

    if mouse_down:
        mouse_position = pygame.mouse.get_pos()
        if holidays_lesson.collidepoint(*mouse_position):
            stage = "discount_lesson"
        elif travel_lesson.collidepoint(*mouse_position):
            stage = "distance_lesson"
        elif vacation_lesson.collidepoint(*mouse_position):
            stage = "time_lesson"


# This sets up the three lessons using classes.
discount_lesson = Lesson("Discount Lesson", DISCOUNT_LESSON, discount_image, "12")
distance_lesson = Lesson("Distance Lesson", DISTANCE_LESSON, distance_image, "100")
time_lesson = Lesson("Time Lesson", TIME_LESSON, time_image, "75")

# This program will run forever.
while True:
    # This runs through all the Pygame events.
    for event in pygame.event.get():
        # This will run if the quit button is clicked.
        if event.type == QUIT:
            # This uninitializes the Pygame module.
            pygame.quit()
            # This exits the program.
            exit()
        # This will run if the mouse button is down.
        elif event.type == MOUSEBUTTONDOWN:
            mouse_down = True
        # This will run if the mouse button is up.
        elif event.type == MOUSEBUTTONUP:
            mouse_down = False
        # This will run if a key is released.
        elif event.type == KEYUP:
            # This will run if we are in the lesson page.
            if stage != "main":
                # This will run if we are pressing a number.
                if chr(event.key).isdigit():
                    # This will run if the output has been shown.
                    if answer[:-1].isalpha():
                        # It will clear the answer stream.
                        answer = ""
                    # It will add on the key being pressed.
                    answer += chr(event.key)
                # This will run if backspace is being pressed.
                elif event.key == K_BACKSPACE:
                    # Delete the last character of the answer.
                    answer = answer[:-1]

    # This will blit an image to the background.
    screen.blit(background, (0, 0))

    # This will run if we are at the main screen.
    if stage == "main":
        # This clears the answer.
        answer = ""
        # This renders the main screen.
        main()
    # This will run if we are at the lesson screens.
    elif stage == "distance_lesson":
        distance_lesson.open()
    elif stage == "time_lesson":
        time_lesson.open()
    elif stage == "discount_lesson":
        discount_lesson.open()

    # This will display the latest changes.
    pygame.display.update()
