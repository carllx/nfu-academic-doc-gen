# How To: Series From Series With Reindex

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test series from series with reindex

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.copy_view.util`

**Setup Required:**
```python
# Fixtures: using_copy_on_write, warn_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series([1, 2, 3], name='name')
```

**Verification:**
```python
assert np.shares_memory(ser.values, result.values)
```

### Step 2: Assign result = Series(...)

```python
result = Series(ser, index=[0, 1, 2, 3])
```

**Verification:**
```python
assert ser.iloc[0] == 1
```

### Step 3: Assign result = Series(...)

```python
result = Series(ser, index=index)
```

**Verification:**
```python
assert ser.iloc[0] == 0
```

### Step 4: Assign unknown = 0

```python
result.iloc[0] = 0
```

**Verification:**
```python
assert not np.shares_memory(ser.values, result.values)
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write, warn_copy_on_write

# Workflow
ser = Series([1, 2, 3], name='name')
for index in [ser.index, ser.index.copy(), list(ser.index), ser.index.rename('idx')]:
    result = Series(ser, index=index)
    assert np.shares_memory(ser.values, result.values)
    with tm.assert_cow_warning(warn_copy_on_write):
        result.iloc[0] = 0
    if using_copy_on_write:
        assert ser.iloc[0] == 1
    else:
        assert ser.iloc[0] == 0
result = Series(ser, index=[0, 1, 2, 3])
assert not np.shares_memory(ser.values, result.values)
if using_copy_on_write:
    assert not result._mgr.blocks[0].refs.has_reference()
```

## Next Steps


---

*Source: test_constructors.py:66 | Complexity: Intermediate | Last updated: 2026-06-02*