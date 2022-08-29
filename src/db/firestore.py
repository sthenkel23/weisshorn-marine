from google.cloud import firestore
import os
# Authenticate to Firestore with the JSON account key.
db = firestore.Client.from_service_account_json("./g-cl.json")

# Create a reference to the Google post.
doc_ref = db.collection("marine-alerts").document("alerts")

# Then get the data at that reference.
doc = doc_ref.get()
