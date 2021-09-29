from app import create_app
from app.extensions import db

def test_get_version(app):
    response = app.test_client().get('api/version')
    assert response.status_code == 200
    assert response.json == {"version": 1.0}



if __name__=='__main__':

    app = create_app()
    test_get_version(app)

