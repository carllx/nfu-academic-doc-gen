# How To: Monotone Dti Indexing Bug

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test monotone DTI indexing bug

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(list(range(5)))
```

### Step 2: Assign date_list = value

```python
date_list = ['2018-01-02', '2017-02-10', '2016-03-10', '2015-03-15', '2014-03-16']
```

### Step 3: Assign date_index = DatetimeIndex(...)

```python
date_index = DatetimeIndex(date_list)
```

### Step 4: Assign unknown = date_index

```python
df['date'] = date_index
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame({0: list(range(5)), 'date': date_index})
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```

### Step 7: Assign dti = date_range(...)

```python
dti = date_range('20170101 01:00:00', periods=3)
```

### Step 8: Assign df = DataFrame(...)

```python
df = DataFrame({'A': [1, 2, 3]}, index=dti[::-1])
```

### Step 9: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': 1}, index=dti[-1:][::-1])
```

### Step 10: Assign result = value

```python
result = df.loc['2017-01-03']
```

### Step 11: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 12: Assign result2 = value

```python
result2 = df.iloc[::-1].loc['2017-01-03']
```

### Step 13: Assign expected2 = value

```python
expected2 = expected.iloc[::-1]
```

### Step 14: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result2, expected2)
```


## Complete Example

```python
# Workflow
df = DataFrame(list(range(5)))
date_list = ['2018-01-02', '2017-02-10', '2016-03-10', '2015-03-15', '2014-03-16']
date_index = DatetimeIndex(date_list)
df['date'] = date_index
expected = DataFrame({0: list(range(5)), 'date': date_index})
tm.assert_frame_equal(df, expected)
dti = date_range('20170101 01:00:00', periods=3)
df = DataFrame({'A': [1, 2, 3]}, index=dti[::-1])
expected = DataFrame({'A': 1}, index=dti[-1:][::-1])
result = df.loc['2017-01-03']
tm.assert_frame_equal(result, expected)
result2 = df.iloc[::-1].loc['2017-01-03']
expected2 = expected.iloc[::-1]
tm.assert_frame_equal(result2, expected2)
```

## Next Steps


---

*Source: test_partial_slicing.py:91 | Complexity: Advanced | Last updated: 2026-06-02*