import os
import firebase_admin
from firebase_admin import credentials, auth
from rest_framework import exceptions


class Firebase:
    path = os.getenv("CREDENTIAL_PATH", "./service_account.json")
    cred = credentials.Certificate(path)
    app = firebase_admin.initialize_app(cred)

    def create_user(self, user):
        client = auth._get_client(self.app)
        client._user_manager.create_user(
            uid=str(user.id), phone_number=user.phone
        )

    def verify_token(self, token):
        decoded_token = auth.verify_id_token(token)
        uid = decoded_token["uid"]
        return uid

    def verify_phone(self, phone):
        user = auth.get_user_by_phone_number(phone)
        return user

    def update_user(self, user):
        auth.update_user(
            uid=str(user.id), phone_number=user.phone
        )

    def delete_user(self, user):
        auth.delete_user(
            uid=str(user.id)
        )
