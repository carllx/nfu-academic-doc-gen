# How To: Set Levels

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test set levels

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: idx
```

## Step-by-Step Guide

### Step 1: Assign levels = value

```python
levels = idx.levels
```

**Verification:**
```python
assert_matching(ind2.levels, new_levels)
```

### Step 2: Assign new_levels = value

```python
new_levels = [[lev + 'a' for lev in level] for level in levels]
```

**Verification:**
```python
assert_matching(idx.levels, levels)
```

### Step 3: Assign ind2 = idx.set_levels(...)

```python
ind2 = idx.set_levels(new_levels)
```

**Verification:**
```python
assert_matching(ind2.levels, [new_levels[0], levels[1]])
```

### Step 4: Call assert_matching()

```python
assert_matching(ind2.levels, new_levels)
```

**Verification:**
```python
assert_matching(idx.levels, levels)
```

### Step 5: Call assert_matching()

```python
assert_matching(idx.levels, levels)
```

**Verification:**
```python
assert_matching(ind2.levels, [levels[0], new_levels[1]])
```

### Step 6: Assign ind2 = idx.set_levels(...)

```python
ind2 = idx.set_levels(new_levels[0], level=0)
```

**Verification:**
```python
assert_matching(idx.levels, levels)
```

### Step 7: Call assert_matching()

```python
assert_matching(ind2.levels, [new_levels[0], levels[1]])
```

**Verification:**
```python
assert_matching(ind2.levels, new_levels)
```

### Step 8: Call assert_matching()

```python
assert_matching(idx.levels, levels)
```

**Verification:**
```python
assert_matching(idx.levels, levels)
```

### Step 9: Assign ind2 = idx.set_levels(...)

```python
ind2 = idx.set_levels(new_levels[1], level=1)
```

**Verification:**
```python
assert_matching(idx.levels, original_index.levels, check_dtype=True)
```

### Step 10: Call assert_matching()

```python
assert_matching(ind2.levels, [levels[0], new_levels[1]])
```

**Verification:**
```python
assert_matching(idx.codes, original_index.codes, check_dtype=True)
```

### Step 11: Call assert_matching()

```python
assert_matching(idx.levels, levels)
```

**Verification:**
```python
assert_matching(idx.levels, original_index.levels, check_dtype=True)
```

### Step 12: Assign ind2 = idx.set_levels(...)

```python
ind2 = idx.set_levels(new_levels, level=[0, 1])
```

**Verification:**
```python
assert_matching(idx.codes, original_index.codes, check_dtype=True)
```

### Step 13: Call assert_matching()

```python
assert_matching(ind2.levels, new_levels)
```

### Step 14: Call assert_matching()

```python
assert_matching(idx.levels, levels)
```

### Step 15: Assign original_index = idx.copy(...)

```python
original_index = idx.copy()
```

### Step 16: Call assert_matching()

```python
assert_matching(idx.levels, original_index.levels, check_dtype=True)
```

### Step 17: Call assert_matching()

```python
assert_matching(idx.codes, original_index.codes, check_dtype=True)
```

### Step 18: Call assert_matching()

```python
assert_matching(idx.levels, original_index.levels, check_dtype=True)
```

### Step 19: Call assert_matching()

```python
assert_matching(idx.codes, original_index.codes, check_dtype=True)
```

### Step 20: Call idx.set_levels()

```python
idx.set_levels(['c'], level=0)
```

### Step 21: Call idx.set_codes()

```python
idx.set_codes([0, 1, 2, 3, 4, 5], level=0)
```

### Step 22: Call idx.set_levels()

```python
idx.set_levels('c', level=0)
```

### Step 23: Call idx.set_codes()

```python
idx.set_codes(1, level=0)
```


## Complete Example

```python
# Setup
# Fixtures: idx

# Workflow
levels = idx.levels
new_levels = [[lev + 'a' for lev in level] for level in levels]
ind2 = idx.set_levels(new_levels)
assert_matching(ind2.levels, new_levels)
assert_matching(idx.levels, levels)
ind2 = idx.set_levels(new_levels[0], level=0)
assert_matching(ind2.levels, [new_levels[0], levels[1]])
assert_matching(idx.levels, levels)
ind2 = idx.set_levels(new_levels[1], level=1)
assert_matching(ind2.levels, [levels[0], new_levels[1]])
assert_matching(idx.levels, levels)
ind2 = idx.set_levels(new_levels, level=[0, 1])
assert_matching(ind2.levels, new_levels)
assert_matching(idx.levels, levels)
original_index = idx.copy()
with pytest.raises(ValueError, match='^On'):
    idx.set_levels(['c'], level=0)
assert_matching(idx.levels, original_index.levels, check_dtype=True)
with pytest.raises(ValueError, match='^On'):
    idx.set_codes([0, 1, 2, 3, 4, 5], level=0)
assert_matching(idx.codes, original_index.codes, check_dtype=True)
with pytest.raises(TypeError, match='^Levels'):
    idx.set_levels('c', level=0)
assert_matching(idx.levels, original_index.levels, check_dtype=True)
with pytest.raises(TypeError, match='^Codes'):
    idx.set_codes(1, level=0)
assert_matching(idx.codes, original_index.codes, check_dtype=True)
```

## Next Steps


---

*Source: test_get_set.py:162 | Complexity: Advanced | Last updated: 2026-06-02*