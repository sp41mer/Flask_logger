import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def hello_world():
    method = request.method
    header = request.headers
    query = request.query_string.decode('utf-8')
    app.logger.info('{} REQUEST: \n'
                    'HEADERS:\n {}'
                    'QUERY STRING:\n {}\n'.format(method,header,query))
    return 'Logger_is_running'


if __name__ == '__main__':
    formatter = logging.Formatter("[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
    handler = RotatingFileHandler('/Users/sp41mer/PycharmProjects/Logger/foo.log', maxBytes=10000000, backupCount=5)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.DEBUG)
    app.run()
