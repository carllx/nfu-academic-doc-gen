# How To: Scalar Na Logical Ops Corners

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test scalar na logical ops corners

## Prerequisites

**Required Modules:**
- `datetime`
- `operator`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas`
- `pandas._testing`
- `pandas.core`


## Step-by-Step Guide

### Step 1: Assign s = Series(...)

```python
s = Series([2, 3, 4, 5, 6, 7, 8, 9, 10])
```

### Step 2: Assign msg = 'Cannot perform.+with a dtyped.+array and scalar of type'

```python
msg = 'Cannot perform.+with a dtyped.+array and scalar of type'
```

### Step 3: Assign s = Series(...)

```python
s = Series([2, 3, 4, 5, 6, 7, 8, 9, datetime(2005, 1, 1)])
```

### Step 4: Assign unknown = value

```python
s[::2] = np.nan
```

### Step 5: Assign expected = Series(...)

```python
expected = Series(True, index=s.index)
```

### Step 6: Assign unknown = False

```python
expected[::2] = False
```

### Step 7: Assign msg = 'Logical ops \\(and, or, xor\\) between Pandas objects and dtype-less sequences'

```python
msg = 'Logical ops \\(and, or, xor\\) between Pandas objects and dtype-less sequences'
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 9: s & datetime(2005, 1, 1)

```python
s & datetime(2005, 1, 1)
```

### Step 10: Assign result = value

```python
result = s & list(s)
```


## Complete Example

```python
# Workflow
s = Series([2, 3, 4, 5, 6, 7, 8, 9, 10])
msg = 'Cannot perform.+with a dtyped.+array and scalar of type'
with pytest.raises(TypeError, match=msg):
    s & datetime(2005, 1, 1)
s = Series([2, 3, 4, 5, 6, 7, 8, 9, datetime(2005, 1, 1)])
s[::2] = np.nan
expected = Series(True, index=s.index)
expected[::2] = False
msg = 'Logical ops \\(and, or, xor\\) between Pandas objects and dtype-less sequences'
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = s & list(s)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_logical_ops.py:260 | Complexity: Advanced | Last updated: 2026-06-02*