# How To: Concat Multiindex Datetime Nat

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concat multiindex datetime nat

## Prerequisites

**Required Modules:**
- `datetime`
- `datetime`
- `dateutil`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign left = DataFrame(...)

```python
left = DataFrame({'a': 1}, index=MultiIndex.from_tuples([(1, pd.NaT)]))
```

### Step 2: Assign right = DataFrame(...)

```python
right = DataFrame({'b': 2}, index=MultiIndex.from_tuples([(1, pd.NaT), (2, pd.NaT)]))
```

### Step 3: Assign result = concat(...)

```python
result = concat([left, right], axis='columns')
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': [1.0, np.nan], 'b': 2}, MultiIndex.from_tuples([(1, pd.NaT), (2, pd.NaT)]))
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
left = DataFrame({'a': 1}, index=MultiIndex.from_tuples([(1, pd.NaT)]))
right = DataFrame({'b': 2}, index=MultiIndex.from_tuples([(1, pd.NaT), (2, pd.NaT)]))
result = concat([left, right], axis='columns')
expected = DataFrame({'a': [1.0, np.nan], 'b': 2}, MultiIndex.from_tuples([(1, pd.NaT), (2, pd.NaT)]))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_datetimes.py:557 | Complexity: Intermediate | Last updated: 2026-06-02*