# How To: Delete Slice2

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test delete slice2

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: tz, unit
```

## Step-by-Step Guide

### Step 1: Assign dti = date_range(...)

```python
dti = date_range('2000-01-01 09:00', periods=10, freq='h', name='idx', tz=tz, unit=unit)
```

**Verification:**
```python
assert result.name == expected.name
```

### Step 2: Assign ts = Series(...)

```python
ts = Series(1, index=dti)
```

**Verification:**
```python
assert result.freq == expected.freq
```

### Step 3: Assign result = value

```python
result = ts.drop(ts.index[:5]).index
```

**Verification:**
```python
assert result.tz == expected.tz
```

### Step 4: Assign expected = value

```python
expected = dti[5:]
```

**Verification:**
```python
assert result.name == expected.name
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

**Verification:**
```python
assert result.freq == expected.freq
```

### Step 6: Assign result = value

```python
result = ts.drop(ts.index[[1, 3, 5, 7, 9]]).index
```

**Verification:**
```python
assert result.tz == expected.tz
```

### Step 7: Assign expected = unknown._with_freq(...)

```python
expected = dti[::2]._with_freq(None)
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

**Verification:**
```python
assert result.name == expected.name
```


## Complete Example

```python
# Setup
# Fixtures: tz, unit

# Workflow
dti = date_range('2000-01-01 09:00', periods=10, freq='h', name='idx', tz=tz, unit=unit)
ts = Series(1, index=dti)
result = ts.drop(ts.index[:5]).index
expected = dti[5:]
tm.assert_index_equal(result, expected)
assert result.name == expected.name
assert result.freq == expected.freq
assert result.tz == expected.tz
result = ts.drop(ts.index[[1, 3, 5, 7, 9]]).index
expected = dti[::2]._with_freq(None)
tm.assert_index_equal(result, expected)
assert result.name == expected.name
assert result.freq == expected.freq
assert result.tz == expected.tz
```

## Next Steps


---

*Source: test_delete.py:119 | Complexity: Advanced | Last updated: 2026-06-02*