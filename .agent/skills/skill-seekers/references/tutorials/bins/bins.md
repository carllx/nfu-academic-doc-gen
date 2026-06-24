# How To: Bins

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test bins

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.api.types`
- `pandas.core.reshape.tile`

**Setup Required:**
```python
# Fixtures: func
```

## Step-by-Step Guide

### Step 1: Assign data = func(...)

```python
data = func([0.2, 1.4, 2.5, 6.2, 9.7, 2.1])
```

### Step 2: Assign unknown = cut(...)

```python
result, bins = cut(data, 3, retbins=True)
```

### Step 3: Assign intervals = IntervalIndex.from_breaks(...)

```python
intervals = IntervalIndex.from_breaks(bins.round(3))
```

### Step 4: Assign intervals = intervals.take(...)

```python
intervals = intervals.take([0, 0, 0, 1, 2, 0])
```

### Step 5: Assign expected = Categorical(...)

```python
expected = Categorical(intervals, ordered=True)
```

### Step 6: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(result, expected)
```

### Step 7: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(bins, np.array([0.1905, 3.36666667, 6.53333333, 9.7]))
```


## Complete Example

```python
# Setup
# Fixtures: func

# Workflow
data = func([0.2, 1.4, 2.5, 6.2, 9.7, 2.1])
result, bins = cut(data, 3, retbins=True)
intervals = IntervalIndex.from_breaks(bins.round(3))
intervals = intervals.take([0, 0, 0, 1, 2, 0])
expected = Categorical(intervals, ordered=True)
tm.assert_categorical_equal(result, expected)
tm.assert_almost_equal(bins, np.array([0.1905, 3.36666667, 6.53333333, 9.7]))
```

## Next Steps


---

*Source: test_cut.py:37 | Complexity: Intermediate | Last updated: 2026-06-02*