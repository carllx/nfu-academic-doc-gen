# How To: Nat Arithmetic Index

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test nat arithmetic index

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `operator`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs`
- `pandas.compat.numpy`
- `pandas`
- `pandas._testing`
- `pandas.core`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: op_name, value
```

## Step-by-Step Guide

### Step 1: Assign exp_name = 'x'

```python
exp_name = 'x'
```

### Step 2: Assign exp_data = value

```python
exp_data = [NaT] * 2
```

### Step 3: Assign expected = expected.as_unit(...)

```python
expected = expected.as_unit(value.unit)
```

### Step 4: Assign op = value

```python
op = _ops[op_name]
```

### Step 5: Assign result = op(...)

```python
result = op(NaT, value)
```

### Step 6: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```

### Step 7: Assign expected = DatetimeIndex(...)

```python
expected = DatetimeIndex(exp_data, tz=value.tz, name=exp_name)
```

### Step 8: Assign expected = TimedeltaIndex(...)

```python
expected = TimedeltaIndex(exp_data, name=exp_name)
```

### Step 9: Assign expected = value

```python
expected = expected.array
```


## Complete Example

```python
# Setup
# Fixtures: op_name, value

# Workflow
exp_name = 'x'
exp_data = [NaT] * 2
if value.dtype.kind == 'M' and 'plus' in op_name:
    expected = DatetimeIndex(exp_data, tz=value.tz, name=exp_name)
else:
    expected = TimedeltaIndex(exp_data, name=exp_name)
expected = expected.as_unit(value.unit)
if not isinstance(value, Index):
    expected = expected.array
op = _ops[op_name]
result = op(NaT, value)
tm.assert_equal(result, expected)
```

## Next Steps


---

*Source: test_nat.py:452 | Complexity: Advanced | Last updated: 2026-06-02*