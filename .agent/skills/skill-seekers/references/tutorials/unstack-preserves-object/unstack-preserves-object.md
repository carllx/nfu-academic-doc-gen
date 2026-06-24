# How To: Unstack Preserves Object

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test unstack preserves object

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign mi = MultiIndex.from_product(...)

```python
mi = MultiIndex.from_product([['bar', 'foo'], ['one', 'two']])
```

**Verification:**
```python
assert (res1.dtypes == object).all()
```

### Step 2: Assign ser = Series(...)

```python
ser = Series(np.arange(4.0), index=mi, dtype=object)
```

**Verification:**
```python
assert (res2.dtypes == object).all()
```

### Step 3: Assign res1 = ser.unstack(...)

```python
res1 = ser.unstack()
```

**Verification:**
```python
assert (res1.dtypes == object).all()
```

### Step 4: Assign res2 = ser.unstack(...)

```python
res2 = ser.unstack(level=0)
```

**Verification:**
```python
assert (res2.dtypes == object).all()
```


## Complete Example

```python
# Workflow
mi = MultiIndex.from_product([['bar', 'foo'], ['one', 'two']])
ser = Series(np.arange(4.0), index=mi, dtype=object)
res1 = ser.unstack()
assert (res1.dtypes == object).all()
res2 = ser.unstack(level=0)
assert (res2.dtypes == object).all()
```

## Next Steps


---

*Source: test_unstack.py:15 | Complexity: Intermediate | Last updated: 2026-06-02*