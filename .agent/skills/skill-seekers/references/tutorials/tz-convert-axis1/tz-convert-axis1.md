# How To: Tz Convert Axis1

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test tz convert axis1

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign rng = date_range(...)

```python
rng = date_range('1/1/2011', periods=200, freq='D', tz='US/Eastern')
```

**Verification:**
```python
assert result.columns.tz.zone == 'Europe/Berlin'
```

### Step 2: Assign obj = DataFrame(...)

```python
obj = DataFrame({'a': 1}, index=rng)
```

### Step 3: Assign obj = value

```python
obj = obj.T
```

### Step 4: Assign result = obj.tz_convert(...)

```python
result = obj.tz_convert('Europe/Berlin', axis=1)
```

**Verification:**
```python
assert result.columns.tz.zone == 'Europe/Berlin'
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': 1}, rng.tz_convert('Europe/Berlin'))
```

### Step 6: Call tm.assert_equal()

```python
tm.assert_equal(result, expected.T)
```


## Complete Example

```python
# Workflow
rng = date_range('1/1/2011', periods=200, freq='D', tz='US/Eastern')
obj = DataFrame({'a': 1}, index=rng)
obj = obj.T
result = obj.tz_convert('Europe/Berlin', axis=1)
assert result.columns.tz.zone == 'Europe/Berlin'
expected = DataFrame({'a': 1}, rng.tz_convert('Europe/Berlin'))
tm.assert_equal(result, expected.T)
```

## Next Steps


---

*Source: test_tz_convert.py:28 | Complexity: Intermediate | Last updated: 2026-06-02*