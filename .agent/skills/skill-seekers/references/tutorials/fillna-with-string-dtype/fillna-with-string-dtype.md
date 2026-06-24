# How To: Fillna With String Dtype

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test fillna with string dtype

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: method, expected
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': pd.array([None, 'a', None], dtype='string'), 'b': [0, 0, 0]})
```

### Step 2: Assign grp = df.groupby(...)

```python
grp = df.groupby('b')
```

### Step 3: Assign msg = 'DataFrameGroupBy.fillna is deprecated'

```python
msg = 'DataFrameGroupBy.fillna is deprecated'
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': pd.array(expected, dtype='string')})
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign result = grp.fillna(...)

```python
result = grp.fillna(method=method)
```


## Complete Example

```python
# Setup
# Fixtures: method, expected

# Workflow
df = DataFrame({'a': pd.array([None, 'a', None], dtype='string'), 'b': [0, 0, 0]})
grp = df.groupby('b')
msg = 'DataFrameGroupBy.fillna is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = grp.fillna(method=method)
expected = DataFrame({'a': pd.array(expected, dtype='string')})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_missing.py:51 | Complexity: Intermediate | Last updated: 2026-06-02*