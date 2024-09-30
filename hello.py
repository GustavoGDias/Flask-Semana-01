# A very simple Flask Hello World app for you to get started with...
from flask import Flask, request, make_response, redirect, abort;
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1)';


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}</h1)'.format(name)

@app.route('/contextorequisicao')
def contextorequisicao():
    user_agent = request.headers.get('User-Agent');
    return '<p>Your Browser is {}</p>' .format(user_agent);
    
@app.route('/codigostatusdiferente')
def condigostatusdiferente():
    return '<p>Bad request</p>', 400;
    
@app.route('/objetoresposta')
def objetoresposta():
    response = make_response('<h1>This document carries a cookie!</h1>');
    response.set_cookie ('answer', '4.2');
    return response

@app.route('/redirecionamento')
def redirecionamento ():
    return redirect ('https://ptb.ifsp.edu.br');

@app.route('/abortar')
def abortar():
    abort(404);