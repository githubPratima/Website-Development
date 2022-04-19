import pytest
from bs4 import BeautifulSoup


@pytest.fixture()
def app():
    from ..main import create_app
    app = create_app()
    """app.config.update({
        "TESTING": True,
    })"""

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


def test_post_add_basic(client):
    response = client.post("/mycalc/", data={"eq": "7+7"})
    print(response.data)
    assert b"value=\"14\"" in response.data


def test_post_add(client):
    response = client.post("/mycalc/", data={"eq": "7+7"})
    html = response.data.decode("UTF-8")
    # string to soup
    soup = BeautifulSoup(html, 'html.parser')
    # find the <input> tag with id "result"
    result_ele = soup.find(id="result")
    # get the value attribute of the input tag
    assert result_ele.get("value") == "14"

def test_post_sub_basic(client):
    response = client.post("/mycalc/", data={"eq": "9-2"})
    print(response.data)
    assert b"value=\"7\"" in response.data


def test_post_sub(client):
    response = client.post("/mycalc/", data={"eq": "9-2"})
    html = response.data.decode("UTF-8")
    soup = BeautifulSoup(html, 'html.parser')
    result_ele = soup.find(id="result")
    assert result_ele.get("value") == "7"

def test_post_mult_basic(client):
    response = client.post("/mycalc/", data={"eq": "3x3"})
    print(response.data)
    assert b"value=\"9\"" in response.data


def test_post_mult(client):
    response = client.post("/mycalc/", data={"eq": "3x3"})
    html = response.data.decode("UTF-8")
    soup = BeautifulSoup(html, 'html.parser')
    result_ele = soup.find(id="result")
    assert result_ele.get("value") == "9"


def test_post_divide_basic(client):
    response = client.post("/mycalc/", data={"eq": "9/3"})
    print(response.data)
    assert b"value=\"3.0\"" in response.data


def test_post_divide(client):
    response = client.post("/mycalc/", data={"eq": "9/3"})
    html = response.data.decode("UTF-8")
    soup = BeautifulSoup(html, 'html.parser')
    result_ele = soup.find(id="result")
    assert result_ele.get("value") == "3.0"

# https://www.twilio.com/blog/web-scraping-and-parsing-html-in-python-with-beautiful-soup
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# https://stackabuse.com/convert-bytes-to-string-in-python/