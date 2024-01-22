import configuration
import requests
import data

def log_in_user():
    return requests.post(configuration.URL_SERVICE,
                         headers=data.headers,
                         json=data.order_body)

responce = log_in_user()


def test_positive_assert():
     assert responce.status_code == 200
     assert responce.json()['canPassTest'] != ''