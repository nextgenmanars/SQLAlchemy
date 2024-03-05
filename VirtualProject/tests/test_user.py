import pytest
from database import session
from user import User


@pytest.fixture(scope="module")
def db_session():
    create_session = session
    yield create_session
    session.rollback()
    session.close()


@pytest.fixture(scope="module")
def user(db_session):
    user_id = 1
    user = db_session.query(User).get(user_id)
    return user


def test_query_user(user):
    assert user.first_name == "Dmitriy"
