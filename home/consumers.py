from channels.generic.websocket import WebSocketConsumer



class TestConsumer(WebSocketConsumer):
    
    def connect(self):
        pass
    
    def receive(self):
        pass
    
    def disconnect(self):
        pass
    
    