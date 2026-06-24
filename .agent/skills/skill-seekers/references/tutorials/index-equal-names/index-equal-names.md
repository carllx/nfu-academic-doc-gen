# How To: Index Equal Names

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test index equal names

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: name1, name2
```

## Step-by-Step Guide

### Step 1: Assign idx1 = Index(...)

```python
idx1 = Index([1, 2, 3], name=name1)
```

### Step 2: Assign idx2 = Index(...)

```python
idx2 = Index([1, 2, 3], name=name2)
```

### Step 3: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx1, idx2)
```

### Step 4: Assign name1 = value

```python
name1 = "'x'" if name1 == 'x' else name1
```

### Step 5: Assign name2 = value

```python
name2 = "'x'" if name2 == 'x' else name2
```

### Step 6: Assign msg = value

```python
msg = f'Index are different\n\nAttribute "names" are different\n\\[left\\]:  \\[{name1}\\]\n\\[right\\]: \\[{name2}\\]'
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx1, idx2)
```


## Complete Example

```python
# Setup
# Fixtures: name1, name2

# Workflow
idx1 = Index([1, 2, 3], name=name1)
idx2 = Index([1, 2, 3], name=name2)
if name1 == name2 or name1 is name2:
    tm.assert_index_equal(idx1, idx2)
else:
    name1 = "'x'" if name1 == 'x' else name1
    name2 = "'x'" if name2 == 'x' else name2
    msg = f'Index are different\n\nAttribute "names" are different\n\\[left\\]:  \\[{name1}\\]\n\\[right\\]: \\[{name2}\\]'
    with pytest.raises(AssertionError, match=msg):
        tm.assert_index_equal(idx1, idx2)
```

## Next Steps


---

*Source: test_assert_index_equal.py:189 | Complexity: Intermediate | Last updated: 2026-06-02*