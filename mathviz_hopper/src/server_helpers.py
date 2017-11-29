#!/usr/bin/env python
import json
from bottle import Bottle, ServerAdapter
from bottle import route, run, post, request
import threading
import time

class MyWSGIRefServer(ServerAdapter):
    server = None

    def run(self, handler):
        from wsgiref.simple_server import make_server, WSGIRequestHandler
        if self.quiet:
            class QuietHandler(WSGIRequestHandler):
                def log_request(*args, **kw): pass
            self.options['handler_class'] = QuietHandler
        self.server = make_server(self.host, self.port, handler, **self.options)
        self.server.serve_forever()

    def stop(self):
        # self.server.server_close() <--- alternative but causes bad fd exception
        print "shutting down"
        self.server.shutdown()
    

if __name__ == '__main__':

    app = Bottle()

    @app.route('/settings')
    def hello():
        return json.dumps({"test": 8})

    @app.route('/query', method='POST')
    def query():
        print "query"
        print json.loads(request.body.read()).get("query")
        # print request.json.get("query")
        return "null"

    server = MyWSGIRefServer(host="localhost", port=8088)

    def begin():
        run(app, server=server)

    begin()

    # threading.Thread(target=begin).start()
    # time.sleep(10) # Shut down server after 2 seconds
    # server.stop()
