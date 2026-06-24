# How To: Is Overlapping Endpoints

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: shared endpoints are marked as overlapping

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `itertools`
- `numpy`
- `pytest`
- `pandas._libs.interval`
- `pandas.compat`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: closed, order
```

## Step-by-Step Guide

### Step 1: 'shared endpoints are marked as overlapping'

```python
'shared endpoints are marked as overlapping'
```

**Verification:**
```python
assert result is expected
```

### Step 2: Assign unknown = value

```python
left, right = (np.arange(3, dtype='int64'), np.arange(1, 4))
```

### Step 3: Assign tree = IntervalTree(...)

```python
tree = IntervalTree(left[order], right[order], closed=closed)
```

### Step 4: Assign result = value

```python
result = tree.is_overlapping
```

### Step 5: Assign expected = value

```python
expected = closed == 'both'
```

**Verification:**
```python
assert result is expected
```


## Complete Example

```python
# Setup
# Fixtures: closed, order

# Workflow
'shared endpoints are marked as overlapping'
left, right = (np.arange(3, dtype='int64'), np.arange(1, 4))
tree = IntervalTree(left[order], right[order], closed=closed)
result = tree.is_overlapping
expected = closed == 'both'
assert result is expected
```

## Next Steps


---

*Source: test_interval_tree.py:159 | Complexity: Intermediate | Last updated: 2026-06-02*