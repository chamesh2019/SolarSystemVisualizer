import sys
import pygame
from math import cos, sin, pi

BLACK, WHITE = (0, 0, 0), (255, 255, 255)

class Base(object):
    def __init__(self, SIZE, FRAME_RATE, scale, SUN) -> None:
        self.FRAME_RATE= FRAME_RATE
        self.width, self.height = SIZE
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(SIZE)
        self.scale = scale
        self.sun = SUN
        self.offset = (0, 0)
        self.current_planets = []
        
    def tick(self):
        for planet in self.current_planets:
            planet.tick()
        
    def add_planet(self, planet):
        self.current_planets.append(planet)
        
    def run(self) -> None:
        dragging = False
        running = True
        while running:
            self.screen.fill(BLACK)
            self.clock.tick(self.FRAME_RATE)
            
            self.sun.draw(self)
            
            for planet in self.current_planets:
                planet.draw(self)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        dragging = True
                        previous_mouse_cordinates = pygame.mouse.get_pos()
                        current_X_offset, current_Y_offset = self.offset
                    elif event.button == 4:
                        self.scale += 100
                        
                    elif event.button == 5:
                        self.scale -= 100
                                
                
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    dragging = False
                    
                if event.type == pygame.MOUSEMOTION:
                    if dragging:
                        current_mouse_x_cordinate, current_mouse_y_cordinate = event.pos
                        previous_mouse_x_cordinate, previous_mouse_y_cordinate = previous_mouse_cordinates
                        X_offset = current_mouse_x_cordinate - previous_mouse_x_cordinate
                        Y_offset = current_mouse_y_cordinate - previous_mouse_y_cordinate
                        self.offset = current_X_offset + X_offset, current_Y_offset + Y_offset
                                        
            pygame.display.update()
            self.tick()

        
        
class Sun(object):
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color
        self.cordinates = (0,0)
        
    def draw(self, base):
        vertical_offset , horizontal_offset = base.offset
        X_cordinates, Y_cordinates = base.width/2 + vertical_offset, base.height/2 + horizontal_offset
        radius = self.radius/base.scale
        self.cordinates = X_cordinates, Y_cordinates
        pygame.draw.circle(base.screen, self.color, (X_cordinates, Y_cordinates), radius)
        
        
class Planet(object):
    def __init__(self, distance, radius, rotation_period, color, orbital_period, moons=[]):
        self.distance = distance
        self.radius = radius
        self.orbital_angle = 0
        self.rotational_angle = 0
        self.rotation_period = rotation_period
        self.orbital_period = orbital_period
        self.cordinates = (0, 0)
        self.color = color
        self.moons = moons
        
    def spherical_cordinates(self, base):
        sun_x_cordinate, sun_y_cordinate = base.sun.cordinates
        x_cordinate = (self.distance - base.sun.radius)/(base.scale*50) * sin(self.orbital_angle) + sun_x_cordinate
        y_cordinate = (self.distance - base.sun.radius)/(base.scale*50) * cos(self.orbital_angle) + sun_y_cordinate
        return x_cordinate, y_cordinate
    
    def draw(self, base):
        radius = self.radius/base.scale*50
        x_cordinate, y_cordinate = self.spherical_cordinates(base)
        self.cordinates = x_cordinate, y_cordinate
        pygame.draw.circle(base.screen, WHITE, base.sun.cordinates, self.distance/(base.scale*50), 1)
        pygame.draw.circle(base.screen, self.color, (x_cordinate, y_cordinate), radius)
        for moon in self.moons:
            moon.draw(self, base)

        
    def tick(self):
        orbital_diff_per_tick = 2*pi/self.orbital_period
        self.orbital_angle += orbital_diff_per_tick/10
        rotational_diff_per_tick = 2*pi/self.rotation_period
        self.rotation_period += rotational_diff_per_tick/10
        for moon in self.moons:
            moon.tick()
        
    def add_moon(self, moon):
        self.moons.append(moon)
        

class Moon(object):
    def __init__(self, radius, distance, rotational_period, orbital_period, color) -> None:
        self.radius = radius
        self.distance = distance
        self.rotational_period = rotational_period
        self.orbital_period = orbital_period
        self.orbital_angle = 0
        self.rotational_angle = 0
        self.color = color
     
    def draw(self, planet, base):
        radius = self.radius/base.scale*30
        x_cordinate, y_cordinate = self.spherical_cordinates(planet, base)
        pygame.draw.circle(base.screen, WHITE, planet.cordinates, self.distance/(base.scale), 1)
        pygame.draw.circle(base.screen, self.color, (x_cordinate, y_cordinate), radius) 
      
    def spherical_cordinates(self, planet, base):
        planet_x_cordinate, planet_y_cordinate = planet.cordinates
        x_cordinate = (self.distance - planet.radius)/(base.scale) * sin(self.orbital_angle) + planet_x_cordinate
        y_cordinate = (self.distance - planet.radius)/(base.scale) * cos(self.orbital_angle) + planet_y_cordinate
        return x_cordinate, y_cordinate  
     
    def tick(self):
        orbital_diff_per_tick = 2*pi/self.orbital_period
        self.orbital_angle += orbital_diff_per_tick/10
        rotational_diff_per_tick = 2*pi/self.rotational_period
        self.rotational_angle += rotational_diff_per_tick/10