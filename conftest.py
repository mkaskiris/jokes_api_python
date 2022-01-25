import pytest
import app
from controllers import jokes

@pytest.fixture
def api(monkeypatch):
    test_jokes = [
        {'id': 6, 'joke': 'Test Joke 1', 'punchline': 'lol'},
        {'id': 7, 'name': 'Test Joke 2', 'punchline': 'lmao'}
    ]
    monkeypatch.setattr(jokes, "jokes", test_jokes)
    api = app.app.test_client()
    return api