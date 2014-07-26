__author__ = 'drew'

from bottle import route, run, template, request, static_file
from navigator import get_user, get_terrain, move_north, move_east, move_south, move_west, get_mini_map

@route('/')
def index():
    return template('login')

@route('/login', method='POST')
def index():
    username = request.forms.get('username')
    user = get_user(username)
    tile = get_terrain(user['longitude'],user['latitude'] )
    get_mini_map(user['longitude'],user['latitude'] )

    return template('navigate', tile=tile, user=user)

@route('/resources/:path#.+#', name='static')
def static(path):
    print "Returning static: " + path
    return static_file(path, root='')

@route('/north', method='POST')
def index():
    user_id = request.forms.get('user_id')
    user = move_north(user_id)
    tile = get_terrain(user['longitude'],user['latitude'] )

    return template('navigate', tile=tile, user=user)

@route('/east', method='POST')
def index():
    user_id = request.forms.get('user_id')
    user = move_east(user_id)
    tile = get_terrain(user['longitude'],user['latitude'] )

    return template('navigate', tile=tile, user=user)

@route('/south', method='POST')
def index():
    user_id = request.forms.get('user_id')
    user = move_south(user_id)
    tile = get_terrain(user['longitude'],user['latitude'] )

    return template('navigate', tile=tile, user=user)

@route('/west', method='POST')
def index():
    user_id = request.forms.get('user_id')
    user = move_west(user_id)
    tile = get_terrain(user['longitude'],user['latitude'] )

    return template('navigate', tile=tile, user=user)

run(host='localhost', port=8080)


