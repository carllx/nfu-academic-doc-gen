# How To: Ngroup Distinct

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test ngroup distinct

## Prerequisites

**Required Modules:**
- `itertools`
- `string`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': list('abcde')})
```

### Step 2: Assign g = df.groupby(...)

```python
g = df.groupby('A')
```

### Step 3: Assign sg = value

```python
sg = g.A
```

### Step 4: Assign expected = Series(...)

```python
expected = Series(range(5), dtype='int64')
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expected, g.ngroup())
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expected, sg.ngroup())
```


## Complete Example

```python
# Workflow
df = DataFrame({'A': list('abcde')})
g = df.groupby('A')
sg = g.A
expected = Series(range(5), dtype='int64')
tm.assert_series_equal(expected, g.ngroup())
tm.assert_series_equal(expected, sg.ngroup())
```

## Next Steps


---

*Source: test_counting.py:86 | Complexity: Intermediate | Last updated: 2026-06-02*