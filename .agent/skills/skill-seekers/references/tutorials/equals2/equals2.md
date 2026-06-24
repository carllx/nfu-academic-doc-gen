# How To: Equals2

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test equals2

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = TimedeltaIndex(...)

```python
idx = TimedeltaIndex(['1 days', '2 days', 'NaT'])
```

**Verification:**
```python
assert idx.equals(idx)
```

### Step 2: Assign idx2 = TimedeltaIndex(...)

```python
idx2 = TimedeltaIndex(['2 days', '1 days', 'NaT'])
```

**Verification:**
```python
assert idx.equals(idx.copy())
```

### Step 3: Assign oob = Index(...)

```python
oob = Index([timedelta(days=10 ** 6)] * 3, dtype=object)
```

**Verification:**
```python
assert idx.equals(idx.astype(object))
```

### Step 4: Assign oob2 = Index(...)

```python
oob2 = Index([np.timedelta64(x) for x in oob], dtype=object)
```

**Verification:**
```python
assert idx.astype(object).equals(idx)
```

### Step 5: Assign oob3 = oob.map(...)

```python
oob3 = oob.map(np.timedelta64)
```

**Verification:**
```python
assert idx.astype(object).equals(idx.astype(object))
```


## Complete Example

```python
# Workflow
idx = TimedeltaIndex(['1 days', '2 days', 'NaT'])
assert idx.equals(idx)
assert idx.equals(idx.copy())
assert idx.equals(idx.astype(object))
assert idx.astype(object).equals(idx)
assert idx.astype(object).equals(idx.astype(object))
assert not idx.equals(list(idx))
assert not idx.equals(pd.Series(idx))
idx2 = TimedeltaIndex(['2 days', '1 days', 'NaT'])
assert not idx.equals(idx2)
assert not idx.equals(idx2.copy())
assert not idx.equals(idx2.astype(object))
assert not idx.astype(object).equals(idx2)
assert not idx.astype(object).equals(idx2.astype(object))
assert not idx.equals(list(idx2))
assert not idx.equals(pd.Series(idx2))
oob = Index([timedelta(days=10 ** 6)] * 3, dtype=object)
assert not idx.equals(oob)
assert not idx2.equals(oob)
oob2 = Index([np.timedelta64(x) for x in oob], dtype=object)
assert (oob == oob2).all()
assert not idx.equals(oob2)
assert not idx2.equals(oob2)
oob3 = oob.map(np.timedelta64)
assert (oob3 == oob).all()
assert not idx.equals(oob3)
assert not idx2.equals(oob3)
```

## Next Steps


---

*Source: test_equals.py:147 | Complexity: Intermediate | Last updated: 2026-06-02*