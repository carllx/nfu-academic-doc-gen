# How To: Constructor Not String Type Value Dictionary Raises

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test constructor not string type value dictionary raises

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pickle`
- `re`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.string_`
- `pandas.core.arrays.string_arrow`

**Setup Required:**
```python
# Fixtures: chunked
```

## Step-by-Step Guide

### Step 1: Assign pa = pytest.importorskip(...)

```python
pa = pytest.importorskip('pyarrow')
```

### Step 2: Assign arr = pa.array(...)

```python
arr = pa.array([1, 2, 3], pa.dictionary(pa.int32(), pa.int32()))
```

### Step 3: Assign msg = re.escape(...)

```python
msg = re.escape('ArrowStringArray requires a PyArrow (chunked) array of large_string type')
```

### Step 4: Assign arr = pa.chunked_array(...)

```python
arr = pa.chunked_array(arr)
```

### Step 5: Call ArrowStringArray()

```python
ArrowStringArray(arr)
```


## Complete Example

```python
# Setup
# Fixtures: chunked

# Workflow
pa = pytest.importorskip('pyarrow')
arr = pa.array([1, 2, 3], pa.dictionary(pa.int32(), pa.int32()))
if chunked:
    arr = pa.chunked_array(arr)
msg = re.escape('ArrowStringArray requires a PyArrow (chunked) array of large_string type')
with pytest.raises(ValueError, match=msg):
    ArrowStringArray(arr)
```

## Next Steps


---

*Source: test_string_arrow.py:74 | Complexity: Intermediate | Last updated: 2026-06-02*