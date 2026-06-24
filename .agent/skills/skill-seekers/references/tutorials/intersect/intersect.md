# How To: Intersect

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test intersect

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `operator`
- `numpy`
- `pytest`
- `pandas._libs.sparse`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.sparse`

**Setup Required:**
```python
# Fixtures: cases, test_length
```

## Step-by-Step Guide

### Step 1: Assign unknown = cases

```python
xloc, xlen, yloc, ylen, eloc, elen = cases
```

**Verification:**
```python
assert result.equals(expected)
```

### Step 2: Assign xindex = BlockIndex(...)

```python
xindex = BlockIndex(test_length, xloc, xlen)
```

**Verification:**
```python
assert result.equals(expected.to_int_index())
```

### Step 3: Assign yindex = BlockIndex(...)

```python
yindex = BlockIndex(test_length, yloc, ylen)
```

### Step 4: Assign expected = BlockIndex(...)

```python
expected = BlockIndex(test_length, eloc, elen)
```

### Step 5: Assign longer_index = BlockIndex(...)

```python
longer_index = BlockIndex(test_length + 1, yloc, ylen)
```

### Step 6: Assign result = xindex.intersect(...)

```python
result = xindex.intersect(yindex)
```

**Verification:**
```python
assert result.equals(expected)
```

### Step 7: Assign result = xindex.to_int_index.intersect(...)

```python
result = xindex.to_int_index().intersect(yindex.to_int_index())
```

**Verification:**
```python
assert result.equals(expected.to_int_index())
```

### Step 8: Assign msg = 'Indices must reference same underlying length'

```python
msg = 'Indices must reference same underlying length'
```

### Step 9: Call xindex.intersect()

```python
xindex.intersect(longer_index)
```

### Step 10: Call xindex.to_int_index.intersect()

```python
xindex.to_int_index().intersect(longer_index.to_int_index())
```


## Complete Example

```python
# Setup
# Fixtures: cases, test_length

# Workflow
xloc, xlen, yloc, ylen, eloc, elen = cases
xindex = BlockIndex(test_length, xloc, xlen)
yindex = BlockIndex(test_length, yloc, ylen)
expected = BlockIndex(test_length, eloc, elen)
longer_index = BlockIndex(test_length + 1, yloc, ylen)
result = xindex.intersect(yindex)
assert result.equals(expected)
result = xindex.to_int_index().intersect(yindex.to_int_index())
assert result.equals(expected.to_int_index())
msg = 'Indices must reference same underlying length'
with pytest.raises(Exception, match=msg):
    xindex.intersect(longer_index)
with pytest.raises(Exception, match=msg):
    xindex.to_int_index().intersect(longer_index.to_int_index())
```

## Next Steps


---

*Source: test_libsparse.py:180 | Complexity: Advanced | Last updated: 2026-06-02*