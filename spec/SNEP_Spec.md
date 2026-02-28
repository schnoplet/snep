\# SNEP Spec v0.1



\## URI scheme



`snep://<authority>/<collection>/<id>@<version>`



Secure variant:



`sneps://...` → signed + revocable + provenance-enabled



\## Headers (HTTP fallback)



X-SNEP-Version: 0.1
X-SNEP-Capabilities: query,subscribe,patch
X-SNEP-Provenance: did:web:alice.example
X-SNEP-Permissions: cap://alice.example/recipes/42/read