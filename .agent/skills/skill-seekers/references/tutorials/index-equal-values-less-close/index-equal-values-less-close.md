# How To: Index Equal Values Less Close

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test index equal values less close

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
idx1 = Index([1, 2, 3.0])
```

### Step 2: Assign idx2 = Index(...)

```python
idx2 = Index([1, 2, 3.0001])
```

### Step 3: Assign kwargs = value

```python
kwargs = {'check_exact': check_exact, 'rtol': rtol}
```

### Step 4: Assign msg = "Index are different\n\nIndex values are different \\(33\\.33333 %\\)\n\\[left\\]:  Index\\(\\[1.0, 2.0, 3.0], dtype='float64'\\)\n\\[right\\]: Index\\(\\[1.0, 2.0, 3.0001\\], dtype='float64'\\)"

```python
msg = "Index are different\n\nIndex values are different \\(33\\.33333 %\\)\n\\[left\\]:  Index\\(\\[1.0, 2.0, 3.0], dtype='float64'\\)\n\\[right\\]: Index\\(\\[1.0, 2.0, 3.0001\\], dtype='float64'\\)"
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx1, idx2, **kwargs)
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx1, idx2, **kwargs)
```


## Complete Example

```python
# Setup
# Fixtures: check_exact, rtol

# Workflow
idx1 = Index([1, 2, 3.0])
idx2 = Index([1, 2, 3.0001])
kwargs = {'check_exact': check_exact, 'rtol': rtol}
if check_exact or rtol < 0.0005:
    msg = "Index are different\n\nIndex values are different \\(33\\.33333 %\\)\n\\[left\\]:  Index\\(\\[1.0, 2.0, 3.0], dtype='float64'\\)\n\\[right\\]: Index\\(\\[1.0, 2.0, 3.0001\\], dtype='float64'\\)"
    with pytest.raises(AssertionError, match=msg):
        tm.assert_index_equal(idx1, idx2, **kwargs)
else:
    tm.assert_index_equal(idx1, idx2, **kwargs)
```

## Next Steps


---

*Source: test_assert_index_equal.py:115 | Complexity: Intermediate | Last updated: 2026-06-02*