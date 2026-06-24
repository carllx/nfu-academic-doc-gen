# How To: Index Equal Level Values Mismatch

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test index equal level values mismatch

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: check_exact, rtol
```

## Step-by-Step Guide

### Step 1: Assign idx1 = MultiIndex.from_tuples(...)

```python
idx1 = MultiIndex.from_tuples([('A', 2), ('A', 2), ('B', 3), ('B', 4)])
```

### Step 2: Assign idx2 = MultiIndex.from_tuples(...)

```python
idx2 = MultiIndex.from_tuples([('A', 1), ('A', 2), ('B', 3), ('B', 4)])
```

### Step 3: Assign kwargs = value

```python
kwargs = {'check_exact': check_exact, 'rtol': rtol}
```

### Step 4: Assign msg = "MultiIndex level \\[1\\] are different\n\nMultiIndex level \\[1\\] values are different \\(25\\.0 %\\)\n\\[left\\]:  Index\\(\\[2, 2, 3, 4\\], dtype='int64'\\)\n\\[right\\]: Index\\(\\[1, 2, 3, 4\\], dtype='int64'\\)"

```python
msg = "MultiIndex level \\[1\\] are different\n\nMultiIndex level \\[1\\] values are different \\(25\\.0 %\\)\n\\[left\\]:  Index\\(\\[2, 2, 3, 4\\], dtype='int64'\\)\n\\[right\\]: Index\\(\\[1, 2, 3, 4\\], dtype='int64'\\)"
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx1, idx2, **kwargs)
```


## Complete Example

```python
# Setup
# Fixtures: check_exact, rtol

# Workflow
idx1 = MultiIndex.from_tuples([('A', 2), ('A', 2), ('B', 3), ('B', 4)])
idx2 = MultiIndex.from_tuples([('A', 1), ('A', 2), ('B', 3), ('B', 4)])
kwargs = {'check_exact': check_exact, 'rtol': rtol}
msg = "MultiIndex level \\[1\\] are different\n\nMultiIndex level \\[1\\] values are different \\(25\\.0 %\\)\n\\[left\\]:  Index\\(\\[2, 2, 3, 4\\], dtype='int64'\\)\n\\[right\\]: Index\\(\\[1, 2, 3, 4\\], dtype='int64'\\)"
with pytest.raises(AssertionError, match=msg):
    tm.assert_index_equal(idx1, idx2, **kwargs)
```

## Next Steps


---

*Source: test_assert_index_equal.py:170 | Complexity: Intermediate | Last updated: 2026-06-02*