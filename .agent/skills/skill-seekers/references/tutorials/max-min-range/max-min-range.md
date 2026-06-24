# How To: Max Min Range

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test max min range

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `decimal`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`
- `pandas.core.arrays.string_arrow`

**Setup Required:**
```python
# Fixtures: start, stop, step
```

## Step-by-Step Guide

### Step 1: Assign idx = RangeIndex(...)

```python
idx = RangeIndex(start, stop, step)
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign expected = idx._values.max(...)

```python
expected = idx._values.max()
```

**Verification:**
```python
assert result2 == expected
```

### Step 3: Assign result = idx.max(...)

```python
result = idx.max()
```

**Verification:**
```python
assert result == expected
```

### Step 4: Assign result2 = idx.max(...)

```python
result2 = idx.max(skipna=False)
```

**Verification:**
```python
assert result2 == expected
```

### Step 5: Assign expected = idx._values.min(...)

```python
expected = idx._values.min()
```

**Verification:**
```python
assert isna(idx.max())
```

### Step 6: Assign result = idx.min(...)

```python
result = idx.min()
```

**Verification:**
```python
assert isna(idx.min())
```

### Step 7: Assign result2 = idx.min(...)

```python
result2 = idx.min(skipna=False)
```

**Verification:**
```python
assert result2 == expected
```

### Step 8: Assign idx = RangeIndex(...)

```python
idx = RangeIndex(start, stop, -step)
```

**Verification:**
```python
assert isna(idx.max())
```


## Complete Example

```python
# Setup
# Fixtures: start, stop, step

# Workflow
idx = RangeIndex(start, stop, step)
expected = idx._values.max()
result = idx.max()
assert result == expected
result2 = idx.max(skipna=False)
assert result2 == expected
expected = idx._values.min()
result = idx.min()
assert result == expected
result2 = idx.min(skipna=False)
assert result2 == expected
idx = RangeIndex(start, stop, -step)
assert isna(idx.max())
assert isna(idx.min())
```

## Next Steps


---

*Source: test_reductions.py:261 | Complexity: Advanced | Last updated: 2026-06-02*