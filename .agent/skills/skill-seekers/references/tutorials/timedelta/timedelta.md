# How To: Timedelta

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test timedelta

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.tests.arithmetic.common`

**Setup Required:**
```python
# Fixtures: freq
```

## Step-by-Step Guide

### Step 1: Assign index = pd.date_range(...)

```python
index = pd.date_range('1/1/2000', periods=50, freq=freq)
```

**Verification:**
```python
assert index.freq == expected
```

### Step 2: Assign shifted = value

```python
shifted = index + timedelta(1)
```

**Verification:**
```python
assert shifted.freq == expected
```

### Step 3: Assign back = value

```python
back = shifted + timedelta(-1)
```

**Verification:**
```python
assert back.freq == expected
```

### Step 4: Assign back = back._with_freq(...)

```python
back = back._with_freq('infer')
```

**Verification:**
```python
assert index.freq == pd.tseries.offsets.BusinessDay(1)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(index, back)
```

**Verification:**
```python
assert shifted.freq is None
```

### Step 6: Assign result = value

```python
result = index - timedelta(1)
```

**Verification:**
```python
assert back.freq == pd.tseries.offsets.BusinessDay(1)
```

### Step 7: Assign expected = value

```python
expected = index + timedelta(-1)
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 9: Assign expected = pd.tseries.offsets.Day(...)

```python
expected = pd.tseries.offsets.Day(1)
```

**Verification:**
```python
assert index.freq == expected
```


## Complete Example

```python
# Setup
# Fixtures: freq

# Workflow
index = pd.date_range('1/1/2000', periods=50, freq=freq)
shifted = index + timedelta(1)
back = shifted + timedelta(-1)
back = back._with_freq('infer')
tm.assert_index_equal(index, back)
if freq == 'D':
    expected = pd.tseries.offsets.Day(1)
    assert index.freq == expected
    assert shifted.freq == expected
    assert back.freq == expected
else:
    assert index.freq == pd.tseries.offsets.BusinessDay(1)
    assert shifted.freq is None
    assert back.freq == pd.tseries.offsets.BusinessDay(1)
result = index - timedelta(1)
expected = index + timedelta(-1)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_timedelta64.py:522 | Complexity: Advanced | Last updated: 2026-06-02*