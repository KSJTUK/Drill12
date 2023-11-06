import random

from pico2d import *
import game_framework

import game_world
from grass import Grass
from boy import Boy
from ball import Ball
from zombie import Zombie

# boy = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)

def init():
    global grass
    global boy
    global balls

    running = True

    grass = Grass()
    game_world.add_object(grass, 0)

    boy = Boy()
    game_world.add_object(boy, 1)

    # fill here
    # 볼을 쉽게 바닥에 뿌림
    balls = [Ball(random.randint(0, 1600), 60, 0) for _ in range(50)]
    game_world.add_objects(balls, 1)


def finish():
    game_world.clear()
    pass


def update():
    game_world.update()
    # fill here
    for ball in balls:
        if game_world.collide(boy, ball):
            print('COLLISION: boy : ball')

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass

