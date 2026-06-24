# How To: Pickling

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test pickling

## Prerequisites

**Required Modules:**
- `pickle`
- `numpy`
- `numpy.ma`
- `numpy._core.records`
- `numpy.ma`
- `numpy.ma.mrecords`
- `numpy.ma.testutils`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign base = self.base.copy(...)

```python
base = self.base.copy()
```

**Verification:**
```python
assert_equal(mrec_.dtype, mrec.dtype)
```

### Step 2: Assign mrec = base.view(...)

```python
mrec = base.view(mrecarray)
```

**Verification:**
```python
assert_equal_records(mrec_._data, mrec._data)
```

### Step 3: Assign _ = pickle.dumps(...)

```python
_ = pickle.dumps(mrec, protocol=proto)
```

**Verification:**
```python
assert_equal(mrec_._mask, mrec._mask)
```

### Step 4: Assign mrec_ = pickle.loads(...)

```python
mrec_ = pickle.loads(_)
```

**Verification:**
```python
assert_equal_records(mrec_._mask, mrec._mask)
```

### Step 5: Call assert_equal()

```python
assert_equal(mrec_.dtype, mrec.dtype)
```

### Step 6: Call assert_equal_records()

```python
assert_equal_records(mrec_._data, mrec._data)
```

### Step 7: Call assert_equal()

```python
assert_equal(mrec_._mask, mrec._mask)
```

### Step 8: Call assert_equal_records()

```python
assert_equal_records(mrec_._mask, mrec._mask)
```


## Complete Example

```python
# Workflow
base = self.base.copy()
mrec = base.view(mrecarray)
for proto in range(2, pickle.HIGHEST_PROTOCOL + 1):
    _ = pickle.dumps(mrec, protocol=proto)
    mrec_ = pickle.loads(_)
    assert_equal(mrec_.dtype, mrec.dtype)
    assert_equal_records(mrec_._data, mrec._data)
    assert_equal(mrec_._mask, mrec._mask)
    assert_equal_records(mrec_._mask, mrec._mask)
```

## Next Steps


---

*Source: test_mrecords.py:285 | Complexity: Advanced | Last updated: 2026-06-02*