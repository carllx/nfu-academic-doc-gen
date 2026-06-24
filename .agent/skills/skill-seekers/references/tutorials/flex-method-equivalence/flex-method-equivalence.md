# How To: Flex Method Equivalence

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test flex method equivalence

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `decimal`
- `operator`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas._libs.tslibs`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`
- `pandas.core.computation`
- `pandas.core.computation.check`

**Setup Required:**
```python
# Fixtures: opname, ts
```

## Step-by-Step Guide

### Step 1: Assign tser = Series(...)

```python
tser = Series(np.arange(20, dtype=np.float64), index=date_range('2020-01-01', periods=20), name='ts')
```

### Step 2: Assign series = unknown(...)

```python
series = ts[0](tser)
```

### Step 3: Assign other = unknown(...)

```python
other = ts[1](tser)
```

### Step 4: Assign check_reverse = value

```python
check_reverse = ts[2]
```

### Step 5: Assign op = getattr(...)

```python
op = getattr(Series, opname)
```

### Step 6: Assign alt = getattr(...)

```python
alt = getattr(operator, opname)
```

### Step 7: Assign result = op(...)

```python
result = op(series, other)
```

### Step 8: Assign expected = alt(...)

```python
expected = alt(series, other)
```

### Step 9: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(result, expected)
```

### Step 10: Assign rop = getattr(...)

```python
rop = getattr(Series, 'r' + opname)
```

### Step 11: Assign result = rop(...)

```python
result = rop(series, other)
```

### Step 12: Assign expected = alt(...)

```python
expected = alt(other, series)
```

### Step 13: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: opname, ts

# Workflow
tser = Series(np.arange(20, dtype=np.float64), index=date_range('2020-01-01', periods=20), name='ts')
series = ts[0](tser)
other = ts[1](tser)
check_reverse = ts[2]
op = getattr(Series, opname)
alt = getattr(operator, opname)
result = op(series, other)
expected = alt(series, other)
tm.assert_almost_equal(result, expected)
if check_reverse:
    rop = getattr(Series, 'r' + opname)
    result = rop(series, other)
    expected = alt(other, series)
    tm.assert_almost_equal(result, expected)
```

## Next Steps


---

*Source: test_arithmetic.py:60 | Complexity: Advanced | Last updated: 2026-06-02*