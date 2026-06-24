# How To: Frame Getitem Not Sorted2

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test frame getitem not sorted2

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: key
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'col1': ['b', 'd', 'b', 'a'], 'col2': [3, 1, 1, 2], 'data': ['one', 'two', 'three', 'four']})
```

**Verification:**
```python
assert not df2.index.is_monotonic_increasing
```

### Step 2: Assign df2 = df.set_index(...)

```python
df2 = df.set_index(['col1', 'col2'])
```

**Verification:**
```python
assert df2_original.index.equals(df2.index)
```

### Step 3: Assign df2_original = df2.copy(...)

```python
df2_original = df2.copy()
```

**Verification:**
```python
assert expected.index.is_monotonic_increasing
```

### Step 4: Assign df2.index = df2.index.set_levels(...)

```python
df2.index = df2.index.set_levels(['b', 'd', 'a'], level='col1')
```

**Verification:**
```python
assert result.index.is_monotonic_increasing
```

### Step 5: Assign df2.index = df2.index.set_codes(...)

```python
df2.index = df2.index.set_codes([0, 1, 0, 2], level='col1')
```

**Verification:**
```python
assert not df2.index.is_monotonic_increasing
```

### Step 6: Assign expected = df2.sort_index(...)

```python
expected = df2.sort_index(key=key)
```

**Verification:**
```python
assert expected.index.is_monotonic_increasing
```

### Step 7: Assign result = df2.sort_index(...)

```python
result = df2.sort_index(level=0, key=key)
```

**Verification:**
```python
assert result.index.is_monotonic_increasing
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: key

# Workflow
df = DataFrame({'col1': ['b', 'd', 'b', 'a'], 'col2': [3, 1, 1, 2], 'data': ['one', 'two', 'three', 'four']})
df2 = df.set_index(['col1', 'col2'])
df2_original = df2.copy()
df2.index = df2.index.set_levels(['b', 'd', 'a'], level='col1')
df2.index = df2.index.set_codes([0, 1, 0, 2], level='col1')
assert not df2.index.is_monotonic_increasing
assert df2_original.index.equals(df2.index)
expected = df2.sort_index(key=key)
assert expected.index.is_monotonic_increasing
result = df2.sort_index(level=0, key=key)
assert result.index.is_monotonic_increasing
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_sorted.py:38 | Complexity: Advanced | Last updated: 2026-06-02*