from Solar_System import Base, Sun, Planet, Moon

if __name__ == '__main__':
    SIZE = (1280, 720)
    FPS = 30
    scale = 10001

    SUN_RADIUS = 696_340
    SUN_COLOR = (255, 255, 0)
    SUN = Sun(SUN_RADIUS, SUN_COLOR)
    
    MERCURY_RADIUS = 2_439
    MERCURY_DISTANCE_TO_SUN = 57_000_000
    MERCURY_ROTATION_PERIOD = 59
    MERCURY_ORBITAL_PERIOD = 115
    MERCURY_COLOR = (211, 211, 211)
    MERCURY = Planet(MERCURY_DISTANCE_TO_SUN, MERCURY_RADIUS, MERCURY_ROTATION_PERIOD, MERCURY_COLOR, MERCURY_ORBITAL_PERIOD)
    
    VENUS_RADIUS = 6_051
    VENUS_DISTANCE_TO_SUN = 108_000_000
    VENUS_ROTATION_PERIOD = 116
    VENUS_ORBITAL_PERIOD = 224
    VENUS_COLOR = (100, 100, 87)
    VENUS = Planet(VENUS_DISTANCE_TO_SUN, VENUS_RADIUS, VENUS_ROTATION_PERIOD, VENUS_COLOR, VENUS_ORBITAL_PERIOD)
   
    MOON_RADIUS = 1_737
    MOON_DISTANCE_TO_EARTH = 384_000
    MOON_ROTATION_PERIOD = 28
    MOON_ORBITAL_PERIOD = 28
    MOON_COLOR = (255, 255, 255)
    MOON = Moon(MOON_RADIUS, MOON_DISTANCE_TO_EARTH, MOON_ROTATION_PERIOD, MOON_ORBITAL_PERIOD, MOON_COLOR)

    EARTH_RADIUS = 6_378
    EARTH_DISTANCE_TO_SUN = 150_000_000
    EARTH_ROTATION_PERIOD = 1
    EARTH_ORBITAL_PERIOD = 365
    EARTH_COLOR = (0, 0, 255)
    EARTH = Planet(EARTH_DISTANCE_TO_SUN, EARTH_RADIUS, EARTH_ROTATION_PERIOD, EARTH_COLOR, EARTH_ORBITAL_PERIOD, [MOON])
        
    MARS_RADIUS = 3_390
    MARS_DISTANCE_TO_SUN = 227_000_000
    MARS_ROTATION_PERIOD = 1
    MARS_ORBITAL_PERIOD = 779
    MARS_COLOR = (214, 44, 67)
    MARS = Planet(MARS_DISTANCE_TO_SUN, MARS_RADIUS, MARS_ROTATION_PERIOD, MARS_COLOR, MARS_ORBITAL_PERIOD)
    
    BASE = Base(SIZE, FPS, scale, SUN)
    BASE.add_planet(MERCURY)
    BASE.add_planet(VENUS)
    BASE.add_planet(EARTH)
    BASE.add_planet(MARS)
    BASE.run()