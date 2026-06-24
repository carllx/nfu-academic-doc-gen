# How To: Fillna Copy Frame

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test fillna copy frame

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.arrays`
- `pandas.tests.extension`

**Setup Required:**
```python
# Fixtures: data_missing, using_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign arr = data_missing.take(...)

```python
arr = data_missing.take([1, 1])
```

**Verification:**
```python
assert df.values.base is result.values.base
```

### Step 2: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame({'A': arr}, copy=False)
```

**Verification:**
```python
assert df.values.base is not result.values.base
```

### Step 3: Assign filled_val = value

```python
filled_val = df.iloc[0, 0]
```

**Verification:**
```python
assert df.A._values.to_dense() is arr.to_dense()
```

### Step 4: Assign result = df.fillna(...)

```python
result = df.fillna(filled_val)
```

**Verification:**
```python
assert df.A._values.to_dense() is arr.to_dense()
```


## Complete Example

```python
# Setup
# Fixtures: data_missing, using_copy_on_write

# Workflow
arr = data_missing.take([1, 1])
df = pd.DataFrame({'A': arr}, copy=False)
filled_val = df.iloc[0, 0]
result = df.fillna(filled_val)
if hasattr(df._mgr, 'blocks'):
    if using_copy_on_write:
        assert df.values.base is result.values.base
    else:
        assert df.values.base is not result.values.base
assert df.A._values.to_dense() is arr.to_dense()
```

## Next Steps


---

*Source: test_sparse.py:280 | Complexity: Intermediate | Last updated: 2026-06-02*