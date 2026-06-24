# How To: Sort Index Multiindex

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test sort index multiindex

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: level
```

## Step-by-Step Guide

### Step 1: Assign mi = MultiIndex.from_tuples(...)

```python
mi = MultiIndex.from_tuples([[1, 1, 3], [1, 1, 1]], names=list('ABC'))
```

### Step 2: Assign s = Series(...)

```python
s = Series([1, 2], mi)
```

### Step 3: Assign backwards = value

```python
backwards = s.iloc[[1, 0]]
```

### Step 4: Assign res = s.sort_index(...)

```python
res = s.sort_index(level=level)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(backwards, res)
```

### Step 6: Assign res = s.sort_index(...)

```python
res = s.sort_index(level=level, sort_remaining=False)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s, res)
```


## Complete Example

```python
# Setup
# Fixtures: level

# Workflow
mi = MultiIndex.from_tuples([[1, 1, 3], [1, 1, 1]], names=list('ABC'))
s = Series([1, 2], mi)
backwards = s.iloc[[1, 0]]
res = s.sort_index(level=level)
tm.assert_series_equal(backwards, res)
res = s.sort_index(level=level, sort_remaining=False)
tm.assert_series_equal(s, res)
```

## Next Steps


---

*Source: test_sort_index.py:100 | Complexity: Intermediate | Last updated: 2026-06-02*