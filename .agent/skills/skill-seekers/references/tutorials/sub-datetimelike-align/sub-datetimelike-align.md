# How To: Sub Datetimelike Align

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test sub datetimelike align

## Prerequisites

**Required Modules:**
- `datetime`
- `decimal`
- `operator`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas._libs.tslibs`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`
- `pandas.core.computation`
- `pandas.core.computation.check`


## Step-by-Step Guide

### Step 1: Assign dt = Series(...)

```python
dt = Series(date_range('2012-1-1', periods=3, freq='D'))
```

### Step 2: Assign unknown = value

```python
dt.iloc[2] = np.nan
```

### Step 3: Assign dt2 = value

```python
dt2 = dt[::-1]
```

### Step 4: Assign expected = Series(...)

```python
expected = Series([timedelta(0), timedelta(0), pd.NaT])
```

### Step 5: Assign result = value

```python
result = dt2 - dt
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 7: Assign expected = Series(...)

```python
expected = Series(expected, name=0)
```

### Step 8: Assign result = value

```python
result = (dt2.to_frame() - dt.to_frame())[0]
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
dt = Series(date_range('2012-1-1', periods=3, freq='D'))
dt.iloc[2] = np.nan
dt2 = dt[::-1]
expected = Series([timedelta(0), timedelta(0), pd.NaT])
result = dt2 - dt
tm.assert_series_equal(result, expected)
expected = Series(expected, name=0)
result = (dt2.to_frame() - dt.to_frame())[0]
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_arithmetic.py:263 | Complexity: Advanced | Last updated: 2026-06-02*