# How To: Series Agg Multikey

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test series agg multikey

## Prerequisites

**Required Modules:**
- `datetime`
- `functools`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.io.formats.printing`
- `pandas.tests.extension.decimal.array`


## Step-by-Step Guide

### Step 1: Assign ts = Series(...)

```python
ts = Series(np.arange(10, dtype=np.float64), index=date_range('2020-01-01', periods=10))
```

### Step 2: Assign grouped = ts.groupby(...)

```python
grouped = ts.groupby([lambda x: x.year, lambda x: x.month])
```

### Step 3: Assign result = grouped.agg(...)

```python
result = grouped.agg('sum')
```

### Step 4: Assign expected = grouped.sum(...)

```python
expected = grouped.sum()
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
ts = Series(np.arange(10, dtype=np.float64), index=date_range('2020-01-01', periods=10))
grouped = ts.groupby([lambda x: x.year, lambda x: x.month])
result = grouped.agg('sum')
expected = grouped.sum()
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_other.py:298 | Complexity: Intermediate | Last updated: 2026-06-02*