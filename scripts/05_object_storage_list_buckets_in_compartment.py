#!/usr/bin/env python3
"""
05_object_storage_list_buckets_in_compartment.py

Purpose:
  Lists buckets in a specific compartment.
  This is useful to validate:
    - Your dynamic group/policy scope
    - You are using the correct compartment OCID
    - You are in the correct region

Parameters to set (REQUIRED):
  COMPARTMENT_OCID: OCID of the compartment that contains the bucket(s)

How to find COMPARTMENT_OCID:
  OCI Console -> Identity & Security -> Compartments -> <your compartment> -> OCID

Optional parameters:
  REGION: If not set, uses OCI_REGION or defaults to 'us-ashburn-1'.
"""

import os
import oci
from oci.auth import signers
from oci.exceptions import ServiceError

# ====== REQUIRED: EDIT THIS ======
COMPARTMENT_OCID = "REPLACE_ME"  # e.g., "ocid1.compartment.oc1..aaaa..."
# ================================

REGION = os.getenv("OCI_REGION") or "us-ashburn-1"

print("=== List Buckets in Compartment Test ===")
print("Region:", REGION)
print("Compartment OCID:", COMPARTMENT_OCID)

signer = signers.get_resource_principals_signer()
os_client = oci.object_storage.ObjectStorageClient({"region": REGION}, signer=signer)

namespace = os_client.get_namespace().data
print("Namespace:", namespace)

try:
    buckets = os_client.list_buckets(namespace, COMPARTMENT_OCID).data
    print("\nBuckets:")
    for b in buckets:
        print("-", b.name)
    print(f"\n✅ Listed {len(buckets)} bucket(s).")
except ServiceError as e:
    print("\n❌ list_buckets failed")
    print("Status:", e.status)
    print("Code:", e.code)
    print("Message:", e.message)
    raise