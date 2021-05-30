from  random import randrange
import math
import pyglet

image_f = pyglet.resource.image('food.png')

# Randomly setting the position of the food - adapted from Pyglet documentation 
def food_random(num_food, player_position):
    '''' Takes the number of expected food objects and the position of the player and 
    draws the food while it is within a certain distance from the player.
    num_food: number of expected food objects
    player_position: position of the player (main sprite object)'''
    food_lst = []
    for i in range(num_food):
        food_x, food_y = player_position
        while math.dist((food_x, food_y), player_position) < 800:
            food_x = randrange(100, 2100, 100) #make it depends on the window size
            food_y = randrange(0, 1800, 200)
        new_food = pyglet.sprite.Sprite(img= image_f, x=food_x, y=food_y)
        food_lst.append(new_food)
    return food_lst
