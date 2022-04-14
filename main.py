import pygame
pygame.init()

window = pygame.display.set_mode((1200, 400))
track = pygame.image.load("track.png")
car = pygame.image.load("car.png")
car = pygame.transform.scale(car, (30, 60))
car_x = 153
car_y = 300
cam_x_offset = 0
cam_y_offset = 0
drive = True
direction = "up"
speed = pygame.time.Clock()

while drive:
    speed.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drive = False

    # declare sensor
    cam_x = car_x + cam_x_offset + 15
    cam_y = car_y + cam_y_offset + 15
    focal_distance = 20

    # detect road using sensor
    up_px = window.get_at((cam_x, cam_y - focal_distance))[0]
    down_px = window.get_at((cam_x, cam_y + focal_distance))[0]
    right_px = window.get_at((cam_x + focal_distance, cam_y))[0]
    # print(up_px, right_px, down_px)
    print(up_px)

    # change car direction
    if direction == "up" and up_px != 255 and right_px == 255:
        direction = "right"
        cam_x_offset = 30
        car = pygame.transform.rotate(car, -90)
    elif direction == "right" and right_px != 255 and down_px == 255:
        direction = "down"
        car_x = car_x + 30
        cam_x_offset = 0
        cam_y_offset = 30
        car = pygame.transform.rotate(car, -90)
    elif direction == "down" and down_px != 255 and right_px == 255:
        direction = "right"
        car = pygame.transform.rotate(car, 90)
        car_y = car_y + 30
        cam_y_offset = 0
        cam_x_offset = 30
    elif direction == "right" and right_px != 255 and up_px == 255:
        direction = "up"
        car = pygame.transform.rotate(car, 90)
        car_x = car_x + 30
        cam_x_offset = 0


    # drive
    if direction == "up" and up_px == 255:
        car_y = car_y - 2
    elif direction == "right" and right_px == 255:
        car_x = car_x + 2
    elif direction == "down" and down_px == 255:
        car_y = car_y + 2
    window.blit(track, (0, 0))
    window.blit(car, (car_x, car_y))
    pygame.draw.circle(window, (0, 255, 0), (cam_x, cam_y), 5, 5)
    pygame.display.update()
