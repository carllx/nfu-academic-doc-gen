# How To: To Records With Categorical

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to records with categorical

## Prerequisites

**Required Modules:**
- `collections`
- `email`
- `email.parser`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': list('abc')}, dtype='category')
```

### Step 2: Assign expected = Series(...)

```python
expected = Series(list('abc'), dtype='category', name='A')
```

### Step 3: Call tm.assert_series_equal()

```python
tm.assert_series_equal(df['A'], expected)
```

### Step 4: Assign df = DataFrame(...)

```python
df = DataFrame(list('abc'), dtype='category')
```

### Step 5: Assign expected = Series(...)

```python
expected = Series(list('abc'), dtype='category', name=0)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(df[0], expected)
```

### Step 7: Assign result = df.to_records(...)

```python
result = df.to_records()
```

### Step 8: Assign expected = np.rec.array(...)

```python
expected = np.rec.array([(0, 'a'), (1, 'b'), (2, 'c')], dtype=[('index', '=i8'), ('0', 'O')])
```

### Step 9: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'A': list('abc')}, dtype='category')
expected = Series(list('abc'), dtype='category', name='A')
tm.assert_series_equal(df['A'], expected)
df = DataFrame(list('abc'), dtype='category')
expected = Series(list('abc'), dtype='category', name=0)
tm.assert_series_equal(df[0], expected)
result = df.to_records()
expected = np.rec.array([(0, 'a'), (1, 'b'), (2, 'c')], dtype=[('index', '=i8'), ('0', 'O')])
tm.assert_almost_equal(result, expected)
```

## Next Steps


---

*Source: test_to_records.py:165 | Complexity: Advanced | Last updated: 2026-06-02*