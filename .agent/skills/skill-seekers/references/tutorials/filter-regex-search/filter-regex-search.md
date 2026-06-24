# How To: Filter Regex Search

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test filter regex search

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: float_frame
```

## Step-by-Step Guide

### Step 1: Assign fcopy = float_frame.copy(...)

```python
fcopy = float_frame.copy()
```

**Verification:**
```python
assert len(filtered.columns) == 2
```

### Step 2: Assign unknown = 1

```python
fcopy['AA'] = 1
```

**Verification:**
```python
assert 'AA' in filtered
```

### Step 3: Assign filtered = fcopy.filter(...)

```python
filtered = fcopy.filter(regex='[A]+')
```

**Verification:**
```python
assert len(filtered.columns) == 2
```

### Step 4: Assign df = DataFrame(...)

```python
df = DataFrame({'aBBa': [1, 2], 'BBaBB': [1, 2], 'aCCa': [1, 2], 'aCCaBB': [1, 2]})
```

### Step 5: Assign result = df.filter(...)

```python
result = df.filter(regex='BB')
```

### Step 6: Assign exp = value

```python
exp = df[[x for x in df.columns if 'BB' in x]]
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, exp)
```


## Complete Example

```python
# Setup
# Fixtures: float_frame

# Workflow
fcopy = float_frame.copy()
fcopy['AA'] = 1
filtered = fcopy.filter(regex='[A]+')
assert len(filtered.columns) == 2
assert 'AA' in filtered
df = DataFrame({'aBBa': [1, 2], 'BBaBB': [1, 2], 'aCCa': [1, 2], 'aCCaBB': [1, 2]})
result = df.filter(regex='BB')
exp = df[[x for x in df.columns if 'BB' in x]]
tm.assert_frame_equal(result, exp)
```

## Next Steps


---

*Source: test_filter.py:82 | Complexity: Intermediate | Last updated: 2026-06-02*