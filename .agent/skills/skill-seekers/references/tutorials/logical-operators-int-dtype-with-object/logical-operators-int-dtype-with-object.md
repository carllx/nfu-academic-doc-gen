# How To: Logical Operators Int Dtype With Object

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test logical operators int dtype with object

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

### Step 1: Assign s_0123 = Series(...)

```python
s_0123 = Series(range(4), dtype='int64')
```

### Step 2: Assign result = value

```python
result = s_0123 & Series([False, np.nan, False, False])
```

### Step 3: Assign expected = Series(...)

```python
expected = Series([False] * 4)
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign s_abNd = Series(...)

```python
s_abNd = Series(['a', 'b', np.nan, 'd'])
```

### Step 6: s_0123 & s_abNd

```python
s_0123 & s_abNd
```


## Complete Example

```python
# Workflow
s_0123 = Series(range(4), dtype='int64')
result = s_0123 & Series([False, np.nan, False, False])
expected = Series([False] * 4)
tm.assert_series_equal(result, expected)
s_abNd = Series(['a', 'b', np.nan, 'd'])
with pytest.raises(TypeError, match="unsupported.* 'int' and 'str'|'rand_' not supported"):
    s_0123 & s_abNd
```

## Next Steps


---

*Source: test_logical_ops.py:153 | Complexity: Intermediate | Last updated: 2026-06-02*