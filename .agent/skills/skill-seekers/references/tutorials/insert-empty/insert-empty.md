# How To: Insert Empty

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test insert empty

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = timedelta_range(...)

```python
idx = timedelta_range('1 Day', periods=3)
```

**Verification:**
```python
assert result.freq == 'D'
```

### Step 2: Assign td = value

```python
td = idx[0]
```

### Step 3: Assign result = unknown.insert(...)

```python
result = idx[:0].insert(0, td)
```

**Verification:**
```python
assert result.freq == 'D'
```

### Step 4: Assign result = unknown.insert(...)

```python
result = idx[:0].insert(1, td)
```

### Step 5: Assign result = unknown.insert(...)

```python
result = idx[:0].insert(-1, td)
```


## Complete Example

```python
# Workflow
idx = timedelta_range('1 Day', periods=3)
td = idx[0]
result = idx[:0].insert(0, td)
assert result.freq == 'D'
with pytest.raises(IndexError, match='loc must be an integer between'):
    result = idx[:0].insert(1, td)
with pytest.raises(IndexError, match='loc must be an integer between'):
    result = idx[:0].insert(-1, td)
```

## Next Steps


---

*Source: test_insert.py:132 | Complexity: Intermediate | Last updated: 2026-06-02*