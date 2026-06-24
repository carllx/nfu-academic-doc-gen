# How To: Merge Asof Multiby With Categorical

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test merge asof multiby with categorical

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pytz`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.reshape.merge`


## Step-by-Step Guide

### Step 1: Assign left = pd.DataFrame(...)

```python
left = pd.DataFrame({'c1': pd.Categorical(['a', 'a', 'b', 'b'], categories=['a', 'b']), 'c2': ['x'] * 4, 't': [1] * 4, 'v': range(4)})
```

### Step 2: Assign right = pd.DataFrame(...)

```python
right = pd.DataFrame({'c1': pd.Categorical(['b', 'b'], categories=['b', 'a']), 'c2': ['x'] * 2, 't': [1, 2], 'v': range(2)})
```

### Step 3: Assign result = merge_asof(...)

```python
result = merge_asof(left, right, by=['c1', 'c2'], on='t', direction='forward', suffixes=['_left', '_right'])
```

### Step 4: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({'c1': pd.Categorical(['a', 'a', 'b', 'b'], categories=['a', 'b']), 'c2': ['x'] * 4, 't': [1] * 4, 'v_left': range(4), 'v_right': [np.nan, np.nan, 0.0, 0.0]})
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
left = pd.DataFrame({'c1': pd.Categorical(['a', 'a', 'b', 'b'], categories=['a', 'b']), 'c2': ['x'] * 4, 't': [1] * 4, 'v': range(4)})
right = pd.DataFrame({'c1': pd.Categorical(['b', 'b'], categories=['b', 'a']), 'c2': ['x'] * 2, 't': [1, 2], 'v': range(2)})
result = merge_asof(left, right, by=['c1', 'c2'], on='t', direction='forward', suffixes=['_left', '_right'])
expected = pd.DataFrame({'c1': pd.Categorical(['a', 'a', 'b', 'b'], categories=['a', 'b']), 'c2': ['x'] * 4, 't': [1] * 4, 'v_left': range(4), 'v_right': [np.nan, np.nan, 0.0, 0.0]})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_merge_asof.py:3619 | Complexity: Intermediate | Last updated: 2026-06-02*