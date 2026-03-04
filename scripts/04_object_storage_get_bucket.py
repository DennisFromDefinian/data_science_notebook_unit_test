#!/usr/bin/env python3
"""
04_object_storage_get_bucket.py

Purpose:
  Checks access to ONE specific bucket by name (no listing required).
  This is the cleanest "do I have access to that bucket?" test.

Parameters to set (REQUIRED):
  BUCKET_NAME: The exact bucket name as shown in the OCI Console.

Optional parameters:
  REGION: If not set, uses OCI_REGION or defaults to 'us-ashburn-1'.
"""

import os
import oci
from oci.auth import signers
from oci.exceptions import ServiceError

# ====== REQUIRED: EDIT THIS ======
BUCKET_NAME = "REPLACE_ME"
# ================================

REGION = os.getenv("OCI_REGION") or "us-ashburn-1"

print("=== Get Bucket Test ===")
print("Region:", REGION)
print("Bucket:", BUCKET_NAME)

signer = signers.get_resource_principals_signer()
os_client = oci.object_storage.ObjectStorageClient({"region": REGION}, signer=signer)

namespace = os_client.get_namespace().data
print("Namespace:", namespace)

try:
    b = os_client.get_bucket(namespace, BUCKET_NAME).data
    print("\n✅ Bucket access successful")
    print("Bucket Name:", b.name)
    print("Bucket Compartment OCID:", b.compartment_id)
except ServiceError as e:
    print("\n❌ Bucket access failed")
    print("Status:", e.status)
    print("Code:", e.code)
    print("Message:", e.message)
    raise