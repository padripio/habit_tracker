import requests
from datetime import datetime

today = datetime.now()
date = today.strftime("%Y%m%d")

USERNAME = "padre"
GRAPH_ID = "tracker"
headers = {"X-USER-TOKEN": "pietheta"}

add_pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}"
pixel_update_url = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{date}"
pixel_delete_url = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{date}"
create_user_url = "https://pixe.la/v1/users"


# if user doesnt exist

def create_user():
    create_user_json = {"token": "pietheta",
                        "username": "mkuu",
                        "agreeTermsOfService": "yes",
                        "notMinor": "yes"}
    response = requests.post(url=create_user_url, json=create_user_json)
    print(response.text)


def add_pixel():
    quantity = input("How many kms today ? \n")
    request_body = {
        "date": date,
        "quantity": quantity,

    }
    response = requests.post(url=add_pixel_endpoint, json=request_body, headers=headers)
    print(response.text)


def update_pixel():
    quantity = input("How many kms today ? \n")

    update_json = {
        "quantity": quantity
    }
    update_response = requests.put(url=pixel_update_url, json=update_json, headers=headers)
    print(update_response.text)


# delete a pixel
def delete_pixel():
    response = requests.delete(url=pixel_delete_url, headers=headers)
    print(response.text)


add_pixel()
