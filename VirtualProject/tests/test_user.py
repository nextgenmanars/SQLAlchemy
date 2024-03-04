import pytest
from database import session
from user import User


@pytest.fixture(scope="module")
def users():
    users = session.query(User).all()
    yield users
    session.rollback()
    session.close()


def test_query_user(users):
    for user in users:
        assert user.first_name.isalpha()
