import json
import os
import random
import bottle
import getFood
from getFood import Map

from api import ping_response, start_response, move_response, end_response

@bottle.route('/')
def index():
    return '''
    Battlesnake documentation can be found at
       <a href="https://docs.battlesnake.io">https://docs.battlesnake.io</a>.
    '''

@bottle.route('/static/<path:path>')
def static(path):
    """
    Given a path, return the static file located relative
    to the static folder.

    This can be used to return the snake head URL in an API response.
    """
    return bottle.static_file(path, root='static/')

@bottle.post('/ping')
def ping():
    """
    A keep-alive endpoint used to prevent cloud application platforms,
    such as Heroku, from sleeping the application instance.
    """
    return ping_response()

@bottle.post('/start')
def start():
    data = bottle.request.json

    """
    TODO: If you intend to have a stateful snake AI,
            initialize your snake state here using the
            request's data if necessary.
    """
    print(json.dumps(data))

    color = "#FF0090"

    return start_response(color)


@bottle.post('/move')
def move():
    data = bottle.request.json

    """
    TODO: Using the data from the endpoint request object, your
            snake AI must choose a direction to move in.
    
    """
    size = data['board']['width'] - 1
    map1 = Map()
    layout = map1.makeMap(data, size)
    print(layout)
    xhead = data['board']['snakes'][0]['body'][0]['x']
    yhead = data['board']['snakes'][0]['body'][0]['y']
    xneck = data['board']['snakes'][0]['body'][1]['x']
    yneck = data['board']['snakes'][0]['body'][1]['y']
    status = ['empty', 'food', 'self', 'enemy']
    if xhead > xneck:
        curDirection = 3
    elif xhead < xneck:
        curDirection = 2
    elif yhead > yneck:
        curDirection = 1
    elif yhead < yneck:
        curDirection = 0
    print(json.dumps(data))
    directions = ['up', 'down', 'left', 'right']
    if (xhead == 0 or xhead == size) and (curDirection == 2 or curDirection == 3):
        if yhead < size / 2:
            direction = directions[1]
        if yhead >= size / 2:
            direction = directions[0]
    elif (yhead == 0 or yhead == size) and (curDirection == 0 or curDirection == 1):
        if xhead < size / 2:
            direction = directions[3]
        if xhead >= size / 2:
            direction = directions[2]
    
    else: direction = directions[curDirection]

    return move_response(direction)


@bottle.post('/end')
def end():
    data = bottle.request.json

    """
    TODO: If your snake AI was stateful,
        clean up any stateful objects here.
    """
    print(json.dumps(data))

    return end_response()

# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()

if __name__ == '__main__':
    bottle.run(
        application,
        host=os.getenv('IP', '0.0.0.0'),
        port=os.getenv('PORT', '8080'),
        debug=os.getenv('DEBUG', True)
    )
