# How To: Relabel No Duplicated Method

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test relabel no duplicated method

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
result = df['A'].agg(foo='sum')
```

### Step 3: Assign expected = unknown.agg(...)

```python
expected = df['A'].agg({'foo': 'sum'})
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign result = unknown.agg(...)

```python
result = df['B'].agg(foo='min', bar='max')
```

### Step 6: Assign expected = unknown.agg(...)

```python
expected = df['B'].agg({'foo': 'min', 'bar': 'max'})
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 8: Assign msg = 'using Series.[sum|min|max]'

```python
msg = 'using Series.[sum|min|max]'
```

### Step 9: Assign msg = 'using Series.[sum|min|max]'

```python
msg = 'using Series.[sum|min|max]'
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 11: Assign result = unknown.agg(...)

```python
result = df['B'].agg(foo=sum, bar=min, cat='max')
```

### Step 12: Assign expected = unknown.agg(...)

```python
expected = df['B'].agg({'foo': sum, 'bar': min, 'cat': 'max'})
```


## Complete Example

```python
# Workflow
df = pd.DataFrame({'A': [1, 2, 1, 2], 'B': [1, 2, 3, 4]})
result = df['A'].agg(foo='sum')
expected = df['A'].agg({'foo': 'sum'})
tm.assert_series_equal(result, expected)
result = df['B'].agg(foo='min', bar='max')
expected = df['B'].agg({'foo': 'min', 'bar': 'max'})
tm.assert_series_equal(result, expected)
msg = 'using Series.[sum|min|max]'
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = df['B'].agg(foo=sum, bar=min, cat='max')
msg = 'using Series.[sum|min|max]'
with tm.assert_produces_warning(FutureWarning, match=msg):
    expected = df['B'].agg({'foo': sum, 'bar': min, 'cat': 'max'})
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_series_apply_relabeling.py:5 | Complexity: Advanced | Last updated: 2026-06-02*