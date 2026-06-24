# How To: Crosstab Pass Values

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test crosstab pass values

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign a = np.random.default_rng.integers(...)

```python
a = np.random.default_rng(2).integers(0, 7, size=100)
```

### Step 2: Assign b = np.random.default_rng.integers(...)

```python
b = np.random.default_rng(2).integers(0, 3, size=100)
```

### Step 3: Assign c = np.random.default_rng.integers(...)

```python
c = np.random.default_rng(2).integers(0, 5, size=100)
```

### Step 4: Assign values = np.random.default_rng.standard_normal(...)

```python
values = np.random.default_rng(2).standard_normal(100)
```

### Step 5: Assign table = crosstab(...)

```python
table = crosstab([a, b], c, values, aggfunc='sum', rownames=['foo', 'bar'], colnames=['baz'])
```

### Step 6: Assign df = DataFrame(...)

```python
df = DataFrame({'foo': a, 'bar': b, 'baz': c, 'values': values})
```

### Step 7: Assign expected = df.pivot_table(...)

```python
expected = df.pivot_table('values', index=['foo', 'bar'], columns='baz', aggfunc='sum')
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(table, expected)
```


## Complete Example

```python
# Workflow
a = np.random.default_rng(2).integers(0, 7, size=100)
b = np.random.default_rng(2).integers(0, 3, size=100)
c = np.random.default_rng(2).integers(0, 5, size=100)
values = np.random.default_rng(2).standard_normal(100)
table = crosstab([a, b], c, values, aggfunc='sum', rownames=['foo', 'bar'], colnames=['baz'])
df = DataFrame({'foo': a, 'bar': b, 'baz': c, 'values': values})
expected = df.pivot_table('values', index=['foo', 'bar'], columns='baz', aggfunc='sum')
tm.assert_frame_equal(table, expected)
```

## Next Steps


---

*Source: test_crosstab.py:208 | Complexity: Advanced | Last updated: 2026-06-02*