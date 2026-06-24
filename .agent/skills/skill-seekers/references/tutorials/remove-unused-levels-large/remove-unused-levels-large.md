# How To: Remove Unused Levels Large

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test remove unused levels large

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas._testing`
- `pandas.core.indexes.frozen`

**Setup Required:**
```python
# Fixtures: first_type, second_type
```

## Step-by-Step Guide

### Step 1: Assign rng = np.random.default_rng(...)

```python
rng = np.random.default_rng(10)
```

**Verification:**
```python
assert len(result.levels[0]) < len(df.index.levels[0])
```

### Step 2: Assign size = value

```python
size = 1 << 16
```

**Verification:**
```python
assert len(result.levels[1]) < len(df.index.levels[1])
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame({'first': rng.integers(0, 1 << 13, size).astype(first_type), 'second': rng.integers(0, 1 << 10, size).astype(second_type), 'third': rng.random(size)})
```

**Verification:**
```python
assert result.equals(df.index)
```

### Step 4: Assign df = df.groupby.sum(...)

```python
df = df.groupby(['first', 'second']).sum()
```

### Step 5: Assign df = value

```python
df = df[df.third < 0.1]
```

### Step 6: Assign result = df.index.remove_unused_levels(...)

```python
result = df.index.remove_unused_levels()
```

**Verification:**
```python
assert len(result.levels[0]) < len(df.index.levels[0])
```

### Step 7: Assign expected = value

```python
expected = df.reset_index().set_index(['first', 'second']).index
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: first_type, second_type

# Workflow
rng = np.random.default_rng(10)
size = 1 << 16
df = DataFrame({'first': rng.integers(0, 1 << 13, size).astype(first_type), 'second': rng.integers(0, 1 << 10, size).astype(second_type), 'third': rng.random(size)})
df = df.groupby(['first', 'second']).sum()
df = df[df.third < 0.1]
result = df.index.remove_unused_levels()
assert len(result.levels[0]) < len(df.index.levels[0])
assert len(result.levels[1]) < len(df.index.levels[1])
assert result.equals(df.index)
expected = df.reset_index().set_index(['first', 'second']).index
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_sorting.py:238 | Complexity: Advanced | Last updated: 2026-06-02*