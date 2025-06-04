from __future__ import annotations
import requests
from requests.auth import AuthBase
import json
from datetime import datetime
from robot.api import logger



class BearerAuth(requests.auth.AuthBase):


    def __init__(self, token):
        self.token = token
    def __call__(self, r):
        r.headers["Authorization"] = "Bearer " + self.token
        return r

class Sheetdb:
    def __init__(self, url: str, api_token: str):
        self.url = url
        self.auth = BearerAuth(api_token)



    def get_content(self):
        # return a list of data from sheet
        # https://docs.sheetdb.io/sheetdb-api/read#get-content
        res = self.get()
        return res

    def create_content(self, data: list):
        # create content like [{'id': 4,'name': "Mark"},{'id': 5,'name': "Susan"}]
        # https://docs.sheetdb.io/sheetdb-api/create
        res = self.post(data)
        return res

    def update_content(self, column_name: str, value: any, data: dict):
        # return a list of data from sheet
        # https://docs.sheetdb.io/sheetdb-api/update
        endpoint = f'/{column_name}/{value}'
        res = self.patch(endpoint, data)
        return res

    def delete_content(self, column_name: str, value: any):
        # return a list of data from sheet
        # https://docs.sheetdb.io/sheetdb-api/delete
        endpoint = f'/{column_name}/{value}'
        res = self.delete(endpoint)
        return res

    # Actual API calls
    def get(self):
        url = self.url
        response = requests.get(url, auth=self.auth)
        # logger.console(f"\nResponse:\n\n{response.text}\n\n")
        response.raise_for_status()
        return response.json()

    def post(self, data: list):
        url = self.url
        response = requests.post(url, auth=self.auth, json=data)
        # logger.console(f"\nResponse:\n\n{response.text}\n\n")
        response.raise_for_status()
        return response.json()

    def patch(self, endpoint: str, data: dict):
        url = self.url + endpoint
        response = requests.patch(url, auth=self.auth, json=data)
        # logger.console(f"\nResponse:\n\n{response.text}\n\n")
        response.raise_for_status()
        return response.json()
    
    def delete(self, endpoint: str):
        url = self.url + endpoint
        response = requests.delete(url, auth=self.auth)
        # logger.console(f"\nResponse:\n\n{response.text}\n\n")
        response.raise_for_status()
        return response.json()