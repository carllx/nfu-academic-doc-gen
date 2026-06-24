# How To: Slice Locs Partial

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test slice locs partial

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: idx
```

## Step-by-Step Guide

### Step 1: Assign unknown = idx.sortlevel(...)

```python
sorted_idx, _ = idx.sortlevel(0)
```

**Verification:**
```python
assert result == (1, 5)
```

### Step 2: Assign result = sorted_idx.slice_locs(...)

```python
result = sorted_idx.slice_locs(('foo', 'two'), ('qux', 'one'))
```

**Verification:**
```python
assert result == (0, 5)
```

### Step 3: Assign result = sorted_idx.slice_locs(...)

```python
result = sorted_idx.slice_locs(None, ('qux', 'one'))
```

**Verification:**
```python
assert result == (1, len(sorted_idx))
```

### Step 4: Assign result = sorted_idx.slice_locs(...)

```python
result = sorted_idx.slice_locs(('foo', 'two'), None)
```

**Verification:**
```python
assert result == (2, 4)
```

### Step 5: Assign result = sorted_idx.slice_locs(...)

```python
result = sorted_idx.slice_locs('bar', 'baz')
```

**Verification:**
```python
assert result == (2, 4)
```


## Complete Example

```python
# Setup
# Fixtures: idx

# Workflow
sorted_idx, _ = idx.sortlevel(0)
result = sorted_idx.slice_locs(('foo', 'two'), ('qux', 'one'))
assert result == (1, 5)
result = sorted_idx.slice_locs(None, ('qux', 'one'))
assert result == (0, 5)
result = sorted_idx.slice_locs(('foo', 'two'), None)
assert result == (1, len(sorted_idx))
result = sorted_idx.slice_locs('bar', 'baz')
assert result == (2, 4)
```

## Next Steps


---

*Source: test_indexing.py:25 | Complexity: Intermediate | Last updated: 2026-06-02*