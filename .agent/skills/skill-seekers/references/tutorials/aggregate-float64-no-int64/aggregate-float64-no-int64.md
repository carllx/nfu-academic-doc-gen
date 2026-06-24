# How To: Aggregate Float64 No Int64

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test aggregate float64 no int64

## Prerequisites

**Required Modules:**
- `datetime`
- `functools`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.io.formats.printing`
- `pandas.tests.extension.decimal.array`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 2, 3, 4, 5], 'b': [1, 2, 2, 4, 5], 'c': [1, 2, 3, 4, 5]})
```

### Step 2: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': [1, 2.5, 4, 5]}, index=[1, 2, 4, 5])
```

### Step 3: Assign expected.index.name = 'b'

```python
expected.index.name = 'b'
```

### Step 4: Assign result = unknown.mean(...)

```python
result = df.groupby('b')[['a']].mean()
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': [1, 2.5, 4, 5], 'c': [1, 2.5, 4, 5]}, index=[1, 2, 4, 5])
```

### Step 7: Assign expected.index.name = 'b'

```python
expected.index.name = 'b'
```

### Step 8: Assign result = unknown.mean(...)

```python
result = df.groupby('b')[['a', 'c']].mean()
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'a': [1, 2, 3, 4, 5], 'b': [1, 2, 2, 4, 5], 'c': [1, 2, 3, 4, 5]})
expected = DataFrame({'a': [1, 2.5, 4, 5]}, index=[1, 2, 4, 5])
expected.index.name = 'b'
result = df.groupby('b')[['a']].mean()
tm.assert_frame_equal(result, expected)
expected = DataFrame({'a': [1, 2.5, 4, 5], 'c': [1, 2.5, 4, 5]}, index=[1, 2, 4, 5])
expected.index.name = 'b'
result = df.groupby('b')[['a', 'c']].mean()
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_other.py:153 | Complexity: Advanced | Last updated: 2026-06-02*