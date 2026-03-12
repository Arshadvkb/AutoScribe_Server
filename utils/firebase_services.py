import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import auth

cred = credentials.Certificate("utils\\ainotegenerator-firebase-adminsdk-fbsvc-5421873e66.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
auth_client = auth

def get_all_users():
    # .iterate_all() automatically fetches the next page when needed
    all_users_iterator = auth.list_users().iterate_all()
    
    users_data = []
    
    for user in all_users_iterator:
        # Each 'user' is a UserRecord object
        users_data.append({
            "uid": user.uid,
            "email": user.email,
            "display_name": user.display_name,
            "last_sign_in": user.user_metadata.last_sign_in_timestamp
        })
    
    return users_data

# Run it
all_my_users = get_all_users()
print(f"Found {all_my_users} users.")
