# How To: Concat Categorical Tz

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concat categorical tz

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign a = Series(...)

```python
a = Series(pd.date_range('2017-01-01', periods=2, tz='US/Pacific'))
```

### Step 2: Assign b = Series(...)

```python
b = Series(['a', 'b'], dtype='category')
```

### Step 3: Assign result = pd.concat(...)

```python
result = pd.concat([a, b], ignore_index=True)
```

### Step 4: Assign expected = Series(...)

```python
expected = Series([pd.Timestamp('2017-01-01', tz='US/Pacific'), pd.Timestamp('2017-01-02', tz='US/Pacific'), 'a', 'b'])
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
a = Series(pd.date_range('2017-01-01', periods=2, tz='US/Pacific'))
b = Series(['a', 'b'], dtype='category')
result = pd.concat([a, b], ignore_index=True)
expected = Series([pd.Timestamp('2017-01-01', tz='US/Pacific'), pd.Timestamp('2017-01-02', tz='US/Pacific'), 'a', 'b'])
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_categorical.py:156 | Complexity: Intermediate | Last updated: 2026-06-02*