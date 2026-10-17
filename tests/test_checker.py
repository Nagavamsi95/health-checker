from unittest.mock import patch, MagicMock
import requests
from checker import check_endpoint


def test_up_when_status_is_200():
    fake = MagicMock(status_code=200)
    with patch("checker.requests.get", return_value=fake):
        result = check_endpoint({"name": "Test", "url": "https://example.com"})
    assert result["status"] == "UP"
    assert result["code"] == 200


def test_down_when_status_is_500():
    fake = MagicMock(status_code=500)
    with patch("checker.requests.get", return_value=fake):
        result = check_endpoint({"name": "Test", "url": "https://example.com"})
    assert result["status"] == "DOWN"
    assert result["code"] == 500


def test_down_when_connection_fails():
    with patch("checker.requests.get", side_effect=requests.RequestException("boom")):
        result = check_endpoint({"name": "Test", "url": "https://example.com"})
    assert result["status"] == "DOWN"
    assert result["code"] is None