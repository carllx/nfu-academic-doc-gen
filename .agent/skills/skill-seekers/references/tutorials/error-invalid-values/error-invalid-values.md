# How To: Error Invalid Values

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test error invalid values

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `operator`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: data, all_arithmetic_operators
```

## Step-by-Step Guide

### Step 1: Assign op = all_arithmetic_operators

```python
op = all_arithmetic_operators
```

### Step 2: Assign s = pd.Series(...)

```python
s = pd.Series(data)
```

### Step 3: Assign ops = getattr(...)

```python
ops = getattr(s, op)
```

### Step 4: Assign str_ser = pd.Series(...)

```python
str_ser = pd.Series('foo', index=s.index)
```

### Step 5: Call ops()

```python
ops('foo')
```

### Step 6: Call ops()

```python
ops(pd.Timestamp('20180101'))
```

### Step 7: Assign res = ops(...)

```python
res = ops(str_ser)
```

### Step 8: Assign expected = pd.Series(...)

```python
expected = pd.Series(['foo' * x for x in data], index=s.index)
```

### Step 9: Assign expected = expected.fillna(...)

```python
expected = expected.fillna(np.nan)
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, expected)
```

### Step 11: Call ops()

```python
ops(pd.Series(pd.date_range('20180101', periods=len(s))))
```

### Step 12: Call ops()

```python
ops(str_ser)
```


## Complete Example

```python
# Setup
# Fixtures: data, all_arithmetic_operators

# Workflow
op = all_arithmetic_operators
s = pd.Series(data)
ops = getattr(s, op)
with tm.external_error_raised(TypeError):
    ops('foo')
with tm.external_error_raised(TypeError):
    ops(pd.Timestamp('20180101'))
str_ser = pd.Series('foo', index=s.index)
if all_arithmetic_operators in ['__mul__', '__rmul__']:
    res = ops(str_ser)
    expected = pd.Series(['foo' * x for x in data], index=s.index)
    expected = expected.fillna(np.nan)
    tm.assert_series_equal(res, expected)
else:
    with tm.external_error_raised(TypeError):
        ops(str_ser)
with tm.external_error_raised(TypeError):
    ops(pd.Series(pd.date_range('20180101', periods=len(s))))
```

## Next Steps


---

*Source: test_arithmetic.py:175 | Complexity: Advanced | Last updated: 2026-06-02*