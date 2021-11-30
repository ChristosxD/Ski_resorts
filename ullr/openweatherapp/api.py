import requests
from requests import Response
from rest_framework.exceptions import ValidationError as DRFValidationError

class Requester:
    """https://api.openweathermap.org/data/2.5/onecall?lat=37.983810&lon=23.727539&appid=160e12886e46d433e48f8db9d0b976c2&lang=el"""
    _base_url: str = "https://api.openweathermap.org/data/2.5/"

    def _get_access_token(self):
        return {"token": "160e12886e46d433e48f8db9d0b976c2"}

    def _validate_response(self, response: Response) -> dict:
        try:
            response.raise_for_status()
        except Exception as e:
            raw_data = response.json()
            raise DRFValidationError(e)
        return response.json()

    def get(self, endpoint: str, params: dict = {}) -> dict:
        token_data: dict = self._get_access_token()
        token_params = params
        token_params["appid"] = token_data["token"]
        response: Response = requests.get(f'{self._base_url}{endpoint}', params=token_params, headers={})
        return self._validate_response(response)

    def post(self, endpoint: str, data: dict) -> dict:
        token_data: dict = self._get_access_token()
        response: Response = requests.post(f'{self._base_url}{endpoint}', json=data, headers={})
        return self._validate_response(response)


class OWAOneCall(Requester):

    def __init__(self, lon: float, lat: float):
        self._lon = lon
        self._lat = lat
        self._endpoint = "onecall"

    def create_payload(self, data: dict):
        """This api endpoint doesn't need any payload."""
        ...

    def make_request(self) -> dict:
        params: dict = {
            "lat": self._lat,
            "lon": self._lon
        }
        response_body: dict = self.get(params=params, endpoint=self._endpoint)
        return response_body

