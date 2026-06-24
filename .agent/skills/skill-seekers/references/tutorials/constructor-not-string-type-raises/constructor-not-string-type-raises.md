# How To: Constructor Not String Type Raises

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test constructor not string type raises

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
# Fixtures: array_lib, chunked
```

## Step-by-Step Guide

### Step 1: Assign pa = pytest.importorskip(...)

```python
pa = pytest.importorskip('pyarrow')
```

### Step 2: Assign array_lib = value

```python
array_lib = pa if array_lib == 'pyarrow' else np
```

### Step 3: Assign arr = array_lib.array(...)

```python
arr = array_lib.array([1, 2, 3])
```

### Step 4: Assign arr = pa.chunked_array(...)

```python
arr = pa.chunked_array(arr)
```

### Step 5: Assign msg = "Unsupported type '<class 'numpy.ndarray'>' for ArrowExtensionArray"

```python
msg = "Unsupported type '<class 'numpy.ndarray'>' for ArrowExtensionArray"
```

### Step 6: Assign msg = re.escape(...)

```python
msg = re.escape('ArrowStringArray requires a PyArrow (chunked) array of large_string type')
```

### Step 7: Call ArrowStringArray()

```python
ArrowStringArray(arr)
```

### Step 8: Call pytest.skip()

```python
pytest.skip('chunked not applicable to numpy array')
```


## Complete Example

```python
# Setup
# Fixtures: array_lib, chunked

# Workflow
pa = pytest.importorskip('pyarrow')
array_lib = pa if array_lib == 'pyarrow' else np
arr = array_lib.array([1, 2, 3])
if chunked:
    if array_lib is np:
        pytest.skip('chunked not applicable to numpy array')
    arr = pa.chunked_array(arr)
if array_lib is np:
    msg = "Unsupported type '<class 'numpy.ndarray'>' for ArrowExtensionArray"
else:
    msg = re.escape('ArrowStringArray requires a PyArrow (chunked) array of large_string type')
with pytest.raises(ValueError, match=msg):
    ArrowStringArray(arr)
```

## Next Steps


---

*Source: test_string_arrow.py:53 | Complexity: Advanced | Last updated: 2026-06-02*