import os
from pathlib import Path

import firebase_admin
from firebase_admin import auth, credentials, firestore

_DEFAULT_CRED_ENV = "FIREBASE_ADMIN_CREDENTIALS"
_app_initialized = False


def _init_firebase():
    global _app_initialized
    if _app_initialized:
        return

    cred_path = os.getenv(_DEFAULT_CRED_ENV)
    if not cred_path:
        raise RuntimeError(
            f"Missing {_DEFAULT_CRED_ENV} environment variable for Firebase credentials."
        )

    cred_file = Path(cred_path)
    if not cred_file.exists():
        raise FileNotFoundError(f"Firebase credentials not found: {cred_file}")

    cred = credentials.Certificate(str(cred_file))
    firebase_admin.initialize_app(cred)
    _app_initialized = True


def get_db():
    _init_firebase()
    return firestore.client()


def get_auth():
    _init_firebase()
    return auth


def get_all_users():
    auth_client = get_auth()
    all_users_iterator = auth_client.list_users().iterate_all()

    users_data = []
    for user in all_users_iterator:
        users_data.append(
            {
                "uid": user.uid,
                "email": user.email,
                "display_name": user.display_name,
                "last_sign_in": user.user_metadata.last_sign_in_timestamp,
            }
        )
    print(f"Retrieved {len(users_data)} users from Firebase Authentication.")
    return users_data


if __name__ == "__main__":
    try:
        from dotenv import load_dotenv

        load_dotenv()
    except Exception:
        pass

    get_all_users()
