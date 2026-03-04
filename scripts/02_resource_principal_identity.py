#!/usr/bin/env python3
"""
02_resource_principal_identity.py

Purpose:
  Proves the notebook can authenticate to OCI using Resource Principal and call the Identity service.

Parameters to set:
  None

What it proves:
  - Resource Principal signer is working
  - Identity API calls succeed
"""

import oci
from oci.auth import signers

print("=== Resource Principal Identity Test ===")

signer = signers.get_resource_principals_signer()
print("Resource Principal signer: OK")

identity = oci.identity.IdentityClient(config={}, signer=signer)
tenancy = identity.get_tenancy(signer.tenancy_id).data

print("Tenancy Name:", tenancy.name)
print("Tenancy OCID:", tenancy.id)

print("\n✅ 02_resource_principal_identity passed.")