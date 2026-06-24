# How To: Mixed Dtypes

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate df_from_dict: test mixed dtypes

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `ctypes`
- `math`
- `pytest`
- `pandas`

**Setup Required:**
```python
# Fixtures: df_from_dict
```

## Step-by-Step Guide

### Step 1: Assign df = df_from_dict(...)

```python
df = df_from_dict({'a': [1, 2, 3], 'b': [3, 4, 5], 'c': [1.5, 2.5, 3.5], 'd': [9, 10, 11], 'e': [True, False, True], 'f': ['a', '', 'c']})
```


## Complete Example

```python
# Setup
# Fixtures: df_from_dict

# Workflow
df = df_from_dict({'a': [1, 2, 3], 'b': [3, 4, 5], 'c': [1.5, 2.5, 3.5], 'd': [9, 10, 11], 'e': [True, False, True], 'f': ['a', '', 'c']})
```

## Next Steps


---

*Source: test_spec_conformance.py:46 | Complexity: Beginner | Last updated: 2026-06-02*