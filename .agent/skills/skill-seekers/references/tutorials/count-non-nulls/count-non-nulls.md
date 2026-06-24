# How To: Count Non Nulls

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test count non nulls

## Prerequisites

**Required Modules:**
- `itertools`
- `string`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame([[1, 2, 'foo'], [1, np.nan, 'bar'], [3, np.nan, np.nan]], columns=['A', 'B', 'C'])
```

### Step 2: Assign count_as = df.groupby.count(...)

```python
count_as = df.groupby('A').count()
```

### Step 3: Assign count_not_as = df.groupby.count(...)

```python
count_not_as = df.groupby('A', as_index=False).count()
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1, 2], [0, 0]], columns=['B', 'C'], index=[1, 3])
```

### Step 5: Assign expected.index.name = 'A'

```python
expected.index.name = 'A'
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(count_not_as, expected.reset_index())
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(count_as, expected)
```

### Step 8: Assign count_B = unknown.count(...)

```python
count_B = df.groupby('A')['B'].count()
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(count_B, expected['B'])
```


## Complete Example

```python
# Workflow
df = DataFrame([[1, 2, 'foo'], [1, np.nan, 'bar'], [3, np.nan, np.nan]], columns=['A', 'B', 'C'])
count_as = df.groupby('A').count()
count_not_as = df.groupby('A', as_index=False).count()
expected = DataFrame([[1, 2], [0, 0]], columns=['B', 'C'], index=[1, 3])
expected.index.name = 'A'
tm.assert_frame_equal(count_not_as, expected.reset_index())
tm.assert_frame_equal(count_as, expected)
count_B = df.groupby('A')['B'].count()
tm.assert_series_equal(count_B, expected['B'])
```

## Next Steps


---

*Source: test_counting.py:298 | Complexity: Advanced | Last updated: 2026-06-02*