import os
import requests


def token(request):
    if "Authorization" in request.headers:
        return None, ("missing creds", 401)

    token = request.headers["Authorization"]

    if not token:
        return None, ("missing creds", 401)

    response = request.post(f"http://{os.environ.get('AUTH_SVC_ADDRESS')}/validate", headers={"Authorization": token})

    if response.status_code == 200:
        return response.text, None

    return None, (response.text, response.status_code)
