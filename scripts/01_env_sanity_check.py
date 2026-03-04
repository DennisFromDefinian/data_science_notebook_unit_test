#!/usr/bin/env python3
"""
01_env_sanity_check.py

Purpose:
  Basic sanity check for a brand-new OCI Data Science notebook session:
  - Confirms Python runtime
  - Confirms environment variables commonly present in OCI
  - Confirms DNS + outbound HTTPS connectivity (optional but very helpful)

Parameters to set:
  None
"""

import os
import sys
import socket
import urllib.request
from datetime import datetime

print("=== Environment Sanity Check ===")
print("Python:", sys.version)
print("UTC Time:", datetime.utcnow().isoformat(), "UTC")

print("\n=== OCI Environment Variables (if present) ===")
for k in [
    "OCI_REGION",
    "REGION",
    "OCI_RESOURCE_PRINCIPAL_VERSION",
    "OCI_RESOURCE_PRINCIPAL_RPST",
    "OCI_RESOURCE_PRINCIPAL_PRIVATE_PEM",
]:
    v = os.getenv(k)
    print(f"{k}: {'(set)' if v else '(not set)'}")

print("\n=== DNS Check ===")
print("oracle.com ->", socket.gethostbyname("oracle.com"))

print("\n=== HTTPS Check ===")
with urllib.request.urlopen("https://www.oracle.com", timeout=10) as r:
    print("GET https://www.oracle.com -> HTTP", r.status)

print("\n✅ 01_env_sanity_check passed.")