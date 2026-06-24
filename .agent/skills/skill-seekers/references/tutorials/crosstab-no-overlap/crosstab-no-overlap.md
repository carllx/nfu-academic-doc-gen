# How To: Crosstab No Overlap

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test crosstab no overlap

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign s1 = Series(...)

```python
s1 = Series([1, 2, 3], index=[1, 2, 3])
```

### Step 2: Assign s2 = Series(...)

```python
s2 = Series([4, 5, 6], index=[4, 5, 6])
```

### Step 3: Assign actual = crosstab(...)

```python
actual = crosstab(s1, s2)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame(index=Index([], dtype='int64', name='row_0'), columns=Index([], dtype='int64', name='col_0'))
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(actual, expected)
```


## Complete Example

```python
# Workflow
s1 = Series([1, 2, 3], index=[1, 2, 3])
s2 = Series([4, 5, 6], index=[4, 5, 6])
actual = crosstab(s1, s2)
expected = DataFrame(index=Index([], dtype='int64', name='row_0'), columns=Index([], dtype='int64', name='col_0'))
tm.assert_frame_equal(actual, expected)
```

## Next Steps


---

*Source: test_crosstab.py:239 | Complexity: Intermediate | Last updated: 2026-06-02*