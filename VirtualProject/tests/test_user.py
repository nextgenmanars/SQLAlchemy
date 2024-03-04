import pytest
from database import session
from user import User


@pytest.fixture(scope="module")
def db_session():
    create_session = session
    yield create_session
    session.rollback()
    session.close()


def test_query_user(db_session):
    user = db_session.query(User).filter_by(id=1).first()
    assert user.id == 1