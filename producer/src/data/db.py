from google.cloud import firestore

# Authenticate to Firestore with the JSON account key.
db = firestore.Client.from_service_account_json("./gcl.json")

# Create a reference to the Google post.
collection = db.collection("alerts")
doc_ref = collection.document("data-posts")

# Then get the data at that reference.
doc = doc_ref.get()
