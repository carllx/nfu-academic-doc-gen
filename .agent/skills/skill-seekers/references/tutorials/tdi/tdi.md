# How To: Tdi

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: tdi

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: monotonic
```

## Step-by-Step Guide

### Step 1: Assign tdi = timedelta_range(...)

```python
tdi = timedelta_range('1 Day', periods=10)
```

### Step 2: Assign tdi = value

```python
tdi = tdi[::-1]
```

### Step 3: Assign taker = np.arange(...)

```python
taker = np.arange(10, dtype=np.intp)
```

### Step 4: Call np.random.default_rng.shuffle()

```python
np.random.default_rng(2).shuffle(taker)
```

### Step 5: Assign tdi = tdi.take(...)

```python
tdi = tdi.take(taker)
```


## Complete Example

```python
# Setup
# Fixtures: monotonic

# Workflow
tdi = timedelta_range('1 Day', periods=10)
if monotonic == 'decreasing':
    tdi = tdi[::-1]
elif monotonic is None:
    taker = np.arange(10, dtype=np.intp)
    np.random.default_rng(2).shuffle(taker)
    tdi = tdi.take(taker)
return tdi
```

## Next Steps


---

*Source: test_indexing.py:282 | Complexity: Intermediate | Last updated: 2026-06-02*