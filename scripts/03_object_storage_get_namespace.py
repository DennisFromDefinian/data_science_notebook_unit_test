#!/usr/bin/env python3
"""
03_object_storage_get_namespace.py

Purpose:
  Confirms Object Storage service is reachable and you can retrieve the tenancy Object Storage namespace.

Parameters to set:
  None

Notes:
  - Uses OCI_REGION if present; otherwise falls back to 'us-ashburn-1'
  - Here is the list of common US OCI Regions:
      us-ashburn-1
      us-chicago-1
      us-phoenix-1
      us-sanjose-1

"""

import os
import oci
from oci.auth import signers

print("=== Object Storage Namespace Test ===")

region = os.getenv("OCI_REGION") or "us-ashburn-1"
print("Region:", region)

signer = signers.get_resource_principals_signer()
os_client = oci.object_storage.ObjectStorageClient({"region": region}, signer=signer)

namespace = os_client.get_namespace().data
print("Namespace:", namespace)

print("\n✅ 03_object_storage_get_namespace passed.")