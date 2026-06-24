# How To: Roundtrip Empty

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test roundtrip empty

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
# Fixtures: orient, convert_axes
```

## Step-by-Step Guide

### Step 1: Assign empty_frame = DataFrame(...)

```python
empty_frame = DataFrame()
```

### Step 2: Assign data = StringIO(...)

```python
data = StringIO(empty_frame.to_json(orient=orient))
```

### Step 3: Assign result = read_json(...)

```python
result = read_json(data, orient=orient, convert_axes=convert_axes)
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign idx = Index(...)

```python
idx = Index([], dtype=float if convert_axes else object)
```

### Step 6: Assign expected = DataFrame(...)

```python
expected = DataFrame(index=idx, columns=idx)
```

### Step 7: Assign expected = DataFrame(...)

```python
expected = DataFrame()
```

### Step 8: Assign expected = empty_frame.copy(...)

```python
expected = empty_frame.copy()
```


## Complete Example

```python
# Setup
# Fixtures: orient, convert_axes

# Workflow
empty_frame = DataFrame()
data = StringIO(empty_frame.to_json(orient=orient))
result = read_json(data, orient=orient, convert_axes=convert_axes)
if orient == 'split':
    idx = Index([], dtype=float if convert_axes else object)
    expected = DataFrame(index=idx, columns=idx)
elif orient in ['index', 'columns']:
    expected = DataFrame()
else:
    expected = empty_frame.copy()
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_pandas.py:269 | Complexity: Advanced | Last updated: 2026-06-02*