# Part 2 — Validation Unit Tests (Run from a Notebook Session)

These scripts are intentionally small and isolated so failures are easy to diagnose.
Together they validate the foundation of cloud-based data science:

**Authentication → Authorization → Storage → Data → Model**

---

## Recommended Execution Order

1. `01_env_sanity_check.py`
2. `02_resource_principal_identity.py`
3. `03_object_storage_get_namespace.py`
4. `04_object_storage_get_bucket.py`
5. `06_object_storage_put_and_get_object.py`
6. `05_object_storage_list_buckets_in_compartment.py` (optional deeper validation)

---

## Script-by-script explanation

### 01_env_sanity_check.py
Confirms Python runtime, common OCI env vars, DNS, and outbound HTTPS. Helps catch VCN/subnet routing issues early.

### 02_resource_principal_identity.py
**Resource Principal authentication** means your notebook session has an OCI IAM identity (no API keys / no secrets).
This test calls the **Identity service** (OCI IAM control plane) to prove:
- the notebook can authenticate
- OCI IAM is reachable
- policies can be evaluated for this principal

If this fails, nothing else will work reliably.

### 03_object_storage_get_namespace.py
Confirms Object Storage API access and retrieves your tenancy’s **Object Storage namespace** (tenancy-wide identifier required for OS API calls).

### 04_object_storage_get_bucket.py
Confirms you can access **one specific bucket** by name. This is the most direct “do I have access to this bucket?” check.

### 05_object_storage_list_buckets_in_compartment.py (optional)
Lists buckets in a specific compartment. Use when diagnosing:
- wrong compartment OCID
- region mismatch
- IAM scoping errors

**Can it replace test 04?**
- Not really. Test 04 is a targeted check for a known bucket.
- Test 05 is a broader diagnostic tool.

### 06_object_storage_put_and_get_object.py
Performs an end-to-end Object Storage read/write:
- **PUT** = write an object
- **GET** = read it back

This validates that you have permission to both **insert into** and **pull from** the bucket, which is typically required for:
- training data reads
- artifact/model writes
- batch scoring outputs

**OBJECT_PREFIX**
Object Storage is flat (no real folders). Prefixes (like `unit-test/`) are just part of the object name and help organize test artifacts for easy cleanup.

---

## Common error meanings

- **403 NotAuthorized** → policy missing or dynamic group not matching notebook sessions
- **404 BucketNotFound** → wrong region or bucket name typo
- **404 NamespaceNotFound** → namespace permission missing or policy not applying

---

✅ If all scripts pass, your notebook is correctly wired to OCI IAM + Object Storage and you’re ready for real work.
