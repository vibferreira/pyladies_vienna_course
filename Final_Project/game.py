import pyglet
import math
from funcs import food_random

# user define the number of food
user = int(input("Input number of food: ")) 

# window constructor 
window = pyglet.window.Window(800,600,'Snake Game')
pyglet.gl.glScalef(0.3, 0.3, 0.5) # adjust the window content size

# loads the images  
image_s = pyglet.resource.image('snake.png')
image_f = pyglet.resource.image('food.png')

# snake object
snake = pyglet.sprite.Sprite(image_s)
snake.y = 1500
snake.x = 50

# randomly setting the position of the food
food = food_random(user, snake.position)

# setting the keyboard movements
@window.event
def on_text_motion(motion):
    if motion == pyglet.window.key.MOTION_UP:
       snake.y = snake.y+100 
    elif motion == pyglet.window.key.MOTION_DOWN:
        snake.y = snake.y-100 
    elif motion == pyglet.window.key.MOTION_LEFT:
        snake.x = snake.x-100
    elif motion == pyglet.window.key.MOTION_RIGHT:
        snake.x = snake.x+100

# setting the movement
def tick(t):
    snake.x = snake.x + t * 60
    snake.y = snake.y + 20 * math.sin(snake.x / 5)

pyglet.clock.schedule_interval(tick, 1/30)

# make snake get bigger after eating food

# make food disapear after being eaten

# infinite game board

# add sound effect


#drawings
@window.event
def on_draw():
    window.clear()
    snake.draw()
    for f in food:
        f.draw()

window.push_handlers(
    on_draw=on_draw,
    on_text_motion=on_text_motion
)

pyglet.app.run()