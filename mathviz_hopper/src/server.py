from threading import Thread
from bottle import Bottle, route, run, post, request, response
from server_helpers import MyWSGIRefServer
import json

class Server:
    def __init__(self, obj):
        app = Bottle()
        self._setup_routing(app)
        self.server = MyWSGIRefServer(host="localhost", port=obj.port)
        self.obj=obj
        def begin():
            run(app, server=self.server)
        Thread(target=begin).start()

    def __delete__(self):
        self.server.stop()

    def _setup_routing(self, app):
        # @app.hook('after_request')
        # def enable_cors():
        #     """
        #     You need to add some headers to each request.
        #     Don't use the wildcard '*' for Access-Control-Allow-Origin in production.
        #     """
        #     response.headers['Access-Control-Allow-Origin'] = '*'
        #     response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
        #     response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

        @app.route('/settings')
        def settings():
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.content_type = 'application/json'
            return json.dumps(self.obj.settings)

        @app.route('/query', method='POST')
        def query():
            response.headers['Access-Control-Allow-Origin'] = '*'
            query=json.loads(request.body.read()).get("query")
            query=self.obj.converter(query)
            sims = self.obj.index[query]
            neighbors = sorted(sims, key=lambda item: -item[1])
            neighbors = {"neighbors":[{"neighbor": self.obj.docs[n[0]], "similarity_score": float(n[1])} for n in neighbors]} if neighbors else {"neighbors": []}
            response.content_type = 'application/json'
            return neighbors

    