from app.extensions import db

class Connection():

    @staticmethod
    def get_connection():
        return db
