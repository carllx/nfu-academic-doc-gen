# How To: Cython Fail Agg

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test cython fail agg

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.common`


## Step-by-Step Guide

### Step 1: Assign dr = bdate_range(...)

```python
dr = bdate_range('1/1/2000', periods=50)
```

### Step 2: Assign ts = Series(...)

```python
ts = Series(['A', 'B', 'C', 'D', 'E'] * 10, dtype=object, index=dr)
```

### Step 3: Assign grouped = ts.groupby(...)

```python
grouped = ts.groupby(lambda x: x.month)
```

### Step 4: Assign summed = grouped.sum(...)

```python
summed = grouped.sum()
```

### Step 5: Assign msg = 'using SeriesGroupBy.sum'

```python
msg = 'using SeriesGroupBy.sum'
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(summed, expected)
```

### Step 7: Assign expected = grouped.agg.astype(...)

```python
expected = grouped.agg(np.sum).astype(object)
```


## Complete Example

```python
# Workflow
dr = bdate_range('1/1/2000', periods=50)
ts = Series(['A', 'B', 'C', 'D', 'E'] * 10, dtype=object, index=dr)
grouped = ts.groupby(lambda x: x.month)
summed = grouped.sum()
msg = 'using SeriesGroupBy.sum'
with tm.assert_produces_warning(FutureWarning, match=msg):
    expected = grouped.agg(np.sum).astype(object)
tm.assert_series_equal(summed, expected)
```

## Next Steps


---

*Source: test_cython.py:166 | Complexity: Intermediate | Last updated: 2026-06-02*