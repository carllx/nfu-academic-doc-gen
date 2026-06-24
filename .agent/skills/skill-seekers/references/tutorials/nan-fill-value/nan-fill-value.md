# How To: Nan Fill Value

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test nan fill value

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas.core.arrays.sparse`

**Setup Required:**
```python
# Fixtures: raw_data, max_expected, min_expected
```

## Step-by-Step Guide

### Step 1: Assign arr = SparseArray(...)

```python
arr = SparseArray(raw_data)
```

**Verification:**
```python
assert max_result in max_expected
```

### Step 2: Assign max_result = arr.max(...)

```python
max_result = arr.max()
```

**Verification:**
```python
assert min_result in min_expected
```

### Step 3: Assign min_result = arr.min(...)

```python
min_result = arr.min()
```

**Verification:**
```python
assert np.isnan(max_result)
```

### Step 4: Assign max_result = arr.max(...)

```python
max_result = arr.max(skipna=False)
```

**Verification:**
```python
assert np.isnan(min_result)
```

### Step 5: Assign min_result = arr.min(...)

```python
min_result = arr.min(skipna=False)
```

**Verification:**
```python
assert max_result in max_expected
```


## Complete Example

```python
# Setup
# Fixtures: raw_data, max_expected, min_expected

# Workflow
arr = SparseArray(raw_data)
max_result = arr.max()
min_result = arr.min()
assert max_result in max_expected
assert min_result in min_expected
max_result = arr.max(skipna=False)
min_result = arr.min(skipna=False)
if np.isnan(raw_data).any():
    assert np.isnan(max_result)
    assert np.isnan(min_result)
else:
    assert max_result in max_expected
    assert min_result in min_expected
```

## Next Steps


---

*Source: test_reductions.py:207 | Complexity: Intermediate | Last updated: 2026-06-02*