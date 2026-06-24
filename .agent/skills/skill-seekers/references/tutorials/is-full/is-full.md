# How To: Is Full

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test is full

## Prerequisites

**Required Modules:**
- `pytest`
- `pandas`


## Step-by-Step Guide

### Step 1: Assign index = PeriodIndex(...)

```python
index = PeriodIndex([2005, 2007, 2009], freq='Y')
```

**Verification:**
```python
assert not index.is_full
```

### Step 2: Assign index = PeriodIndex(...)

```python
index = PeriodIndex([2005, 2006, 2007], freq='Y')
```

**Verification:**
```python
assert index.is_full
```

### Step 3: Assign index = PeriodIndex(...)

```python
index = PeriodIndex([2005, 2005, 2007], freq='Y')
```

**Verification:**
```python
assert not index.is_full
```

### Step 4: Assign index = PeriodIndex(...)

```python
index = PeriodIndex([2005, 2005, 2006], freq='Y')
```

**Verification:**
```python
assert index.is_full
```

### Step 5: Assign index = PeriodIndex(...)

```python
index = PeriodIndex([2006, 2005, 2005], freq='Y')
```

**Verification:**
```python
assert index[:0].is_full
```

### Step 6: index.is_full

```python
index.is_full
```


## Complete Example

```python
# Workflow
index = PeriodIndex([2005, 2007, 2009], freq='Y')
assert not index.is_full
index = PeriodIndex([2005, 2006, 2007], freq='Y')
assert index.is_full
index = PeriodIndex([2005, 2005, 2007], freq='Y')
assert not index.is_full
index = PeriodIndex([2005, 2005, 2006], freq='Y')
assert index.is_full
index = PeriodIndex([2006, 2005, 2005], freq='Y')
with pytest.raises(ValueError, match='Index is not monotonic'):
    index.is_full
assert index[:0].is_full
```

## Next Steps


---

*Source: test_is_full.py:6 | Complexity: Intermediate | Last updated: 2026-06-02*