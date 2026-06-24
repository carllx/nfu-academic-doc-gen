# How To: Sort Values Nat

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test sort values nat

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.util.version`


## Step-by-Step Guide

### Step 1: Assign d1 = value

```python
d1 = [Timestamp(x) for x in ['2016-01-01', '2015-01-01', np.nan, '2016-01-01']]
```

### Step 2: Assign d2 = value

```python
d2 = [Timestamp(x) for x in ['2017-01-01', '2014-01-01', '2016-01-01', '2015-01-01']]
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame({'a': d1, 'b': d2}, index=[0, 1, 2, 3])
```

### Step 4: Assign d3 = value

```python
d3 = [Timestamp(x) for x in ['2015-01-01', '2016-01-01', '2016-01-01', np.nan]]
```

### Step 5: Assign d4 = value

```python
d4 = [Timestamp(x) for x in ['2014-01-01', '2015-01-01', '2017-01-01', '2016-01-01']]
```

### Step 6: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': d3, 'b': d4}, index=[1, 3, 0, 2])
```

### Step 7: Assign sorted_df = df.sort_values(...)

```python
sorted_df = df.sort_values(by=['a', 'b'])
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(sorted_df, expected)
```


## Complete Example

```python
# Workflow
d1 = [Timestamp(x) for x in ['2016-01-01', '2015-01-01', np.nan, '2016-01-01']]
d2 = [Timestamp(x) for x in ['2017-01-01', '2014-01-01', '2016-01-01', '2015-01-01']]
df = DataFrame({'a': d1, 'b': d2}, index=[0, 1, 2, 3])
d3 = [Timestamp(x) for x in ['2015-01-01', '2016-01-01', '2016-01-01', np.nan]]
d4 = [Timestamp(x) for x in ['2014-01-01', '2015-01-01', '2017-01-01', '2016-01-01']]
expected = DataFrame({'a': d3, 'b': d4}, index=[1, 3, 0, 2])
sorted_df = df.sort_values(by=['a', 'b'])
tm.assert_frame_equal(sorted_df, expected)
```

## Next Steps


---

*Source: test_sort_values.py:512 | Complexity: Advanced | Last updated: 2026-06-02*