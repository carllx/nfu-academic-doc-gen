# How To: Roundtrip Str Axes

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test roundtrip str axes

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
# Fixtures: orient, convert_axes, dtype
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(np.zeros((200, 4)), columns=[str(i) for i in range(4)], index=[str(i) for i in range(200)], dtype=dtype)
```

**Verification:**
```python
assert_json_roundtrip_equal(result, expected, orient)
```

### Step 2: Assign data = StringIO(...)

```python
data = StringIO(df.to_json(orient=orient))
```

### Step 3: Assign result = read_json(...)

```python
result = read_json(data, orient=orient, convert_axes=convert_axes, dtype=dtype)
```

### Step 4: Assign expected = df.copy(...)

```python
expected = df.copy()
```

### Step 5: Call assert_json_roundtrip_equal()

```python
assert_json_roundtrip_equal(result, expected, orient)
```

### Step 6: Assign expected = expected.astype(...)

```python
expected = expected.astype(np.int64)
```

### Step 7: Assign expected.columns = expected.columns.astype(...)

```python
expected.columns = expected.columns.astype(np.int64)
```

### Step 8: Assign expected.index = expected.index.astype(...)

```python
expected.index = expected.index.astype(np.int64)
```

### Step 9: Assign expected.columns = expected.columns.astype(...)

```python
expected.columns = expected.columns.astype(np.int64)
```

### Step 10: Assign expected.columns = expected.columns.astype(...)

```python
expected.columns = expected.columns.astype(np.int64)
```


## Complete Example

```python
# Setup
# Fixtures: orient, convert_axes, dtype

# Workflow
df = DataFrame(np.zeros((200, 4)), columns=[str(i) for i in range(4)], index=[str(i) for i in range(200)], dtype=dtype)
data = StringIO(df.to_json(orient=orient))
result = read_json(data, orient=orient, convert_axes=convert_axes, dtype=dtype)
expected = df.copy()
if not dtype:
    expected = expected.astype(np.int64)
if convert_axes and orient in ('index', 'columns'):
    expected.columns = expected.columns.astype(np.int64)
    expected.index = expected.index.astype(np.int64)
elif orient == 'records' and convert_axes:
    expected.columns = expected.columns.astype(np.int64)
elif convert_axes and orient == 'split':
    expected.columns = expected.columns.astype(np.int64)
assert_json_roundtrip_equal(result, expected, orient)
```

## Next Steps


---

*Source: test_pandas.py:216 | Complexity: Advanced | Last updated: 2026-06-02*