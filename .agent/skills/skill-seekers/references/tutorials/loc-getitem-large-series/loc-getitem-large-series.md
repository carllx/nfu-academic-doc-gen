# How To: Loc Getitem Large Series

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: mock, workflow, integration

## Overview

Workflow: test loc getitem large series

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: monkeypatch
```

## Step-by-Step Guide

### Step 1: Assign size_cutoff = 20

```python
size_cutoff = 20
```

### Step 2: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result1, result2)
```

### Step 3: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result1, result3)
```

### Step 4: Call monkeypatch.setattr()

```python
monkeypatch.setattr(libindex, '_SIZE_CUTOFF', size_cutoff)
```

### Step 5: Assign ser = Series(...)

```python
ser = Series(np.arange(size_cutoff), index=IntervalIndex.from_breaks(np.arange(size_cutoff + 1)))
```

### Step 6: Assign result1 = value

```python
result1 = ser.loc[:8]
```

### Step 7: Assign result2 = value

```python
result2 = ser.loc[0:8]
```

### Step 8: Assign result3 = value

```python
result3 = ser.loc[0:8:1]
```


## Complete Example

```python
# Setup
# Fixtures: monkeypatch

# Workflow
size_cutoff = 20
with monkeypatch.context():
    monkeypatch.setattr(libindex, '_SIZE_CUTOFF', size_cutoff)
    ser = Series(np.arange(size_cutoff), index=IntervalIndex.from_breaks(np.arange(size_cutoff + 1)))
    result1 = ser.loc[:8]
    result2 = ser.loc[0:8]
    result3 = ser.loc[0:8:1]
tm.assert_series_equal(result1, result2)
tm.assert_series_equal(result1, result3)
```

## Next Steps


---

*Source: test_interval.py:75 | Complexity: Advanced | Last updated: 2026-06-02*