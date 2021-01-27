import pytest, os
from app import db, create_app
from app.models import Record


@pytest.fixture(scope="module")
def test_client():
    flask_app = create_app(os.getenv("TEST_ENV"))

    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            yield testing_client


@pytest.fixture(scope="module")
def init_database(test_client):
    db.create_all()

    test_record = Record(
        code="A00", desc_short="", desc_long="", type="ICD-10", year="2019"
    )
    db.session.add(test_record)
    db.session.commit()

    yield

    db.drop_all()
