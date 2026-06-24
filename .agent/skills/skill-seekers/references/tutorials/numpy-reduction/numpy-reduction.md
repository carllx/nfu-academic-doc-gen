# How To: Numpy Reduction

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test numpy reduction

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `operator`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.groupby.grouper`
- `pandas.core.indexes.datetimes`

**Setup Required:**
```python
# Fixtures: test_series
```

## Step-by-Step Guide

### Step 1: Assign result = test_series.resample.prod(...)

```python
result = test_series.resample('YE', closed='right').prod()
```

### Step 2: Assign msg = 'using SeriesGroupBy.prod'

```python
msg = 'using SeriesGroupBy.prod'
```

### Step 3: Assign expected.index = value

```python
expected.index = result.index
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign expected = test_series.groupby.agg(...)

```python
expected = test_series.groupby(lambda x: x.year).agg(np.prod)
```


## Complete Example

```python
# Setup
# Fixtures: test_series

# Workflow
result = test_series.resample('YE', closed='right').prod()
msg = 'using SeriesGroupBy.prod'
with tm.assert_produces_warning(FutureWarning, match=msg):
    expected = test_series.groupby(lambda x: x.year).agg(np.prod)
expected.index = result.index
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_time_grouper.py:58 | Complexity: Intermediate | Last updated: 2026-06-02*