#!/usr/bin/env python3
"""
06_object_storage_put_and_get_object.py

Purpose:
  End-to-end Object Storage test:
    - Writes a small JSON object to a bucket
    - Reads it back
  This is a great final "unit test" proving IAM + Object Storage actually work.

Parameters to set (REQUIRED):
  BUCKET_NAME: Target bucket name
  OBJECT_PREFIX: Optional prefix "folder" in the bucket

Optional parameters:
  REGION: If not set, uses OCI_REGION or defaults to 'us-ashburn-1'.
"""

import os
import json
import time
from datetime import datetime

import oci
from oci.auth import signers
from oci.exceptions import ServiceError

# ====== REQUIRED: EDIT THIS ======
BUCKET_NAME = "REPLACE_ME"       # e.g., "bucket-1234"
OBJECT_PREFIX = "unit-test"      # e.g., "unit-test" or "healthcheck" or leave blank ""
# ================================

REGION = os.getenv("OCI_REGION") or "us-ashburn-1"

print("=== Put/Get Object Test ===")
print("Region:", REGION)
print("Bucket:", BUCKET_NAME)

signer = signers.get_resource_principals_signer()
os_client = oci.object_storage.ObjectStorageClient({"region": REGION}, signer=signer)

namespace = os_client.get_namespace().data
print("Namespace:", namespace)

key = f"{OBJECT_PREFIX}/hello-{int(time.time())}.json"
payload = {
    "msg": "hello from OCI Data Science notebook",
    "utc": datetime.utcnow().isoformat() + "Z",
}

try:
    # PUT
    os_client.put_object(
        namespace,
        BUCKET_NAME,
        key,
        json.dumps(payload).encode("utf-8"),
        content_type="application/json",
    )
    print("\n✅ PUT OK:", f"{BUCKET_NAME}/{key}")

    # GET
    resp = os_client.get_object(namespace, BUCKET_NAME, key)
    text = resp.data.content.decode("utf-8")
    print("✅ GET OK:", text)

    print("\n✅ 06_object_storage_put_and_get_object passed.")
except ServiceError as e:
    print("\n❌ Put/Get failed")
    print("Status:", e.status)
    print("Code:", e.code)
    print("Message:", e.message)
    raise