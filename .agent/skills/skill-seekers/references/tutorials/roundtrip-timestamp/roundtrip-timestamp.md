# How To: Roundtrip Timestamp

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test roundtrip timestamp

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `datetime`
- `decimal`
- `io`
- `json`
- `os`
- `sys`
- `time`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.compat`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.io.json`
- `pandas.arrays`
- `pandas.arrays`

**Setup Required:**
```python
# Fixtures: orient, convert_axes, datetime_frame
```

## Step-by-Step Guide

### Step 1: Assign data = StringIO(...)

```python
data = StringIO(datetime_frame.to_json(orient=orient))
```

**Verification:**
```python
assert_json_roundtrip_equal(result, expected, orient)
```

### Step 2: Assign result = read_json(...)

```python
result = read_json(data, orient=orient, convert_axes=convert_axes)
```

### Step 3: Assign expected = datetime_frame.copy(...)

```python
expected = datetime_frame.copy()
```

### Step 4: Call assert_json_roundtrip_equal()

```python
assert_json_roundtrip_equal(result, expected, orient)
```

### Step 5: Assign idx = value

```python
idx = expected.index.view(np.int64) // 1000000
```

### Step 6: Assign expected.index = idx

```python
expected.index = idx
```

### Step 7: Assign idx = idx.astype(...)

```python
idx = idx.astype(str)
```


## Complete Example

```python
# Setup
# Fixtures: orient, convert_axes, datetime_frame

# Workflow
data = StringIO(datetime_frame.to_json(orient=orient))
result = read_json(data, orient=orient, convert_axes=convert_axes)
expected = datetime_frame.copy()
if not convert_axes:
    idx = expected.index.view(np.int64) // 1000000
    if orient != 'split':
        idx = idx.astype(str)
    expected.index = idx
assert_json_roundtrip_equal(result, expected, orient)
```

## Next Steps


---

*Source: test_pandas.py:284 | Complexity: Intermediate | Last updated: 2026-06-02*