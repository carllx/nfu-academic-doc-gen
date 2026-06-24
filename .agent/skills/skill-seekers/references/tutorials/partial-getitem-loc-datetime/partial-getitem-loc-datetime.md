# How To: Partial Getitem Loc Datetime

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test partial getitem loc datetime

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: indexer, exp_idx, exp_values
```

## Step-by-Step Guide

### Step 1: Assign date_idx = date_range(...)

```python
date_idx = date_range('2019', periods=2, freq='MS')
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(list(range(4)), index=MultiIndex.from_product([date_idx, [0, 1]], names=['x', 'y']))
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame(exp_values, index=MultiIndex.from_product([exp_idx, [0, 1]], names=['x', 'y']))
```

### Step 4: Assign result = value

```python
result = df[indexer]
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign result = value

```python
result = df.loc[indexer]
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Assign result = value

```python
result = df.loc(axis=0)[indexer]
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 10: Assign result = value

```python
result = df.loc[indexer, :]
```

### Step 11: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 12: Assign df2 = df.swaplevel.sort_index(...)

```python
df2 = df.swaplevel(0, 1).sort_index()
```

### Step 13: Assign expected = expected.swaplevel.sort_index(...)

```python
expected = expected.swaplevel(0, 1).sort_index()
```

### Step 14: Assign result = value

```python
result = df2.loc[:, indexer, :]
```

### Step 15: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: indexer, exp_idx, exp_values

# Workflow
date_idx = date_range('2019', periods=2, freq='MS')
df = DataFrame(list(range(4)), index=MultiIndex.from_product([date_idx, [0, 1]], names=['x', 'y']))
expected = DataFrame(exp_values, index=MultiIndex.from_product([exp_idx, [0, 1]], names=['x', 'y']))
result = df[indexer]
tm.assert_frame_equal(result, expected)
result = df.loc[indexer]
tm.assert_frame_equal(result, expected)
result = df.loc(axis=0)[indexer]
tm.assert_frame_equal(result, expected)
result = df.loc[indexer, :]
tm.assert_frame_equal(result, expected)
df2 = df.swaplevel(0, 1).sort_index()
expected = expected.swaplevel(0, 1).sort_index()
result = df2.loc[:, indexer, :]
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_partial.py:230 | Complexity: Advanced | Last updated: 2026-06-02*