from flask import Blueprint, request, render_template, make_response, jsonify
from .utils import generateCookie, checkCookie
userApp = Blueprint('userApp', __name__)

@userApp.route('/', methods=['GET'])
@userApp.route('/login', methods=['GET', 'POST'])
def user_login():
    if request.method == 'POST':
        cookieee = generateCookie()
        resp = make_response(render_template('home.html', loggedin=True))
        resp.set_cookie('session', cookieee)
        return resp
    return render_template('home.html', loggedin=False)

@userApp.route('/get-flag', methods=['GET'])
def get_flag():
    if request.cookies.get('session'):
        if checkCookie(request.cookies.get('session')):
            return jsonify({'flag': 'sudo{0hH_734H_1_@m_Fa$t3r_7|-|@n_fL4$h}'})
    return jsonify({'flag': 'You are too late !!'})