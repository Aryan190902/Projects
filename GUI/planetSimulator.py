import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 800 # for defining the dimensions of the program
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # For taking the coordinates of our program

YELLOW = (255, 255, 0) # RGB code for yellow color
BLUE = (100, 149, 237)
RED = (188, 39, 50)
DARK_GREY = (80, 78, 81)
WHITE = (255, 255, 255)

FONT = pygame.font.SysFont("comicsans", 16)

pygame.display.set_caption("Solar System") # Title of the window

class Planet:
    AU = 149.6e6*1000# Distance between Earth and Sun
    # Converted the distance in metres.
    G = 6.67428e-11 #Gravitational Constant
    SCALE = 250/AU # Scale set to be 1AU = 100px
    TIMESTEP = 3600*24 # Set to 1 day.

    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.sun = False
        self.dist_sun = 0
        self.orbit = []

        self.velX = 0 # Velocity in X direction
        self.velY = 0 # Velocity in Y direction

    def Draw(self, win):
        x = self.x*self.SCALE + WIDTH/2 # To place x, y in the center.
        y = self.y*self.SCALE + HEIGHT/2
        if len(self.orbit)>2:
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = x*self.SCALE + WIDTH/2
                y = y*self.SCALE + HEIGHT/2
                updated_points.append((x, y))
            
            pygame.draw.lines(win, self.color, False, updated_points, 2)
            pygame.draw.circle(win, self.color, (x, y), self.radius)
        if not self.sun:
            distText = FONT.render(f"{round(self.dist_sun/1000, 1)}km", 1, WHITE)
            win.blit(distText, (x, y))

        
    
    def Force(self, other):
        other_x, other_y = other.x, other.y
        distX = other_x - self.x
        distY = other_y - self.y
        totalDist = math.sqrt(distX**2 + distY**2)

        if other.sun:
            self.dist_sun = totalDist

        force = self.G*self.mass*other.mass/(totalDist**2)
        theta = math.atan2(distY, distX) # Will give tan inv(y/x)
        forceX = math.cos(theta)*force
        forceY = math.sin(theta)*force

        return forceX, forceY

    def update_pos(self, planets):
        totalForceX = totalForceY = 0
        for planet in planets:
            if self == planet:
                continue
            fx, fy = self.Force(planet)
            totalForceX += fx
            totalForceY += fy

        self.velX += totalForceX/self.mass*self.TIMESTEP
        self.velY += totalForceY/self.mass*self.TIMESTEP

        self.x += self.velX*self.TIMESTEP
        self.y += self.velY*self.TIMESTEP
        self.orbit.append((self.x, self.y))


def main():
    run = True
    clock = pygame.time.Clock()

    sun = Planet(0, 0, 30, YELLOW, 1.98892*10**30)
    sun.sun = True

    earth = Planet(-1*Planet.AU, 0,16, BLUE, 5.9724*10**24)
    earth.velY = 29.783*1000 # in metre per second

    mars = Planet(-1.524*Planet.AU, 0, 12, RED, 6.39*10**23)
    mars.velY = 24.077*1000

    mercury = Planet(0.387*Planet.AU, 0, 8, DARK_GREY, 3.30*10**23)
    mercury.velY = -47.4*1000

    venus = Planet(0.723*Planet.AU, 0, 14, WHITE, 4.8685*10**24)
    venus.velY = -35.02*1000

    planets = [sun, earth, mars, mercury, venus]

    while run:
        clock.tick(60)
        WIN.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run= False

        for planet in planets:
            planet.update_pos(planets)
            planet.Draw(WIN)

        pygame.display.update()

    pygame.quit()

main()
