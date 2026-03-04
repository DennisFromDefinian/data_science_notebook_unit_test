# OCI Data Science: Setup + Validation (Resource Principal Unit Tests)

This repo is a practical, copy/paste-friendly guide for getting OCI Data Science working **the right way**:
- **Part 1: Setup** IAM + networking prerequisites before your first notebook session
- **Part 2: Validation** small unit test scripts to confirm auth, IAM, and Object Storage access

## Repository Structure

```
.
├── README.md
├── docs/
│   ├── 01_setup_prerequisites.md
│   └── 02_validation_unit_tests.md
└── scripts/
    ├── 01_env_sanity_check.py
    ├── 02_resource_principal_identity.py
    ├── 03_object_storage_get_namespace.py
    ├── 04_object_storage_get_bucket.py
    ├── 05_object_storage_list_buckets_in_compartment.py
    └── 06_object_storage_put_and_get_object.py
```

## Quick Start

1. Follow **docs/01_setup_prerequisites.md**
2. Launch a Notebook Session
3. Run the scripts in order (see **docs/02_validation_unit_tests.md**)

## Who this is for

- OCI learners
- Data engineers onboarding to OCI
- AI/ML practitioners validating cloud foundations
- Platform teams building reproducible environments
