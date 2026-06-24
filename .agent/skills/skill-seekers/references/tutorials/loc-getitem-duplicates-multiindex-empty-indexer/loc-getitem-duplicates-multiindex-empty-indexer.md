# How To: Loc Getitem Duplicates Multiindex Empty Indexer

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test loc getitem duplicates multiindex empty indexer

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: columns_indexer
```

## Step-by-Step Guide

### Step 1: Assign multi_index = MultiIndex.from_product(...)

```python
multi_index = MultiIndex.from_product((['foo', 'bar', 'baz'], ['alpha', 'beta']))
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((5, 6)), index=range(5), columns=multi_index)
```

### Step 3: Assign df = df.sort_index(...)

```python
df = df.sort_index(level=0, axis=1)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame(index=range(5), columns=multi_index.reindex([])[0])
```

### Step 5: Assign result = value

```python
result = df.loc[:, columns_indexer]
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: columns_indexer

# Workflow
multi_index = MultiIndex.from_product((['foo', 'bar', 'baz'], ['alpha', 'beta']))
df = DataFrame(np.random.default_rng(2).standard_normal((5, 6)), index=range(5), columns=multi_index)
df = df.sort_index(level=0, axis=1)
expected = DataFrame(index=range(5), columns=multi_index.reindex([])[0])
result = df.loc[:, columns_indexer]
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_loc.py:482 | Complexity: Intermediate | Last updated: 2026-06-02*