import sys
import pytest

sys.path.append('..')

from app import *

@pytest.fixture
def app():
    print "initing app"
    return app

# @pytest.fixture
# def test_client(app):
# 	return app.test_client()

