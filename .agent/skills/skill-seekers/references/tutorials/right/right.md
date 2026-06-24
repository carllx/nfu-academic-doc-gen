# How To: Right

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test right

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.api.types`
- `pandas.core.reshape.tile`


## Step-by-Step Guide

### Step 1: Assign data = np.array(...)

```python
data = np.array([0.2, 1.4, 2.5, 6.2, 9.7, 2.1, 2.575])
```

### Step 2: Assign unknown = cut(...)

```python
result, bins = cut(data, 4, right=True, retbins=True)
```

### Step 3: Assign intervals = IntervalIndex.from_breaks(...)

```python
intervals = IntervalIndex.from_breaks(bins.round(3))
```

### Step 4: Assign expected = Categorical(...)

```python
expected = Categorical(intervals, ordered=True)
```

### Step 5: Assign expected = expected.take(...)

```python
expected = expected.take([0, 0, 0, 2, 3, 0, 0])
```

### Step 6: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(result, expected)
```

### Step 7: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(bins, np.array([0.1905, 2.575, 4.95, 7.325, 9.7]))
```


## Complete Example

```python
# Workflow
data = np.array([0.2, 1.4, 2.5, 6.2, 9.7, 2.1, 2.575])
result, bins = cut(data, 4, right=True, retbins=True)
intervals = IntervalIndex.from_breaks(bins.round(3))
expected = Categorical(intervals, ordered=True)
expected = expected.take([0, 0, 0, 2, 3, 0, 0])
tm.assert_categorical_equal(result, expected)
tm.assert_almost_equal(bins, np.array([0.1905, 2.575, 4.95, 7.325, 9.7]))
```

## Next Steps


---

*Source: test_cut.py:49 | Complexity: Intermediate | Last updated: 2026-06-02*