# How To: Roundtrip Mixed

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test roundtrip mixed

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

### Step 1: Assign index = Index(...)

```python
index = Index(['a', 'b', 'c', 'd', 'e'])
```

**Verification:**
```python
assert_json_roundtrip_equal(result, expected, orient)
```

### Step 2: Assign values = value

```python
values = {'A': [0.0, 1.0, 2.0, 3.0, 4.0], 'B': [0.0, 1.0, 0.0, 1.0, 0.0], 'C': ['foo1', 'foo2', 'foo3', 'foo4', 'foo5'], 'D': [True, False, True, False, True]}
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame(data=values, index=index)
```

### Step 4: Assign data = StringIO(...)

```python
data = StringIO(df.to_json(orient=orient))
```

### Step 5: Assign result = read_json(...)

```python
result = read_json(data, orient=orient, convert_axes=convert_axes)
```

### Step 6: Assign expected = df.copy(...)

```python
expected = df.copy()
```

### Step 7: Assign expected = expected.assign(...)

```python
expected = expected.assign(**expected.select_dtypes('number').astype(np.int64))
```

### Step 8: Call assert_json_roundtrip_equal()

```python
assert_json_roundtrip_equal(result, expected, orient)
```


## Complete Example

```python
# Setup
# Fixtures: orient, convert_axes

# Workflow
index = Index(['a', 'b', 'c', 'd', 'e'])
values = {'A': [0.0, 1.0, 2.0, 3.0, 4.0], 'B': [0.0, 1.0, 0.0, 1.0, 0.0], 'C': ['foo1', 'foo2', 'foo3', 'foo4', 'foo5'], 'D': [True, False, True, False, True]}
df = DataFrame(data=values, index=index)
data = StringIO(df.to_json(orient=orient))
result = read_json(data, orient=orient, convert_axes=convert_axes)
expected = df.copy()
expected = expected.assign(**expected.select_dtypes('number').astype(np.int64))
assert_json_roundtrip_equal(result, expected, orient)
```

## Next Steps


---

*Source: test_pandas.py:301 | Complexity: Advanced | Last updated: 2026-06-02*