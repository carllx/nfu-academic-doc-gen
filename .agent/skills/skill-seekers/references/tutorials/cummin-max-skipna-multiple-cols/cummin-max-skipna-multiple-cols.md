# How To: Cummin Max Skipna Multiple Cols

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test cummin max skipna multiple cols

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: method
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [np.nan, 2.0, 2.0], 'b': [2.0, 2.0, 2.0]})
```

### Step 2: Assign gb = value

```python
gb = df.groupby([1, 1, 1])[['a', 'b']]
```

### Step 3: Assign result = getattr(...)

```python
result = getattr(gb, method)(skipna=False)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': [np.nan, np.nan, np.nan], 'b': [2.0, 2.0, 2.0]})
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: method

# Workflow
df = DataFrame({'a': [np.nan, 2.0, 2.0], 'b': [2.0, 2.0, 2.0]})
gb = df.groupby([1, 1, 1])[['a', 'b']]
result = getattr(gb, method)(skipna=False)
expected = DataFrame({'a': [np.nan, np.nan, np.nan], 'b': [2.0, 2.0, 2.0]})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_cumulative.py:254 | Complexity: Intermediate | Last updated: 2026-06-02*