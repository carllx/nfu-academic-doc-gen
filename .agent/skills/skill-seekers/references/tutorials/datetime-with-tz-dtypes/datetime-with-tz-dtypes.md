# How To: Datetime With Tz Dtypes

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test datetime with tz dtypes

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign tzframe = DataFrame(...)

```python
tzframe = DataFrame({'A': date_range('20130101', periods=3), 'B': date_range('20130101', periods=3, tz='US/Eastern'), 'C': date_range('20130101', periods=3, tz='CET')})
```

### Step 2: Assign unknown = value

```python
tzframe.iloc[1, 1] = pd.NaT
```

### Step 3: Assign unknown = value

```python
tzframe.iloc[1, 2] = pd.NaT
```

### Step 4: Assign result = tzframe.dtypes.sort_index(...)

```python
result = tzframe.dtypes.sort_index()
```

### Step 5: Assign expected = Series(...)

```python
expected = Series([np.dtype('datetime64[ns]'), DatetimeTZDtype('ns', 'US/Eastern'), DatetimeTZDtype('ns', 'CET')], ['A', 'B', 'C'])
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
tzframe = DataFrame({'A': date_range('20130101', periods=3), 'B': date_range('20130101', periods=3, tz='US/Eastern'), 'C': date_range('20130101', periods=3, tz='CET')})
tzframe.iloc[1, 1] = pd.NaT
tzframe.iloc[1, 2] = pd.NaT
result = tzframe.dtypes.sort_index()
expected = Series([np.dtype('datetime64[ns]'), DatetimeTZDtype('ns', 'US/Eastern'), DatetimeTZDtype('ns', 'CET')], ['A', 'B', 'C'])
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_dtypes.py:41 | Complexity: Intermediate | Last updated: 2026-06-02*