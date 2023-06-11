#!/usr/bin/python
import socketio

sio = socketio.Client()

@sio.event
def connect():
    print("I'm connected!")

@sio.event
def connect_error():
    print("The connection failed!")

@sio.event
def message(data):
    print('I received a message!')

@sio.on("chat message")
def on_message(data):
    try:
        print('Data: ', data)
    except:
        print("Hata Oluştu")


sio.connect('http://localhost:3000')
