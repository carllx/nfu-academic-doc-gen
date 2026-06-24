# How To: Index Make Union

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test index make union

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
# Fixtures: xloc, xlen, yloc, ylen, eloc, elen, test_length
```

## Step-by-Step Guide

### Step 1: Assign xindex = BlockIndex(...)

```python
xindex = BlockIndex(test_length, xloc, xlen)
```

**Verification:**
```python
assert isinstance(bresult, BlockIndex)
```

### Step 2: Assign yindex = BlockIndex(...)

```python
yindex = BlockIndex(test_length, yloc, ylen)
```

**Verification:**
```python
assert isinstance(iresult, IntIndex)
```

### Step 3: Assign bresult = xindex.make_union(...)

```python
bresult = xindex.make_union(yindex)
```

**Verification:**
```python
assert isinstance(bresult, BlockIndex)
```

### Step 4: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(bresult.blocs, np.array(eloc, dtype=np.int32))
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(bresult.blengths, np.array(elen, dtype=np.int32))
```

### Step 6: Assign ixindex = xindex.to_int_index(...)

```python
ixindex = xindex.to_int_index()
```

### Step 7: Assign iyindex = yindex.to_int_index(...)

```python
iyindex = yindex.to_int_index()
```

### Step 8: Assign iresult = ixindex.make_union(...)

```python
iresult = ixindex.make_union(iyindex)
```

**Verification:**
```python
assert isinstance(iresult, IntIndex)
```

### Step 9: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(iresult.indices, bresult.to_int_index().indices)
```


## Complete Example

```python
# Setup
# Fixtures: xloc, xlen, yloc, ylen, eloc, elen, test_length

# Workflow
xindex = BlockIndex(test_length, xloc, xlen)
yindex = BlockIndex(test_length, yloc, ylen)
bresult = xindex.make_union(yindex)
assert isinstance(bresult, BlockIndex)
tm.assert_numpy_array_equal(bresult.blocs, np.array(eloc, dtype=np.int32))
tm.assert_numpy_array_equal(bresult.blengths, np.array(elen, dtype=np.int32))
ixindex = xindex.to_int_index()
iyindex = yindex.to_int_index()
iresult = ixindex.make_union(iyindex)
assert isinstance(iresult, IntIndex)
tm.assert_numpy_array_equal(iresult.indices, bresult.to_int_index().indices)
```

## Next Steps


---

*Source: test_libsparse.py:101 | Complexity: Advanced | Last updated: 2026-06-02*