# How To: Length

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test length

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `itertools`
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.common`

**Setup Required:**
```python
# Fixtures: closed, breaks
```

## Step-by-Step Guide

### Step 1: Assign index = IntervalIndex.from_breaks(...)

```python
index = IntervalIndex.from_breaks(breaks, closed=closed)
```

### Step 2: Assign result = value

```python
result = index.length
```

### Step 3: Assign expected = Index(...)

```python
expected = Index((iv.length for iv in index))
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 5: Assign index = index.insert(...)

```python
index = index.insert(1, np.nan)
```

### Step 6: Assign result = value

```python
result = index.length
```

### Step 7: Assign expected = Index(...)

```python
expected = Index((iv.length if notna(iv) else iv for iv in index))
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: closed, breaks

# Workflow
index = IntervalIndex.from_breaks(breaks, closed=closed)
result = index.length
expected = Index((iv.length for iv in index))
tm.assert_index_equal(result, expected)
index = index.insert(1, np.nan)
result = index.length
expected = Index((iv.length if notna(iv) else iv for iv in index))
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_interval.py:97 | Complexity: Advanced | Last updated: 2026-06-02*