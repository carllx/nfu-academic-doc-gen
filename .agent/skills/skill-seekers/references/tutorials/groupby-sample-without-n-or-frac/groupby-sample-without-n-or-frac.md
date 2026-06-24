# How To: Groupby Sample Without N Or Frac

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test groupby sample without n or frac

## Prerequisites

**Required Modules:**
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign values = value

```python
values = [1] * 10 + [2] * 10
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'a': values, 'b': values})
```

### Step 3: Assign result = df.groupby.sample(...)

```python
result = df.groupby('a').sample(n=None, frac=None)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': [1, 2], 'b': [1, 2]}, index=result.index)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign result = unknown.sample(...)

```python
result = df.groupby('a')['b'].sample(n=None, frac=None)
```

### Step 7: Assign expected = Series(...)

```python
expected = Series([1, 2], name='b', index=result.index)
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
values = [1] * 10 + [2] * 10
df = DataFrame({'a': values, 'b': values})
result = df.groupby('a').sample(n=None, frac=None)
expected = DataFrame({'a': [1, 2], 'b': [1, 2]}, index=result.index)
tm.assert_frame_equal(result, expected)
result = df.groupby('a')['b'].sample(n=None, frac=None)
expected = Series([1, 2], name='b', index=result.index)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_sample.py:106 | Complexity: Advanced | Last updated: 2026-06-02*