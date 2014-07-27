__author__ = 'drew'

from bottle import route, run, template, request, static_file
from navigator import get_user, get_terrain, move_north, move_northeast, move_northwest, move_south, move_southeast, move_southwest, get_mini_map

@route('/')
def index():
    return template('login')

@route('/login', method='POST')
def index():
    username = request.forms.get('username')
    user = get_user(username)
    tile = get_terrain(user['longitude'],user['latitude'])
    get_mini_map(user['longitude'],user['latitude'])

    return template('navigate', tile=tile, user=user)

@route('/resources/:path#.+#', name='static')
def static(path):
    print "Returning static: " + path
    return static_file(path, root='')

@route('/move', method='POST')
def index():
    user_id = request.forms.get('user_id')
    direction = request.forms.get('direction')
    if direction == 'north':
        user = move_north(user_id)
    elif direction == 'northeast':
        user = move_northeast(user_id)
    elif direction == 'northwest':
        user = move_northwest(user_id)
    elif direction == 'south':
        user = move_south(user_id)
    elif direction == 'southeast':
        user = move_southeast(user_id)
    elif direction == 'southwest':
        user = move_southwest(user_id)

    map = get_mini_map(user['longitude'],user['latitude'])
    tile = get_terrain(user['longitude'],user['latitude'])
    return template('navigate', tile=tile, user=user, map=map)

run(host='localhost', port=8080)


