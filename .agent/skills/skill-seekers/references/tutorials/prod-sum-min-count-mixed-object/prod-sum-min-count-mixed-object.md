# How To: Prod Sum Min Count Mixed Object

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test prod sum min count mixed object

## Prerequisites

**Required Modules:**
- `datetime`
- `decimal`
- `re`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.compat.numpy`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame([1, 'a', True])
```

### Step 2: Assign result = df.prod(...)

```python
result = df.prod(axis=0, min_count=1, numeric_only=False)
```

### Step 3: Assign expected = Series(...)

```python
expected = Series(['a'], dtype=object)
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign msg = re.escape(...)

```python
msg = re.escape("unsupported operand type(s) for +: 'int' and 'str'")
```

### Step 6: Call df.sum()

```python
df.sum(axis=0, min_count=1, numeric_only=False)
```


## Complete Example

```python
# Workflow
df = DataFrame([1, 'a', True])
result = df.prod(axis=0, min_count=1, numeric_only=False)
expected = Series(['a'], dtype=object)
tm.assert_series_equal(result, expected)
msg = re.escape("unsupported operand type(s) for +: 'int' and 'str'")
with pytest.raises(TypeError, match=msg):
    df.sum(axis=0, min_count=1, numeric_only=False)
```

## Next Steps


---

*Source: test_reductions.py:1975 | Complexity: Intermediate | Last updated: 2026-06-02*