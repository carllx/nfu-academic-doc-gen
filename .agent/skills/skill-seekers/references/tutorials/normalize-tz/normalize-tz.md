# How To: Normalize Tz

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test normalize tz

## Prerequisites

**Required Modules:**
- `dateutil.tz`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign rng = date_range(...)

```python
rng = date_range('1/1/2000 9:30', periods=10, freq='D', tz='US/Eastern')
```

**Verification:**
```python
assert result.is_normalized
```

### Step 2: Assign result = rng.normalize(...)

```python
result = rng.normalize()
```

**Verification:**
```python
assert not rng.is_normalized
```

### Step 3: Assign expected = date_range(...)

```python
expected = date_range('1/1/2000', periods=10, freq='D', tz='US/Eastern')
```

**Verification:**
```python
assert result.is_normalized
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected._with_freq(None))
```

**Verification:**
```python
assert not rng.is_normalized
```

### Step 5: Assign rng = date_range(...)

```python
rng = date_range('1/1/2000 9:30', periods=10, freq='D', tz='UTC')
```

**Verification:**
```python
assert result.is_normalized
```

### Step 6: Assign result = rng.normalize(...)

```python
result = rng.normalize()
```

**Verification:**
```python
assert not rng.is_normalized
```

### Step 7: Assign expected = date_range(...)

```python
expected = date_range('1/1/2000', periods=10, freq='D', tz='UTC')
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

**Verification:**
```python
assert result.is_normalized
```

### Step 9: Assign rng = date_range(...)

```python
rng = date_range('1/1/2000 9:30', periods=10, freq='D', tz=tzlocal())
```

### Step 10: Assign result = rng.normalize(...)

```python
result = rng.normalize()
```

### Step 11: Assign expected = date_range(...)

```python
expected = date_range('1/1/2000', periods=10, freq='D', tz=tzlocal())
```

### Step 12: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected._with_freq(None))
```

**Verification:**
```python
assert result.is_normalized
```


## Complete Example

```python
# Workflow
rng = date_range('1/1/2000 9:30', periods=10, freq='D', tz='US/Eastern')
result = rng.normalize()
expected = date_range('1/1/2000', periods=10, freq='D', tz='US/Eastern')
tm.assert_index_equal(result, expected._with_freq(None))
assert result.is_normalized
assert not rng.is_normalized
rng = date_range('1/1/2000 9:30', periods=10, freq='D', tz='UTC')
result = rng.normalize()
expected = date_range('1/1/2000', periods=10, freq='D', tz='UTC')
tm.assert_index_equal(result, expected)
assert result.is_normalized
assert not rng.is_normalized
rng = date_range('1/1/2000 9:30', periods=10, freq='D', tz=tzlocal())
result = rng.normalize()
expected = date_range('1/1/2000', periods=10, freq='D', tz=tzlocal())
tm.assert_index_equal(result, expected._with_freq(None))
assert result.is_normalized
assert not rng.is_normalized
```

## Next Steps


---

*Source: test_normalize.py:45 | Complexity: Advanced | Last updated: 2026-06-02*