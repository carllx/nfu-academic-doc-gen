# How To: Numeric Dtype

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test numeric dtype

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `collections`
- `io`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: all_parsers, dtype
```

## Step-by-Step Guide

### Step 1: Assign data = '0\n1'

```python
data = '0\n1'
```

### Step 2: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame([0, 1], dtype=dtype)
```

### Step 4: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), header=None, dtype=dtype)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(expected, result)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers, dtype

# Workflow
data = '0\n1'
parser = all_parsers
expected = DataFrame([0, 1], dtype=dtype)
result = parser.read_csv(StringIO(data), header=None, dtype=dtype)
tm.assert_frame_equal(expected, result)
```

## Next Steps


---

*Source: test_dtypes_basic.py:137 | Complexity: Intermediate | Last updated: 2026-06-02*