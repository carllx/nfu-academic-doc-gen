# How To: First Last Nth Dtypes

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test first last nth dtypes

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'], 'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'], 'C': np.random.default_rng(2).standard_normal(8), 'D': np.array(np.random.default_rng(2).standard_normal(8), dtype='float32')})
```

### Step 2: Assign unknown = True

```python
df['E'] = True
```

### Step 3: Assign unknown = 1

```python
df['F'] = 1
```

### Step 4: Assign grouped = df.groupby(...)

```python
grouped = df.groupby('A')
```

### Step 5: Assign first = grouped.first(...)

```python
first = grouped.first()
```

### Step 6: Assign expected = value

```python
expected = df.loc[[1, 0], ['B', 'C', 'D', 'E', 'F']]
```

### Step 7: Assign expected.index = Index(...)

```python
expected.index = Index(['bar', 'foo'], name='A')
```

### Step 8: Assign expected = expected.sort_index(...)

```python
expected = expected.sort_index()
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(first, expected)
```

### Step 10: Assign last = grouped.last(...)

```python
last = grouped.last()
```

### Step 11: Assign expected = value

```python
expected = df.loc[[5, 7], ['B', 'C', 'D', 'E', 'F']]
```

### Step 12: Assign expected.index = Index(...)

```python
expected.index = Index(['bar', 'foo'], name='A')
```

### Step 13: Assign expected = expected.sort_index(...)

```python
expected = expected.sort_index()
```

### Step 14: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(last, expected)
```

### Step 15: Assign nth = grouped.nth(...)

```python
nth = grouped.nth(1)
```

### Step 16: Assign expected = value

```python
expected = df.iloc[[2, 3]]
```

### Step 17: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(nth, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'], 'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'], 'C': np.random.default_rng(2).standard_normal(8), 'D': np.array(np.random.default_rng(2).standard_normal(8), dtype='float32')})
df['E'] = True
df['F'] = 1
grouped = df.groupby('A')
first = grouped.first()
expected = df.loc[[1, 0], ['B', 'C', 'D', 'E', 'F']]
expected.index = Index(['bar', 'foo'], name='A')
expected = expected.sort_index()
tm.assert_frame_equal(first, expected)
last = grouped.last()
expected = df.loc[[5, 7], ['B', 'C', 'D', 'E', 'F']]
expected.index = Index(['bar', 'foo'], name='A')
expected = expected.sort_index()
tm.assert_frame_equal(last, expected)
nth = grouped.nth(1)
expected = df.iloc[[2, 3]]
tm.assert_frame_equal(nth, expected)
```

## Next Steps


---

*Source: test_nth.py:125 | Complexity: Advanced | Last updated: 2026-06-02*