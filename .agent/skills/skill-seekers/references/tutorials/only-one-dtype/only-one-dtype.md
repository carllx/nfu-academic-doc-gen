# How To: Only One Dtype

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test only one dtype

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `ctypes`
- `math`
- `pytest`
- `pandas`

**Setup Required:**
```python
# Fixtures: test_data, df_from_dict
```

## Step-by-Step Guide

### Step 1: Assign columns = list(...)

```python
columns = list(test_data.keys())
```

**Verification:**
```python
assert null_count == 0
```

### Step 2: Assign df = df_from_dict(...)

```python
df = df_from_dict(test_data)
```

**Verification:**
```python
assert isinstance(null_count, int)
```

### Step 3: Assign dfX = df.__dataframe__(...)

```python
dfX = df.__dataframe__()
```

**Verification:**
```python
assert dfX.get_column_by_name(column).size() == column_size
```

### Step 4: Assign column_size = len(...)

```python
column_size = len(test_data[columns[0]])
```

**Verification:**
```python
assert dfX.get_column_by_name(column).offset == 0
```

### Step 5: Assign null_count = value

```python
null_count = dfX.get_column_by_name(column).null_count
```

**Verification:**
```python
assert null_count == 0
```


## Complete Example

```python
# Setup
# Fixtures: test_data, df_from_dict

# Workflow
columns = list(test_data.keys())
df = df_from_dict(test_data)
dfX = df.__dataframe__()
column_size = len(test_data[columns[0]])
for column in columns:
    null_count = dfX.get_column_by_name(column).null_count
    assert null_count == 0
    assert isinstance(null_count, int)
    assert dfX.get_column_by_name(column).size() == column_size
    assert dfX.get_column_by_name(column).offset == 0
```

## Next Steps


---

*Source: test_spec_conformance.py:31 | Complexity: Intermediate | Last updated: 2026-06-02*