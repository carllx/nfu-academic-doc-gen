# How To: Concat Multiindex Datetime Object Index

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concat multiindex datetime object index

## Prerequisites

**Required Modules:**
- `datetime`
- `datetime`
- `dateutil`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = Index(...)

```python
idx = Index([dt.date(2013, 1, 1), dt.date(2014, 1, 1), dt.date(2015, 1, 1)], dtype='object')
```

**Verification:**
```python
assert mi.levels[1].dtype == object
```

### Step 2: Assign s = Series(...)

```python
s = Series(['a', 'b'], index=MultiIndex.from_arrays([[1, 2], idx[:-1]], names=['first', 'second']))
```

### Step 3: Assign s2 = Series(...)

```python
s2 = Series(['a', 'b'], index=MultiIndex.from_arrays([[1, 2], idx[::2]], names=['first', 'second']))
```

### Step 4: Assign mi = MultiIndex.from_arrays(...)

```python
mi = MultiIndex.from_arrays([[1, 2, 2], idx], names=['first', 'second'])
```

**Verification:**
```python
assert mi.levels[1].dtype == object
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame([['a', 'a'], ['b', np.nan], [np.nan, 'b']], index=mi)
```

### Step 6: Assign result = concat(...)

```python
result = concat([s, s2], axis=1)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
idx = Index([dt.date(2013, 1, 1), dt.date(2014, 1, 1), dt.date(2015, 1, 1)], dtype='object')
s = Series(['a', 'b'], index=MultiIndex.from_arrays([[1, 2], idx[:-1]], names=['first', 'second']))
s2 = Series(['a', 'b'], index=MultiIndex.from_arrays([[1, 2], idx[::2]], names=['first', 'second']))
mi = MultiIndex.from_arrays([[1, 2, 2], idx], names=['first', 'second'])
assert mi.levels[1].dtype == object
expected = DataFrame([['a', 'a'], ['b', np.nan], [np.nan, 'b']], index=mi)
result = concat([s, s2], axis=1)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_datetimes.py:123 | Complexity: Intermediate | Last updated: 2026-06-02*