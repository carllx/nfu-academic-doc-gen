# How To: Indexer Caching

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: mock, workflow, integration

## Overview

Workflow: test indexer caching

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: monkeypatch
```

## Step-by-Step Guide

### Step 1: Assign size_cutoff = 20

```python
size_cutoff = 20
```

### Step 2: Assign expected = Series(...)

```python
expected = Series(np.ones(size_cutoff), index=index)
```

### Step 3: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s, expected)
```

### Step 4: Call monkeypatch.setattr()

```python
monkeypatch.setattr(libindex, '_SIZE_CUTOFF', size_cutoff)
```

### Step 5: Assign index = MultiIndex.from_arrays(...)

```python
index = MultiIndex.from_arrays([np.arange(size_cutoff), np.arange(size_cutoff)])
```

### Step 6: Assign s = Series(...)

```python
s = Series(np.zeros(size_cutoff), index=index)
```

### Step 7: Assign unknown = 1

```python
s[s == 0] = 1
```


## Complete Example

```python
# Setup
# Fixtures: monkeypatch

# Workflow
size_cutoff = 20
with monkeypatch.context():
    monkeypatch.setattr(libindex, '_SIZE_CUTOFF', size_cutoff)
    index = MultiIndex.from_arrays([np.arange(size_cutoff), np.arange(size_cutoff)])
    s = Series(np.zeros(size_cutoff), index=index)
    s[s == 0] = 1
expected = Series(np.ones(size_cutoff), index=index)
tm.assert_series_equal(s, expected)
```

## Next Steps


---

*Source: test_chaining_and_caching.py:75 | Complexity: Intermediate | Last updated: 2026-06-02*