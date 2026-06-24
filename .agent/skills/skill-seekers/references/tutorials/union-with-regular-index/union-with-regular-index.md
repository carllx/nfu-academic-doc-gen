# How To: Union With Regular Index

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test union with regular index

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.api.types`

**Setup Required:**
```python
# Fixtures: idx, using_infer_string
```

## Step-by-Step Guide

### Step 1: Assign other = Index(...)

```python
other = Index(['A', 'B', 'C'])
```

**Verification:**
```python
assert ('foo', 'one') in result
```

### Step 2: Assign result = other.union(...)

```python
result = other.union(idx)
```

**Verification:**
```python
assert 'B' in result
```

### Step 3: Assign msg = 'The values in the array are unorderable'

```python
msg = 'The values in the array are unorderable'
```

**Verification:**
```python
assert not result.equals(result2)
```

### Step 4: Call idx.union()

```python
idx.union(other)
```

### Step 5: Assign result2 = idx.union(...)

```python
result2 = idx.union(other)
```


## Complete Example

```python
# Setup
# Fixtures: idx, using_infer_string

# Workflow
other = Index(['A', 'B', 'C'])
result = other.union(idx)
assert ('foo', 'one') in result
assert 'B' in result
if using_infer_string:
    with pytest.raises(NotImplementedError, match='Can only union'):
        idx.union(other)
else:
    msg = 'The values in the array are unorderable'
    with tm.assert_produces_warning(RuntimeWarning, match=msg):
        result2 = idx.union(other)
    assert not result.equals(result2)
```

## Next Steps


---

*Source: test_setops.py:266 | Complexity: Intermediate | Last updated: 2026-06-02*