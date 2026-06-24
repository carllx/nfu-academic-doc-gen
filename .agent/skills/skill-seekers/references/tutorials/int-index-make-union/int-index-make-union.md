# How To: Int Index Make Union

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test int index make union

## Prerequisites

**Required Modules:**
- `operator`
- `numpy`
- `pytest`
- `pandas._libs.sparse`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.sparse`


## Step-by-Step Guide

### Step 1: Assign a = IntIndex(...)

```python
a = IntIndex(5, np.array([0, 3, 4], dtype=np.int32))
```

**Verification:**
```python
assert res.equals(exp)
```

### Step 2: Assign b = IntIndex(...)

```python
b = IntIndex(5, np.array([0, 2], dtype=np.int32))
```

**Verification:**
```python
assert res.equals(exp)
```

### Step 3: Assign res = a.make_union(...)

```python
res = a.make_union(b)
```

**Verification:**
```python
assert res.equals(exp)
```

### Step 4: Assign exp = IntIndex(...)

```python
exp = IntIndex(5, np.array([0, 2, 3, 4], np.int32))
```

**Verification:**
```python
assert res.equals(exp)
```

### Step 5: Assign a = IntIndex(...)

```python
a = IntIndex(5, np.array([], dtype=np.int32))
```

### Step 6: Assign b = IntIndex(...)

```python
b = IntIndex(5, np.array([0, 2], dtype=np.int32))
```

### Step 7: Assign res = a.make_union(...)

```python
res = a.make_union(b)
```

### Step 8: Assign exp = IntIndex(...)

```python
exp = IntIndex(5, np.array([0, 2], np.int32))
```

**Verification:**
```python
assert res.equals(exp)
```

### Step 9: Assign a = IntIndex(...)

```python
a = IntIndex(5, np.array([], dtype=np.int32))
```

### Step 10: Assign b = IntIndex(...)

```python
b = IntIndex(5, np.array([], dtype=np.int32))
```

### Step 11: Assign res = a.make_union(...)

```python
res = a.make_union(b)
```

### Step 12: Assign exp = IntIndex(...)

```python
exp = IntIndex(5, np.array([], np.int32))
```

**Verification:**
```python
assert res.equals(exp)
```

### Step 13: Assign a = IntIndex(...)

```python
a = IntIndex(5, np.array([0, 1, 2, 3, 4], dtype=np.int32))
```

### Step 14: Assign b = IntIndex(...)

```python
b = IntIndex(5, np.array([0, 1, 2, 3, 4], dtype=np.int32))
```

### Step 15: Assign res = a.make_union(...)

```python
res = a.make_union(b)
```

### Step 16: Assign exp = IntIndex(...)

```python
exp = IntIndex(5, np.array([0, 1, 2, 3, 4], np.int32))
```

**Verification:**
```python
assert res.equals(exp)
```

### Step 17: Assign a = IntIndex(...)

```python
a = IntIndex(5, np.array([0, 1], dtype=np.int32))
```

### Step 18: Assign b = IntIndex(...)

```python
b = IntIndex(4, np.array([0, 1], dtype=np.int32))
```

### Step 19: Assign msg = 'Indices must reference same underlying length'

```python
msg = 'Indices must reference same underlying length'
```

### Step 20: Call a.make_union()

```python
a.make_union(b)
```


## Complete Example

```python
# Workflow
a = IntIndex(5, np.array([0, 3, 4], dtype=np.int32))
b = IntIndex(5, np.array([0, 2], dtype=np.int32))
res = a.make_union(b)
exp = IntIndex(5, np.array([0, 2, 3, 4], np.int32))
assert res.equals(exp)
a = IntIndex(5, np.array([], dtype=np.int32))
b = IntIndex(5, np.array([0, 2], dtype=np.int32))
res = a.make_union(b)
exp = IntIndex(5, np.array([0, 2], np.int32))
assert res.equals(exp)
a = IntIndex(5, np.array([], dtype=np.int32))
b = IntIndex(5, np.array([], dtype=np.int32))
res = a.make_union(b)
exp = IntIndex(5, np.array([], np.int32))
assert res.equals(exp)
a = IntIndex(5, np.array([0, 1, 2, 3, 4], dtype=np.int32))
b = IntIndex(5, np.array([0, 1, 2, 3, 4], dtype=np.int32))
res = a.make_union(b)
exp = IntIndex(5, np.array([0, 1, 2, 3, 4], np.int32))
assert res.equals(exp)
a = IntIndex(5, np.array([0, 1], dtype=np.int32))
b = IntIndex(4, np.array([0, 1], dtype=np.int32))
msg = 'Indices must reference same underlying length'
with pytest.raises(ValueError, match=msg):
    a.make_union(b)
```

## Next Steps


---

*Source: test_libsparse.py:145 | Complexity: Advanced | Last updated: 2026-06-02*