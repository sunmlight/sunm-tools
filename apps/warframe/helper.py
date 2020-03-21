import requests
from django.conf import settings
import os


def get_wf_key():
    WFAPI = settings.WFAPI
    wfurl = WFAPI["BASE_URL"]
    url = WFAPI["BASE_URL"] + "/connect/token"
    data = {
        "client_id": WFAPI["ClientId"],
        "client_secret": WFAPI["ClientSecret"],
        "grant_type": "client_credentials",
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    req = requests.post(url, data=data, headers=headers)
