# Part 1 — Setup Prerequisites (Before Your First Notebook)

OCI Data Science notebooks authenticate using **Resource Principals**. That means the notebook session itself has an identity in OCI IAM.
If IAM is not configured correctly, your notebook won’t be able to access Object Storage (datasets / artifacts), networking resources, or other OCI services.

This document walks through the minimum setup steps.

---

## 1) Choose or Create a Compartment (Recommended)

Keep your AI resources in a dedicated compartment to simplify IAM scoping.

Example compartment name:
- `datascience`

**Console path**
- Identity & Security → Compartments → Create Compartment

---

## 2) Create a Dynamic Group (for notebooks)

Dynamic Groups are for **OCI resources** (not human users). Membership is automatic based on a **matching rule**.

**Console path (new IAM domains UI)**
- Identity & Security → Domains → Default → Dynamic Groups → Create Dynamic Group

**Example**
- Name: `dg_datascience_dev`
- Matching rule:

```
ALL {resource.type = 'datasciencenotebooksession'}
```

**What this does**
- Any Data Science Notebook Session becomes a member of this dynamic group automatically (no manual assignment).

---

## 3) Create Policies (grant the notebook permissions)

Policies define what the notebook is allowed to do.

**Console path**
- Identity & Security → Policies → Create Policy

**Best practice for labs**
- Create the policy in the **root compartment** and scope permissions to the target compartment(s).

### Minimum recommended policies (lab setup)

Replace the compartment name if you used something other than `datascience`.

```
Allow dynamic-group dg_datascience_dev to manage data-science-family in tenancy
Allow dynamic-group dg_datascience_dev to read objectstorage-namespaces in tenancy
Allow dynamic-group dg_datascience_dev to manage object-family in compartment datascience
```

**What these do**
- `data-science-family`: manage notebook sessions, jobs, model deployments
- `objectstorage-namespaces`: retrieve your tenancy Object Storage namespace (required for OS API calls)
- `object-family`: read/write buckets and objects in the compartment (datasets, outputs, artifacts)

---

## 4) Confirm Region Alignment

Object Storage and buckets are **regional**.

- Confirm the Console region (top-right)
- Create your bucket in the same region as your notebook session

---

## 5) Create a Test Bucket (Recommended)

**Console path**
- Storage → Object Storage & Archive Storage → Buckets → Create Bucket

Put it in your `datascience` compartment.

Example bucket name:
- `ds-unit-test`

---

## Common “setup” errors and what they usually mean

- **403 NotAuthorized** → missing/incorrect policy
- **404 BucketNotFound** → wrong region or wrong bucket name
- **404 NamespaceNotFound** → namespace not readable or policy not applied (often a dynamic-group rule issue)

---

✅ Once Part 1 is complete, move to **Part 2** and run the validation scripts.
