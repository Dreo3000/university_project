import os
import cherrypy
import quizgen


correct_answer = 0

class Root(object):
    @cherrypy.expose
    def index(self):
        return "test server"

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def get_question(self):
        return quizgen.get_data()

    def check_correctanswer(self):
        return None


if __name__ == '__main__':
    conf = {
        'global': {
            'server.socket_port': 9090,
        },
        '/': {
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Access-Control-Allow-Origin', '*')],
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
    }
    cherrypy.quickstart(Root(), '/', conf)
