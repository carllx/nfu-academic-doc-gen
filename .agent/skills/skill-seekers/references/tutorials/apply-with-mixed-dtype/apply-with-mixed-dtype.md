# How To: Apply With Mixed Dtype

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test apply with mixed dtype

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.groupby`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'foo1': np.random.default_rng(2).standard_normal(6), 'foo2': ['one', 'two', 'two', 'three', 'one', 'two']})
```

### Step 2: Assign result = value

```python
result = df.apply(lambda x: x, axis=1).dtypes
```

### Step 3: Assign expected = value

```python
expected = df.dtypes
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign df = DataFrame(...)

```python
df = DataFrame({'c1': [1, 2, 6, 6, 8]})
```

### Step 6: Assign unknown = value

```python
df['c2'] = df.c1 / 2.0
```

### Step 7: Assign result1 = value

```python
result1 = df.groupby('c2').mean().reset_index().c2
```

### Step 8: Assign result2 = value

```python
result2 = df.groupby('c2', as_index=False).mean().c2
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result1, result2)
```


## Complete Example

```python
# Workflow
df = DataFrame({'foo1': np.random.default_rng(2).standard_normal(6), 'foo2': ['one', 'two', 'two', 'three', 'one', 'two']})
result = df.apply(lambda x: x, axis=1).dtypes
expected = df.dtypes
tm.assert_series_equal(result, expected)
df = DataFrame({'c1': [1, 2, 6, 6, 8]})
df['c2'] = df.c1 / 2.0
result1 = df.groupby('c2').mean().reset_index().c2
result2 = df.groupby('c2', as_index=False).mean().c2
tm.assert_series_equal(result1, result2)
```

## Next Steps


---

*Source: test_apply.py:304 | Complexity: Advanced | Last updated: 2026-06-02*