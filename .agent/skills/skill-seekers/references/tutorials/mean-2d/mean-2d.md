# How To: Mean 2D

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test mean 2d

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign tdi = pd.timedelta_range(...)

```python
tdi = pd.timedelta_range('14 days', periods=6)
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign tda = tdi._data.reshape(...)

```python
tda = tdi._data.reshape(3, 2)
```

### Step 3: Assign result = tda.mean(...)

```python
result = tda.mean(axis=0)
```

### Step 4: Assign expected = value

```python
expected = tda[1]
```

### Step 5: Call tm.assert_timedelta_array_equal()

```python
tm.assert_timedelta_array_equal(result, expected)
```

### Step 6: Assign result = tda.mean(...)

```python
result = tda.mean(axis=1)
```

### Step 7: Assign expected = value

```python
expected = tda[:, 0] + Timedelta(hours=12)
```

### Step 8: Call tm.assert_timedelta_array_equal()

```python
tm.assert_timedelta_array_equal(result, expected)
```

### Step 9: Assign result = tda.mean(...)

```python
result = tda.mean(axis=None)
```

### Step 10: Assign expected = tdi.mean(...)

```python
expected = tdi.mean()
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Workflow
tdi = pd.timedelta_range('14 days', periods=6)
tda = tdi._data.reshape(3, 2)
result = tda.mean(axis=0)
expected = tda[1]
tm.assert_timedelta_array_equal(result, expected)
result = tda.mean(axis=1)
expected = tda[:, 0] + Timedelta(hours=12)
tm.assert_timedelta_array_equal(result, expected)
result = tda.mean(axis=None)
expected = tdi.mean()
assert result == expected
```

## Next Steps


---

*Source: test_reductions.py:204 | Complexity: Advanced | Last updated: 2026-06-02*