# How To: Union Freq Infer

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test union freq infer

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tseries.offsets`


## Step-by-Step Guide

### Step 1: Assign tdi = timedelta_range(...)

```python
tdi = timedelta_range('1 Day', periods=5)
```

**Verification:**
```python
assert left.freq is None
```

### Step 2: Assign left = value

```python
left = tdi[[0, 1, 3, 4]]
```

**Verification:**
```python
assert right.freq is None
```

### Step 3: Assign right = value

```python
right = tdi[[2, 3, 1]]
```

**Verification:**
```python
assert result.freq == 'D'
```

### Step 4: Assign result = left.union(...)

```python
result = left.union(right)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, tdi)
```

**Verification:**
```python
assert result.freq == 'D'
```


## Complete Example

```python
# Workflow
tdi = timedelta_range('1 Day', periods=5)
left = tdi[[0, 1, 3, 4]]
right = tdi[[2, 3, 1]]
assert left.freq is None
assert right.freq is None
result = left.union(right)
tm.assert_index_equal(result, tdi)
assert result.freq == 'D'
```

## Next Steps


---

*Source: test_setops.py:80 | Complexity: Intermediate | Last updated: 2026-06-02*