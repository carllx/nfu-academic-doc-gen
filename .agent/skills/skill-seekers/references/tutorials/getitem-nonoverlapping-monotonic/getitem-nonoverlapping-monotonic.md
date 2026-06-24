# How To: Getitem Nonoverlapping Monotonic

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test getitem nonoverlapping monotonic

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: direction, closed, indexer_sl
```

## Step-by-Step Guide

### Step 1: Assign tpls = value

```python
tpls = [(0, 1), (2, 3), (4, 5)]
```

**Verification:**
```python
assert indexer_sl(ser)[key] == expected
```

### Step 2: Assign idx = IntervalIndex.from_tuples(...)

```python
idx = IntervalIndex.from_tuples(tpls, closed=closed)
```

**Verification:**
```python
assert indexer_sl(ser)[key] == expected
```

### Step 3: Assign ser = Series(...)

```python
ser = Series(list('abc'), idx)
```

**Verification:**
```python
assert indexer_sl(ser)[key] == expected
```

### Step 4: Assign tpls = value

```python
tpls = tpls[::-1]
```

**Verification:**
```python
assert indexer_sl(ser)[key] == expected
```

### Step 5: indexer_sl(ser)[key]

```python
indexer_sl(ser)[key]
```

### Step 6: indexer_sl(ser)[key]

```python
indexer_sl(ser)[key]
```


## Complete Example

```python
# Setup
# Fixtures: direction, closed, indexer_sl

# Workflow
tpls = [(0, 1), (2, 3), (4, 5)]
if direction == 'decreasing':
    tpls = tpls[::-1]
idx = IntervalIndex.from_tuples(tpls, closed=closed)
ser = Series(list('abc'), idx)
for key, expected in zip(idx.left, ser):
    if idx.closed_left:
        assert indexer_sl(ser)[key] == expected
    else:
        with pytest.raises(KeyError, match=str(key)):
            indexer_sl(ser)[key]
for key, expected in zip(idx.right, ser):
    if idx.closed_right:
        assert indexer_sl(ser)[key] == expected
    else:
        with pytest.raises(KeyError, match=str(key)):
            indexer_sl(ser)[key]
for key, expected in zip(idx.mid, ser):
    assert indexer_sl(ser)[key] == expected
```

## Next Steps


---

*Source: test_interval.py:39 | Complexity: Intermediate | Last updated: 2026-06-02*