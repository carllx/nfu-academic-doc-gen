# How To: Agg Mixed Column Aggregation

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test agg mixed column aggregation

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.indexes.datetimes`

**Setup Required:**
```python
# Fixtures: cases, a_mean, a_std, b_mean, b_std, request
```

## Step-by-Step Guide

### Step 1: Assign expected = pd.concat(...)

```python
expected = pd.concat([a_mean, a_std, b_mean, b_std], axis=1)
```

### Step 2: Assign expected.columns = pd.MultiIndex.from_product(...)

```python
expected.columns = pd.MultiIndex.from_product([['A', 'B'], ['mean', 'std']])
```

### Step 3: Assign msg = 'using SeriesGroupBy.[mean|std]'

```python
msg = 'using SeriesGroupBy.[mean|std]'
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign date_mean = unknown.mean(...)

```python
date_mean = cases['date'].mean()
```

### Step 6: Assign date_std = unknown.std(...)

```python
date_std = cases['date'].std()
```

### Step 7: Assign expected = pd.concat(...)

```python
expected = pd.concat([date_mean, date_std, expected], axis=1)
```

### Step 8: Assign expected.columns = pd.MultiIndex.from_product(...)

```python
expected.columns = pd.MultiIndex.from_product([['date', 'A', 'B'], ['mean', 'std']])
```

### Step 9: Assign result = cases.aggregate(...)

```python
result = cases.aggregate([np.mean, np.std])
```


## Complete Example

```python
# Setup
# Fixtures: cases, a_mean, a_std, b_mean, b_std, request

# Workflow
expected = pd.concat([a_mean, a_std, b_mean, b_std], axis=1)
expected.columns = pd.MultiIndex.from_product([['A', 'B'], ['mean', 'std']])
msg = 'using SeriesGroupBy.[mean|std]'
if 'df_mult' in request.node.callspec.id:
    date_mean = cases['date'].mean()
    date_std = cases['date'].std()
    expected = pd.concat([date_mean, date_std, expected], axis=1)
    expected.columns = pd.MultiIndex.from_product([['date', 'A', 'B'], ['mean', 'std']])
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = cases.aggregate([np.mean, np.std])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_resample_api.py:470 | Complexity: Advanced | Last updated: 2026-06-02*