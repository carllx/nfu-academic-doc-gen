# How To: Tick Rdiv

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test tick rdiv

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `hypothesis`
- `numpy`
- `pytest`
- `pandas._libs.tslibs.offsets`
- `pandas.errors`
- `pandas`
- `pandas._testing`
- `pandas._testing._hypothesis`
- `pandas.tests.tseries.offsets.common`
- `pandas.tseries`
- `pandas.tseries.offsets`

**Setup Required:**
```python
# Fixtures: cls
```

## Step-by-Step Guide

### Step 1: Assign off = cls(...)

```python
off = cls(10)
```

**Verification:**
```python
assert td64 * 2.5 / off == 2.5
```

### Step 2: Assign delta = value

```python
delta = off._as_pd_timedelta
```

**Verification:**
```python
assert delta.to_pytimedelta() * 2 / off == 2
```

### Step 3: Assign td64 = delta.to_timedelta64(...)

```python
td64 = delta.to_timedelta64()
```

### Step 4: Assign instance__type = unknown.join(...)

```python
instance__type = '.'.join([cls.__module__, cls.__name__])
```

### Step 5: Assign msg = value

```python
msg = f"unsupported operand type\\(s\\) for \\/: 'int'|'float' and '{instance__type}'"
```

**Verification:**
```python
assert td64 * 2.5 / off == 2.5
```

### Step 6: Assign result = value

```python
result = np.array([2 * td64, td64]) / off
```

### Step 7: Assign expected = np.array(...)

```python
expected = np.array([2.0, 1.0])
```

### Step 8: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 9: 2 / off

```python
2 / off
```

### Step 10: 2.0 / off

```python
2.0 / off
```

**Verification:**
```python
assert delta.to_pytimedelta() * 2 / off == 2
```


## Complete Example

```python
# Setup
# Fixtures: cls

# Workflow
off = cls(10)
delta = off._as_pd_timedelta
td64 = delta.to_timedelta64()
instance__type = '.'.join([cls.__module__, cls.__name__])
msg = f"unsupported operand type\\(s\\) for \\/: 'int'|'float' and '{instance__type}'"
with pytest.raises(TypeError, match=msg):
    2 / off
with pytest.raises(TypeError, match=msg):
    2.0 / off
assert td64 * 2.5 / off == 2.5
if cls is not Nano:
    assert delta.to_pytimedelta() * 2 / off == 2
result = np.array([2 * td64, td64]) / off
expected = np.array([2.0, 1.0])
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_ticks.py:296 | Complexity: Advanced | Last updated: 2026-06-02*