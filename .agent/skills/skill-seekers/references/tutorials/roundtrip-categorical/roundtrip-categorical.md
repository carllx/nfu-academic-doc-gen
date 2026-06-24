# How To: Roundtrip Categorical

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test roundtrip categorical

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
# Fixtures: request, orient, categorical_frame, convert_axes, using_infer_string
```

## Step-by-Step Guide

### Step 1: Assign data = StringIO(...)

```python
data = StringIO(categorical_frame.to_json(orient=orient))
```

**Verification:**
```python
assert_json_roundtrip_equal(result, expected, orient)
```

### Step 2: Assign result = read_json(...)

```python
result = read_json(data, orient=orient, convert_axes=convert_axes)
```

### Step 3: Assign expected = categorical_frame.copy(...)

```python
expected = categorical_frame.copy()
```

### Step 4: Assign expected.index = expected.index.astype(...)

```python
expected.index = expected.index.astype(str if not using_infer_string else 'str')
```

### Step 5: Assign expected.index.name = None

```python
expected.index.name = None
```

### Step 6: Call assert_json_roundtrip_equal()

```python
assert_json_roundtrip_equal(result, expected, orient)
```

### Step 7: Call request.applymarker()

```python
request.applymarker(pytest.mark.xfail(reason=f"Can't have duplicate index values for orient '{orient}')"))
```


## Complete Example

```python
# Setup
# Fixtures: request, orient, categorical_frame, convert_axes, using_infer_string

# Workflow
if orient in ('index', 'columns'):
    request.applymarker(pytest.mark.xfail(reason=f"Can't have duplicate index values for orient '{orient}')"))
data = StringIO(categorical_frame.to_json(orient=orient))
result = read_json(data, orient=orient, convert_axes=convert_axes)
expected = categorical_frame.copy()
expected.index = expected.index.astype(str if not using_infer_string else 'str')
expected.index.name = None
assert_json_roundtrip_equal(result, expected, orient)
```

## Next Steps


---

*Source: test_pandas.py:247 | Complexity: Intermediate | Last updated: 2026-06-02*