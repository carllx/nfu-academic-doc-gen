# How To: Frame Non Unique Index

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test frame non unique index

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
# Fixtures: orient
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame([['a', 'b'], ['c', 'd']], index=[1, 1], columns=['x', 'y'])
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
result = read_json(data, orient=orient)
```

### Step 4: Assign expected = df.copy(...)

```python
expected = df.copy()
```

### Step 5: Call assert_json_roundtrip_equal()

```python
assert_json_roundtrip_equal(result, expected, orient)
```


## Complete Example

```python
# Setup
# Fixtures: orient

# Workflow
df = DataFrame([['a', 'b'], ['c', 'd']], index=[1, 1], columns=['x', 'y'])
data = StringIO(df.to_json(orient=orient))
result = read_json(data, orient=orient)
expected = df.copy()
assert_json_roundtrip_equal(result, expected, orient)
```

## Next Steps


---

*Source: test_pandas.py:140 | Complexity: Intermediate | Last updated: 2026-06-02*