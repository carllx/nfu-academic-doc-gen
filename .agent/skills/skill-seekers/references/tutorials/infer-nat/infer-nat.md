# How To: Infer Nat

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test infer nat

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `decimal`
- `numpy`
- `pytest`
- `pandas._libs.tslibs.timezones`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: val
```

## Step-by-Step Guide

### Step 1: Assign values = value

```python
values = [NaT, val]
```

**Verification:**
```python
assert idx.dtype == 'datetime64[ns]' and idx.isna().all()
```

### Step 2: Assign idx = Index(...)

```python
idx = Index(values)
```

**Verification:**
```python
assert idx.dtype == 'datetime64[ns]' and idx.isna().all()
```

### Step 3: Assign idx = Index(...)

```python
idx = Index(values[::-1])
```

**Verification:**
```python
assert idx.dtype == 'datetime64[ns]' and idx.isna().all()
```

### Step 4: Assign idx = Index(...)

```python
idx = Index(np.array(values, dtype=object))
```

**Verification:**
```python
assert idx.dtype == 'datetime64[ns]' and idx.isna().all()
```

### Step 5: Assign idx = Index(...)

```python
idx = Index(np.array(values, dtype=object)[::-1])
```

**Verification:**
```python
assert idx.dtype == 'datetime64[ns]' and idx.isna().all()
```


## Complete Example

```python
# Setup
# Fixtures: val

# Workflow
values = [NaT, val]
idx = Index(values)
assert idx.dtype == 'datetime64[ns]' and idx.isna().all()
idx = Index(values[::-1])
assert idx.dtype == 'datetime64[ns]' and idx.isna().all()
idx = Index(np.array(values, dtype=object))
assert idx.dtype == 'datetime64[ns]' and idx.isna().all()
idx = Index(np.array(values, dtype=object)[::-1])
assert idx.dtype == 'datetime64[ns]' and idx.isna().all()
```

## Next Steps


---

*Source: test_index_new.py:57 | Complexity: Intermediate | Last updated: 2026-06-02*