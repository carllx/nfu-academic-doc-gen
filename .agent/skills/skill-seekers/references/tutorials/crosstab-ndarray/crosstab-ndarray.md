# How To: Crosstab Ndarray

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test crosstab ndarray

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: box
```

## Step-by-Step Guide

### Step 1: Assign a = box(...)

```python
a = box(np.random.default_rng(2).integers(0, 5, size=100))
```

### Step 2: Assign b = box(...)

```python
b = box(np.random.default_rng(2).integers(0, 3, size=100))
```

### Step 3: Assign c = box(...)

```python
c = box(np.random.default_rng(2).integers(0, 10, size=100))
```

### Step 4: Assign df = DataFrame(...)

```python
df = DataFrame({'a': a, 'b': b, 'c': c})
```

### Step 5: Assign result = crosstab(...)

```python
result = crosstab(a, [b, c], rownames=['a'], colnames=('b', 'c'))
```

### Step 6: Assign expected = crosstab(...)

```python
expected = crosstab(df['a'], [df['b'], df['c']])
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Assign result = crosstab(...)

```python
result = crosstab([b, c], a, colnames=['a'], rownames=('b', 'c'))
```

### Step 9: Assign expected = crosstab(...)

```python
expected = crosstab([df['b'], df['c']], df['a'])
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 11: Assign result = crosstab(...)

```python
result = crosstab(a, c)
```

### Step 12: Assign expected = crosstab(...)

```python
expected = crosstab(df['a'], df['c'])
```

### Step 13: Assign expected.index.names = value

```python
expected.index.names = ['row_0']
```

### Step 14: Assign expected.columns.names = value

```python
expected.columns.names = ['col_0']
```

### Step 15: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: box

# Workflow
a = box(np.random.default_rng(2).integers(0, 5, size=100))
b = box(np.random.default_rng(2).integers(0, 3, size=100))
c = box(np.random.default_rng(2).integers(0, 10, size=100))
df = DataFrame({'a': a, 'b': b, 'c': c})
result = crosstab(a, [b, c], rownames=['a'], colnames=('b', 'c'))
expected = crosstab(df['a'], [df['b'], df['c']])
tm.assert_frame_equal(result, expected)
result = crosstab([b, c], a, colnames=['a'], rownames=('b', 'c'))
expected = crosstab([df['b'], df['c']], df['a'])
tm.assert_frame_equal(result, expected)
result = crosstab(a, c)
expected = crosstab(df['a'], df['c'])
expected.index.names = ['row_0']
expected.columns.names = ['col_0']
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_crosstab.py:87 | Complexity: Advanced | Last updated: 2026-06-02*