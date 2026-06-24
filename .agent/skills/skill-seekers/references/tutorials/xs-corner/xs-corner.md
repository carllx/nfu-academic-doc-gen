# How To: Xs Corner

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test xs corner

## Prerequisites

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas._testing`
- `pandas.tseries.offsets`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(index=[0], columns=Index([], dtype='str'))
```

### Step 2: Assign unknown = 1.0

```python
df['A'] = 1.0
```

### Step 3: Assign unknown = 'foo'

```python
df['B'] = 'foo'
```

### Step 4: Assign unknown = 2.0

```python
df['C'] = 2.0
```

### Step 5: Assign unknown = 'bar'

```python
df['D'] = 'bar'
```

### Step 6: Assign unknown = 3.0

```python
df['E'] = 3.0
```

### Step 7: Assign xs = df.xs(...)

```python
xs = df.xs(0)
```

### Step 8: Assign exp = Series(...)

```python
exp = Series([1.0, 'foo', 2.0, 'bar', 3.0], index=list('ABCDE'), name=0)
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(xs, exp)
```

### Step 10: Assign df = DataFrame(...)

```python
df = DataFrame(index=['a', 'b', 'c'])
```

### Step 11: Assign result = df.xs(...)

```python
result = df.xs('a')
```

### Step 12: Assign expected = Series(...)

```python
expected = Series([], name='a', dtype=np.float64)
```

### Step 13: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame(index=[0], columns=Index([], dtype='str'))
df['A'] = 1.0
df['B'] = 'foo'
df['C'] = 2.0
df['D'] = 'bar'
df['E'] = 3.0
xs = df.xs(0)
exp = Series([1.0, 'foo', 2.0, 'bar', 3.0], index=list('ABCDE'), name=0)
tm.assert_series_equal(xs, exp)
df = DataFrame(index=['a', 'b', 'c'])
result = df.xs('a')
expected = Series([], name='a', dtype=np.float64)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_xs.py:80 | Complexity: Advanced | Last updated: 2026-06-02*