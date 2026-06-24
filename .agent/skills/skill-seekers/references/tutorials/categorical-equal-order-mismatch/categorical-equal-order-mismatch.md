# How To: Categorical Equal Order Mismatch

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test categorical equal order mismatch

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: check_category_order
```

## Step-by-Step Guide

### Step 1: Assign c1 = Categorical(...)

```python
c1 = Categorical([1, 2, 3, 4], categories=[1, 2, 3, 4])
```

### Step 2: Assign c2 = Categorical(...)

```python
c2 = Categorical([1, 2, 3, 4], categories=[4, 3, 2, 1])
```

### Step 3: Assign kwargs = value

```python
kwargs = {'check_category_order': check_category_order}
```

### Step 4: Assign msg = "Categorical\\.categories are different\n\nCategorical\\.categories values are different \\(100\\.0 %\\)\n\\[left\\]:  Index\\(\\[1, 2, 3, 4\\], dtype='int64'\\)\n\\[right\\]: Index\\(\\[4, 3, 2, 1\\], dtype='int64'\\)"

```python
msg = "Categorical\\.categories are different\n\nCategorical\\.categories values are different \\(100\\.0 %\\)\n\\[left\\]:  Index\\(\\[1, 2, 3, 4\\], dtype='int64'\\)\n\\[right\\]: Index\\(\\[4, 3, 2, 1\\], dtype='int64'\\)"
```

### Step 5: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(c1, c2, **kwargs)
```

### Step 6: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(c1, c2, **kwargs)
```


## Complete Example

```python
# Setup
# Fixtures: check_category_order

# Workflow
c1 = Categorical([1, 2, 3, 4], categories=[1, 2, 3, 4])
c2 = Categorical([1, 2, 3, 4], categories=[4, 3, 2, 1])
kwargs = {'check_category_order': check_category_order}
if check_category_order:
    msg = "Categorical\\.categories are different\n\nCategorical\\.categories values are different \\(100\\.0 %\\)\n\\[left\\]:  Index\\(\\[1, 2, 3, 4\\], dtype='int64'\\)\n\\[right\\]: Index\\(\\[4, 3, 2, 1\\], dtype='int64'\\)"
    with pytest.raises(AssertionError, match=msg):
        tm.assert_categorical_equal(c1, c2, **kwargs)
else:
    tm.assert_categorical_equal(c1, c2, **kwargs)
```

## Next Steps


---

*Source: test_assert_categorical_equal.py:16 | Complexity: Intermediate | Last updated: 2026-06-02*