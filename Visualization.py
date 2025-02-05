import pygame
import CrossRoad
import Car

crossroad = CrossRoad.CrossRoad(1, 1, 1, 1, 10, 10)

# Constants
WINDOW_SIZE = 600  # Window size (square window)
coefficient = 4 # coefficient to adjust the size of the crossroads for the visualization

ROAD_WIDTH_SN = (crossroad.lanes_south + crossroad.lanes_north) * crossroad.size_crossroad_sn * coefficient

ROAD_WIDTH_WE = (crossroad.lanes_west + crossroad.lanes_east) * crossroad.size_crossroad_we * coefficient

one_lane = crossroad.size_crossroad_sn//2 * coefficient

size_ns = crossroad.size_crossroad_sn * coefficient
size_we = crossroad.size_crossroad_we * coefficient

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Crossroads Visualization")

# Colors
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
YELLOW = (255, 204, 0)
RED = (255, 0, 0)

# Function to draw the crossroads
def draw_crossroads():
    screen.fill(WHITE)

    # Draw vertical road
    pygame.draw.rect(screen, GRAY, [
        (WINDOW_SIZE // 2 - ROAD_WIDTH_SN // 2), 0, 
        ROAD_WIDTH_SN, WINDOW_SIZE
    ])

    # Draw horizontal road
    pygame.draw.rect(screen, GRAY, [
        0, (WINDOW_SIZE // 2 - ROAD_WIDTH_WE // 2),
        WINDOW_SIZE, ROAD_WIDTH_WE
    ])

    # Draw lane markings (dashed lines) = > To see the different lane : dotted or plain line
    
    # Add the lane markings

    # Plain lines but no lines inside the crossroads
    # Draw lane markings (dashed lines)
    dash_length = 20  # Length of each dash
    gap_length = 20   # Gap between dashes

    pygame.draw.line(screen, YELLOW, (WINDOW_SIZE // 2, 0), (WINDOW_SIZE // 2, WINDOW_SIZE//2 - size_ns), 5)
    pygame.draw.line(screen, YELLOW, (WINDOW_SIZE // 2 , WINDOW_SIZE // 2 + size_ns), (WINDOW_SIZE//2, WINDOW_SIZE), 5)

    pygame.draw.line(screen, YELLOW, (0, WINDOW_SIZE // 2), (WINDOW_SIZE//2 - size_we, WINDOW_SIZE // 2), 5)
    pygame.draw.line(screen, YELLOW, (WINDOW_SIZE // 2 + size_we, WINDOW_SIZE // 2), (WINDOW_SIZE, WINDOW_SIZE // 2), 5)

# Create cars

car = Car.Car(1, 10, 2, 6) # Create a car with id, speed, width, and length 

def move_car():
    initial_position = (WINDOW_SIZE // 2, 0)
    car_position = initial_position
    car_speed = car.speed
    car_width = car.width
    car_length = car.length

    while car_position[1] < WINDOW_SIZE:
        car_position = (car_position[0], car_position[1] + car_speed)
        # remove the previous car
        pygame.draw.rect(screen, GRAY , [car_position[0] - car_width // 2 - one_lane, car_position[1] - car_speed, car_width * coefficient , car_length*coefficient])
        pygame.draw.rect(screen, RED, [car_position[0] - car_width // 2 - one_lane, car_position[1], car_width*coefficient, car_length*coefficient])
        pygame.display.flip()
        pygame.time.delay(100)
    
    
    
    

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_crossroads()
    move_car()
    pygame.display.flip()

pygame.quit()
