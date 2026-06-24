# How To: Loc Getitem Duplicates Multiindex Missing Indexers

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test loc getitem duplicates multiindex missing indexers

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
# Fixtures: indexer, pos
```

## Step-by-Step Guide

### Step 1: Assign idx = MultiIndex.from_product(...)

```python
idx = MultiIndex.from_product([['A', 'B', 'C'], ['foo', 'bar', 'baz']], names=['one', 'two'])
```

### Step 2: Assign ser = Series.sort_index(...)

```python
ser = Series(np.arange(9, dtype='int64'), index=idx).sort_index()
```

### Step 3: Assign expected = value

```python
expected = ser.iloc[pos]
```

### Step 4: ser.loc[indexer]

```python
ser.loc[indexer]
```

### Step 5: Assign result = value

```python
result = ser.loc[indexer]
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 7: ser.loc[indexer]

```python
ser.loc[indexer]
```


## Complete Example

```python
# Setup
# Fixtures: indexer, pos

# Workflow
idx = MultiIndex.from_product([['A', 'B', 'C'], ['foo', 'bar', 'baz']], names=['one', 'two'])
ser = Series(np.arange(9, dtype='int64'), index=idx).sort_index()
expected = ser.iloc[pos]
if expected.size == 0 and indexer != []:
    with pytest.raises(KeyError, match=str(indexer)):
        ser.loc[indexer]
elif indexer == (slice(None), ['foo', 'bah']):
    with pytest.raises(KeyError, match="'bah'"):
        ser.loc[indexer]
else:
    result = ser.loc[indexer]
    tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_loc.py:460 | Complexity: Intermediate | Last updated: 2026-06-02*