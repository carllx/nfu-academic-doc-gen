# How To: Index From Series Copy

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test index from series copy

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.tests.copy_view.util`

**Setup Required:**
```python
# Fixtures: using_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series([1, 2])
```

**Verification:**
```python
assert np.shares_memory(get_array(ser), arr)
```

### Step 2: Assign idx = Index(...)

```python
idx = Index(ser, copy=True)
```

### Step 3: Assign arr = get_array(...)

```python
arr = get_array(ser)
```

### Step 4: Assign unknown = 100

```python
ser.iloc[0] = 100
```

**Verification:**
```python
assert np.shares_memory(get_array(ser), arr)
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write

# Workflow
ser = Series([1, 2])
idx = Index(ser, copy=True)
arr = get_array(ser)
ser.iloc[0] = 100
assert np.shares_memory(get_array(ser), arr)
```

## Next Steps


---

*Source: test_index.py:96 | Complexity: Intermediate | Last updated: 2026-06-02*