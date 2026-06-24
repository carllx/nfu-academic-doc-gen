# How To: Multiindex Slice First Level

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test multiindex slice first level

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.indexing.common`


## Step-by-Step Guide

### Step 1: Assign freq = value

```python
freq = ['a', 'b', 'c', 'd']
```

### Step 2: Assign idx = MultiIndex.from_product(...)

```python
idx = MultiIndex.from_product([freq, range(500)])
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame(list(range(2000)), index=idx, columns=['Test'])
```

### Step 4: Assign df_slice = value

```python
df_slice = df.loc[pd.IndexSlice[:, 30:70], :]
```

### Step 5: Assign result = value

```python
result = df_slice.loc['a']
```

### Step 6: Assign expected = DataFrame(...)

```python
expected = DataFrame(list(range(30, 71)), columns=['Test'], index=range(30, 71))
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Assign result = value

```python
result = df_slice.loc['d']
```

### Step 9: Assign expected = DataFrame(...)

```python
expected = DataFrame(list(range(1530, 1571)), columns=['Test'], index=range(30, 71))
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
freq = ['a', 'b', 'c', 'd']
idx = MultiIndex.from_product([freq, range(500)])
df = DataFrame(list(range(2000)), index=idx, columns=['Test'])
df_slice = df.loc[pd.IndexSlice[:, 30:70], :]
result = df_slice.loc['a']
expected = DataFrame(list(range(30, 71)), columns=['Test'], index=range(30, 71))
tm.assert_frame_equal(result, expected)
result = df_slice.loc['d']
expected = DataFrame(list(range(1530, 1571)), columns=['Test'], index=range(30, 71))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_slice.py:720 | Complexity: Advanced | Last updated: 2026-06-02*