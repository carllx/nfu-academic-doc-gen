# How To: Rename Multiindex With Duplicates

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test rename multiindex with duplicates

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs.index`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.boolean`


## Step-by-Step Guide

### Step 1: Assign mi = MultiIndex.from_tuples(...)

```python
mi = MultiIndex.from_tuples([('A', 'cat'), ('B', 'cat'), ('B', 'cat')])
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(index=mi)
```

### Step 3: Assign df = df.rename(...)

```python
df = df.rename(index={'A': 'Apple'}, level=0)
```

### Step 4: Assign mi2 = MultiIndex.from_tuples(...)

```python
mi2 = MultiIndex.from_tuples([('Apple', 'cat'), ('B', 'cat'), ('B', 'cat')])
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame(index=mi2)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```


## Complete Example

```python
# Workflow
mi = MultiIndex.from_tuples([('A', 'cat'), ('B', 'cat'), ('B', 'cat')])
df = DataFrame(index=mi)
df = df.rename(index={'A': 'Apple'}, level=0)
mi2 = MultiIndex.from_tuples([('Apple', 'cat'), ('B', 'cat'), ('B', 'cat')])
expected = DataFrame(index=mi2)
tm.assert_frame_equal(df, expected)
```

## Next Steps


---

*Source: test_multiindex.py:145 | Complexity: Intermediate | Last updated: 2026-06-02*