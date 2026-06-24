# How To: Is Unique Interval

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: Interval specific tests for is_unique in addition to base class tests

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `itertools`
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.common`

**Setup Required:**
```python
# Fixtures: closed
```

## Step-by-Step Guide

### Step 1: '\n        Interval specific tests for is_unique in addition to base class tests\n        '

```python
'\n        Interval specific tests for is_unique in addition to base class tests\n        '
```

**Verification:**
```python
assert idx.is_unique is True
```

### Step 2: Assign idx = IntervalIndex.from_tuples(...)

```python
idx = IntervalIndex.from_tuples([(0, 1), (0.5, 1.5)], closed=closed)
```

**Verification:**
```python
assert idx.is_unique is True
```

### Step 3: Assign idx = IntervalIndex.from_tuples(...)

```python
idx = IntervalIndex.from_tuples([(1, 2), (1, 3), (2, 3)], closed=closed)
```

**Verification:**
```python
assert idx.is_unique is True
```

### Step 4: Assign idx = IntervalIndex.from_tuples(...)

```python
idx = IntervalIndex.from_tuples([(-1, 1), (-2, 2)], closed=closed)
```

**Verification:**
```python
assert idx.is_unique is True
```

### Step 5: Assign idx = IntervalIndex.from_tuples(...)

```python
idx = IntervalIndex.from_tuples([(np.nan, np.nan)], closed=closed)
```

**Verification:**
```python
assert idx.is_unique is False
```

### Step 6: Assign idx = IntervalIndex.from_tuples(...)

```python
idx = IntervalIndex.from_tuples([(np.nan, np.nan), (np.nan, np.nan)], closed=closed)
```

**Verification:**
```python
assert idx.is_unique is False
```


## Complete Example

```python
# Setup
# Fixtures: closed

# Workflow
'\n        Interval specific tests for is_unique in addition to base class tests\n        '
idx = IntervalIndex.from_tuples([(0, 1), (0.5, 1.5)], closed=closed)
assert idx.is_unique is True
idx = IntervalIndex.from_tuples([(1, 2), (1, 3), (2, 3)], closed=closed)
assert idx.is_unique is True
idx = IntervalIndex.from_tuples([(-1, 1), (-2, 2)], closed=closed)
assert idx.is_unique is True
idx = IntervalIndex.from_tuples([(np.nan, np.nan)], closed=closed)
assert idx.is_unique is True
idx = IntervalIndex.from_tuples([(np.nan, np.nan), (np.nan, np.nan)], closed=closed)
assert idx.is_unique is False
```

## Next Steps


---

*Source: test_interval.py:237 | Complexity: Intermediate | Last updated: 2026-06-02*