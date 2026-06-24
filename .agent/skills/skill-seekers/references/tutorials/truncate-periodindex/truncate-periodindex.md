# How To: Truncate Periodindex

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test truncate periodindex

## Prerequisites

**Required Modules:**
- `datetime`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx1 = pd.PeriodIndex(...)

```python
idx1 = pd.PeriodIndex([pd.Period('2017-09-02'), pd.Period('2017-09-02'), pd.Period('2017-09-03')])
```

### Step 2: Assign series1 = Series(...)

```python
series1 = Series([1, 2, 3], index=idx1)
```

### Step 3: Assign result1 = series1.truncate(...)

```python
result1 = series1.truncate(after='2017-09-02')
```

### Step 4: Assign expected_idx1 = pd.PeriodIndex(...)

```python
expected_idx1 = pd.PeriodIndex([pd.Period('2017-09-02'), pd.Period('2017-09-02')])
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result1, Series([1, 2], index=expected_idx1))
```

### Step 6: Assign idx2 = pd.PeriodIndex(...)

```python
idx2 = pd.PeriodIndex([pd.Period('2017-09-03'), pd.Period('2017-09-02'), pd.Period('2017-09-03')])
```

### Step 7: Assign series2 = Series(...)

```python
series2 = Series([1, 2, 3], index=idx2)
```

### Step 8: Assign result2 = series2.sort_index.truncate(...)

```python
result2 = series2.sort_index().truncate(after='2017-09-02')
```

### Step 9: Assign expected_idx2 = pd.PeriodIndex(...)

```python
expected_idx2 = pd.PeriodIndex([pd.Period('2017-09-02')])
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result2, Series([2], index=expected_idx2))
```


## Complete Example

```python
# Workflow
idx1 = pd.PeriodIndex([pd.Period('2017-09-02'), pd.Period('2017-09-02'), pd.Period('2017-09-03')])
series1 = Series([1, 2, 3], index=idx1)
result1 = series1.truncate(after='2017-09-02')
expected_idx1 = pd.PeriodIndex([pd.Period('2017-09-02'), pd.Period('2017-09-02')])
tm.assert_series_equal(result1, Series([1, 2], index=expected_idx1))
idx2 = pd.PeriodIndex([pd.Period('2017-09-03'), pd.Period('2017-09-02'), pd.Period('2017-09-03')])
series2 = Series([1, 2, 3], index=idx2)
result2 = series2.sort_index().truncate(after='2017-09-02')
expected_idx2 = pd.PeriodIndex([pd.Period('2017-09-02')])
tm.assert_series_equal(result2, Series([2], index=expected_idx2))
```

## Next Steps


---

*Source: test_truncate.py:28 | Complexity: Advanced | Last updated: 2026-06-02*