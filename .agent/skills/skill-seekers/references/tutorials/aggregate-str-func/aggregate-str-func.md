# How To: Aggregate Str Func

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test aggregate str func

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `functools`
- `functools`
- `re`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.groupby.grouper`

**Setup Required:**
```python
# Fixtures: tsframe, groupbyfunc
```

## Step-by-Step Guide

### Step 1: Assign grouped = tsframe.groupby(...)

```python
grouped = tsframe.groupby(groupbyfunc)
```

### Step 2: Assign result = unknown.agg(...)

```python
result = grouped['A'].agg('std')
```

### Step 3: Assign expected = unknown.std(...)

```python
expected = grouped['A'].std()
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign result = grouped.aggregate(...)

```python
result = grouped.aggregate('var')
```

### Step 6: Assign expected = grouped.var(...)

```python
expected = grouped.var()
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Assign result = grouped.agg(...)

```python
result = grouped.agg({'A': 'var', 'B': 'std', 'C': 'mean', 'D': 'sem'})
```

### Step 9: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': grouped['A'].var(), 'B': grouped['B'].std(), 'C': grouped['C'].mean(), 'D': grouped['D'].sem()})
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: tsframe, groupbyfunc

# Workflow
grouped = tsframe.groupby(groupbyfunc)
result = grouped['A'].agg('std')
expected = grouped['A'].std()
tm.assert_series_equal(result, expected)
result = grouped.aggregate('var')
expected = grouped.var()
tm.assert_frame_equal(result, expected)
result = grouped.agg({'A': 'var', 'B': 'std', 'C': 'mean', 'D': 'sem'})
expected = DataFrame({'A': grouped['A'].var(), 'B': grouped['B'].std(), 'C': grouped['C'].mean(), 'D': grouped['D'].sem()})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_aggregate.py:196 | Complexity: Advanced | Last updated: 2026-06-02*