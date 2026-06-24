# How To: Delete2

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test delete2

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: tz
```

## Step-by-Step Guide

### Step 1: Assign idx = date_range(...)

```python
idx = date_range(start='2000-01-01 09:00', periods=10, freq='h', name='idx', tz=tz)
```

**Verification:**
```python
assert result.name == expected.name
```

### Step 2: Assign expected = date_range(...)

```python
expected = date_range(start='2000-01-01 10:00', periods=9, freq='h', name='idx', tz=tz)
```

**Verification:**
```python
assert result.freqstr == 'h'
```

### Step 3: Assign result = idx.delete(...)

```python
result = idx.delete(0)
```

**Verification:**
```python
assert result.tz == expected.tz
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

**Verification:**
```python
assert result.name == expected.name
```

### Step 5: Assign expected = date_range(...)

```python
expected = date_range(start='2000-01-01 09:00', periods=9, freq='h', name='idx', tz=tz)
```

**Verification:**
```python
assert result.freqstr == 'h'
```

### Step 6: Assign result = idx.delete(...)

```python
result = idx.delete(-1)
```

**Verification:**
```python
assert result.tz == expected.tz
```

### Step 7: Call tm.assert_index_equal()

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
# Fixtures: tz

# Workflow
idx = date_range(start='2000-01-01 09:00', periods=10, freq='h', name='idx', tz=tz)
expected = date_range(start='2000-01-01 10:00', periods=9, freq='h', name='idx', tz=tz)
result = idx.delete(0)
tm.assert_index_equal(result, expected)
assert result.name == expected.name
assert result.freqstr == 'h'
assert result.tz == expected.tz
expected = date_range(start='2000-01-01 09:00', periods=9, freq='h', name='idx', tz=tz)
result = idx.delete(-1)
tm.assert_index_equal(result, expected)
assert result.name == expected.name
assert result.freqstr == 'h'
assert result.tz == expected.tz
```

## Next Steps


---

*Source: test_delete.py:50 | Complexity: Intermediate | Last updated: 2026-06-02*