# How To: Group Shift With Multiple Periods

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test group shift with multiple periods

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 2, 3, 3, 2], 'b': [True, True, False, False, True]})
```

### Step 2: Assign shifted_df = unknown.shift(...)

```python
shifted_df = df.groupby('b')[['a']].shift([0, 1])
```

### Step 3: Assign expected_df = DataFrame(...)

```python
expected_df = DataFrame({'a_0': [1, 2, 3, 3, 2], 'a_1': [np.nan, 1.0, np.nan, 3.0, 2.0]})
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(shifted_df, expected_df)
```

### Step 5: Assign shifted_series = unknown.shift(...)

```python
shifted_series = df.groupby('b')['a'].shift([0, 1])
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(shifted_series, expected_df)
```


## Complete Example

```python
# Workflow
df = DataFrame({'a': [1, 2, 3, 3, 2], 'b': [True, True, False, False, True]})
shifted_df = df.groupby('b')[['a']].shift([0, 1])
expected_df = DataFrame({'a_0': [1, 2, 3, 3, 2], 'a_1': [np.nan, 1.0, np.nan, 3.0, 2.0]})
tm.assert_frame_equal(shifted_df, expected_df)
shifted_series = df.groupby('b')['a'].shift([0, 1])
tm.assert_frame_equal(shifted_series, expected_df)
```

## Next Steps


---

*Source: test_groupby_shift_diff.py:190 | Complexity: Intermediate | Last updated: 2026-06-02*