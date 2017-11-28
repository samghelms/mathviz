from threading import Thread
from bottle import Bottle, route, run, post, request, response
from server_helpers import MyWSGIRefServer
import json

class Server:
    def __init__(self, obj):
        app = Bottle()
        self._setup_routing(app)
        self.server = MyWSGIRefServer(host="localhost", port=obj.port)
        self.index = obj.index
        self.settings = obj.settings
        def begin():
            run(app, server=self.server)
        Thread(target=begin).start()

    def __delete__(self):
        self.server.stop()

    def _setup_routing(self, app):

        @app.route('/settings')
        def settings():
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.content_type = 'application/json'
            return json.dumps(self.settings)

        @app.route('/query', method='POST')
        def query():
            query=json.loads(request.body.read()).get("query")
            return_val = self.index.query(query)
            print return_val
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Access-Control-Allow-Methods'] = 'POST'
            response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
            response.content_type = 'application/json'
            return json.dumps(return_val)

    