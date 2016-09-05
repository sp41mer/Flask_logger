import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, request

app = Flask(__name__)


@app.route('/log/', methods=['GET','POST'])
def write_to_log():
    method = request.method
    header = request.headers
    query = request.query_string.encode('utf-8')
    app.logger.info('{} REQUEST: \n'
                    'HEADERS:\n {}'
                    'QUERY STRING:\n {}\n'.format(method,header,query))
    return 'Logger_is_running'

@app.route('/')
def hello_world():
    return 'Hello world!'


if __name__ == '__main__':
    formatter = logging.Formatter("[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
    handler = RotatingFileHandler('/Users/sp41mer/PycharmProjects/Logger/log.log', maxBytes=10000000, backupCount=5)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.DEBUG)
    app.run()
