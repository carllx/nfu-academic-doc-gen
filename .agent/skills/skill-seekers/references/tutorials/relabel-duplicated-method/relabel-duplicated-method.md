# How To: Relabel Duplicated Method

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test relabel duplicated method

## Prerequisites

**Required Modules:**
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame({'A': [1, 2, 1, 2], 'B': [1, 2, 3, 4]})
```

### Step 2: Assign result = unknown.agg(...)

```python
result = df['A'].agg(foo='sum', bar='sum')
```

### Step 3: Assign expected = pd.Series(...)

```python
expected = pd.Series([6, 6], index=['foo', 'bar'], name='A')
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign msg = 'using Series.min'

```python
msg = 'using Series.min'
```

### Step 6: Assign expected = pd.Series(...)

```python
expected = pd.Series([1, 1], index=['foo', 'bar'], name='B')
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 8: Assign result = unknown.agg(...)

```python
result = df['B'].agg(foo=min, bar='min')
```


## Complete Example

```python
# Workflow
df = pd.DataFrame({'A': [1, 2, 1, 2], 'B': [1, 2, 3, 4]})
result = df['A'].agg(foo='sum', bar='sum')
expected = pd.Series([6, 6], index=['foo', 'bar'], name='A')
tm.assert_series_equal(result, expected)
msg = 'using Series.min'
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = df['B'].agg(foo=min, bar='min')
expected = pd.Series([1, 1], index=['foo', 'bar'], name='B')
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_series_apply_relabeling.py:26 | Complexity: Advanced | Last updated: 2026-06-02*