# How To: Pivot With Interval Index Margins

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test pivot with interval index margins

## Prerequisites

**Required Modules:**
- `datetime`
- `itertools`
- `re`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.api.types`
- `pandas.core.reshape`
- `pandas.core.reshape.pivot`


## Step-by-Step Guide

### Step 1: Assign ordered_cat = pd.IntervalIndex.from_arrays(...)

```python
ordered_cat = pd.IntervalIndex.from_arrays([0, 0, 1, 1], [1, 1, 2, 2])
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'A': np.arange(4, 0, -1, dtype=np.intp), 'B': ['a', 'b', 'a', 'b'], 'C': Categorical(ordered_cat, ordered=True).sort_values(ascending=False)})
```

### Step 3: Assign msg = 'The default value of observed=False is deprecated'

```python
msg = 'The default value of observed=False is deprecated'
```

### Step 4: Assign result = value

```python
result = pivot_tab['All']
```

### Step 5: Assign expected = Series(...)

```python
expected = Series([3, 7, 10], index=Index([pd.Interval(0, 1), pd.Interval(1, 2), 'All'], name='C'), name='All', dtype=np.intp)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 7: Assign pivot_tab = pivot_table(...)

```python
pivot_tab = pivot_table(df, index='C', columns='B', values='A', aggfunc='sum', margins=True)
```


## Complete Example

```python
# Workflow
ordered_cat = pd.IntervalIndex.from_arrays([0, 0, 1, 1], [1, 1, 2, 2])
df = DataFrame({'A': np.arange(4, 0, -1, dtype=np.intp), 'B': ['a', 'b', 'a', 'b'], 'C': Categorical(ordered_cat, ordered=True).sort_values(ascending=False)})
msg = 'The default value of observed=False is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg):
    pivot_tab = pivot_table(df, index='C', columns='B', values='A', aggfunc='sum', margins=True)
result = pivot_tab['All']
expected = Series([3, 7, 10], index=Index([pd.Interval(0, 1), pd.Interval(1, 2), 'All'], name='C'), name='All', dtype=np.intp)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_pivot.py:325 | Complexity: Intermediate | Last updated: 2026-06-02*