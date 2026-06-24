# How To: Iteration Over Chunksize

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, mock, workflow, integration

## Overview

Workflow: test iteration over chunksize

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `dateutil.tz`
- `numpy`
- `pytest`
- `pandas`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: offset, monkeypatch
```

## Step-by-Step Guide

### Step 1: Assign chunksize = 5

```python
chunksize = 5
```

**Verification:**
```python
assert index[num] == stamp
```

### Step 2: Assign index = date_range(...)

```python
index = date_range('2000-01-01 00:00:00', periods=chunksize - offset, freq='min')
```

**Verification:**
```python
assert num == len(index)
```

### Step 3: Assign num = 0

```python
num = 0
```

**Verification:**
```python
assert num == len(index)
```

### Step 4: Call m.setattr()

```python
m.setattr(datetimes, '_ITER_CHUNKSIZE', chunksize)
```

**Verification:**
```python
assert index[num] == stamp
```


## Complete Example

```python
# Setup
# Fixtures: offset, monkeypatch

# Workflow
chunksize = 5
index = date_range('2000-01-01 00:00:00', periods=chunksize - offset, freq='min')
num = 0
with monkeypatch.context() as m:
    m.setattr(datetimes, '_ITER_CHUNKSIZE', chunksize)
    for stamp in index:
        assert index[num] == stamp
        num += 1
assert num == len(index)
```

## Next Steps


---

*Source: test_iter.py:64 | Complexity: Intermediate | Last updated: 2026-06-02*