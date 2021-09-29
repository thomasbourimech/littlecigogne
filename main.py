from app import create_app
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import logging
logging.basicConfig(filename='flask_app.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

flask_app = create_app()
db = SQLAlchemy(flask_app)
ma = Marshmallow(flask_app)


if __name__ == '__main__':
    flask_app.run(debug=True, threaded=True, host="127.0.0.1", port=8080)
