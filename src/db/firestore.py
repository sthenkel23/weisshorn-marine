from google.cloud import firestore

# Authenticate to Firestore with the JSON account key.
db = firestore.Client.from_service_account_json("gcloud.json")

# Create a reference to the Google post.
doc_ref = db.collection("marine-alerts").document("alerts")

# Then get the data at that reference.
doc = doc_ref.get()
