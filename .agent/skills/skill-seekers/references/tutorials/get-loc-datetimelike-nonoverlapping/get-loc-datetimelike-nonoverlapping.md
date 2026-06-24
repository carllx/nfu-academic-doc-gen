# How To: Get Loc Datetimelike Nonoverlapping

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test get loc datetimelike nonoverlapping

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: breaks
```

## Step-by-Step Guide

### Step 1: Assign index = IntervalIndex.from_breaks(...)

```python
index = IntervalIndex.from_breaks(breaks)
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign value = value

```python
value = index[0].mid
```

**Verification:**
```python
assert result == expected
```

### Step 3: Assign result = index.get_loc(...)

```python
result = index.get_loc(value)
```

### Step 4: Assign expected = 0

```python
expected = 0
```

**Verification:**
```python
assert result == expected
```

### Step 5: Assign interval = Interval(...)

```python
interval = Interval(index[0].left, index[0].right)
```

### Step 6: Assign result = index.get_loc(...)

```python
result = index.get_loc(interval)
```

### Step 7: Assign expected = 0

```python
expected = 0
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Setup
# Fixtures: breaks

# Workflow
index = IntervalIndex.from_breaks(breaks)
value = index[0].mid
result = index.get_loc(value)
expected = 0
assert result == expected
interval = Interval(index[0].left, index[0].right)
result = index.get_loc(interval)
expected = 0
assert result == expected
```

## Next Steps


---

*Source: test_indexing.py:170 | Complexity: Intermediate | Last updated: 2026-06-02*