# How To: Index Equal Values Too Far

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test index equal values too far

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

### Step 1: Assign idx1 = Index(...)

```python
idx1 = Index([1, 2, 3])
```

### Step 2: Assign idx2 = Index(...)

```python
idx2 = Index([1, 2, 4])
```

### Step 3: Assign kwargs = value

```python
kwargs = {'check_exact': check_exact, 'rtol': rtol}
```

### Step 4: Assign msg = "Index are different\n\nIndex values are different \\(33\\.33333 %\\)\n\\[left\\]:  Index\\(\\[1, 2, 3\\], dtype='int64'\\)\n\\[right\\]: Index\\(\\[1, 2, 4\\], dtype='int64'\\)"

```python
msg = "Index are different\n\nIndex values are different \\(33\\.33333 %\\)\n\\[left\\]:  Index\\(\\[1, 2, 3\\], dtype='int64'\\)\n\\[right\\]: Index\\(\\[1, 2, 4\\], dtype='int64'\\)"
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
idx1 = Index([1, 2, 3])
idx2 = Index([1, 2, 4])
kwargs = {'check_exact': check_exact, 'rtol': rtol}
msg = "Index are different\n\nIndex values are different \\(33\\.33333 %\\)\n\\[left\\]:  Index\\(\\[1, 2, 3\\], dtype='int64'\\)\n\\[right\\]: Index\\(\\[1, 2, 4\\], dtype='int64'\\)"
with pytest.raises(AssertionError, match=msg):
    tm.assert_index_equal(idx1, idx2, **kwargs)
```

## Next Steps


---

*Source: test_assert_index_equal.py:133 | Complexity: Intermediate | Last updated: 2026-06-02*