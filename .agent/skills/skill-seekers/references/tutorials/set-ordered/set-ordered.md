# How To: Set Ordered

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test set ordered

## Prerequisites

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.categorical`


## Step-by-Step Guide

### Step 1: Assign cat = Categorical(...)

```python
cat = Categorical(['a', 'b', 'c', 'a'], ordered=True)
```

**Verification:**
```python
assert not cat2.ordered
```

### Step 2: Assign cat2 = cat.as_unordered(...)

```python
cat2 = cat.as_unordered()
```

**Verification:**
```python
assert cat2.ordered
```

### Step 3: Assign cat2 = cat.as_ordered(...)

```python
cat2 = cat.as_ordered()
```

**Verification:**
```python
assert cat2.set_ordered(True).ordered
```

### Step 4: Assign msg = value

```python
msg = "property 'ordered' of 'Categorical' object has no setter" if PY311 else "can't set attribute"
```

**Verification:**
```python
assert not cat2.set_ordered(False).ordered
```

### Step 5: Assign cat.ordered = True

```python
cat.ordered = True
```

### Step 6: Assign cat.ordered = False

```python
cat.ordered = False
```


## Complete Example

```python
# Workflow
cat = Categorical(['a', 'b', 'c', 'a'], ordered=True)
cat2 = cat.as_unordered()
assert not cat2.ordered
cat2 = cat.as_ordered()
assert cat2.ordered
assert cat2.set_ordered(True).ordered
assert not cat2.set_ordered(False).ordered
msg = "property 'ordered' of 'Categorical' object has no setter" if PY311 else "can't set attribute"
with pytest.raises(AttributeError, match=msg):
    cat.ordered = True
with pytest.raises(AttributeError, match=msg):
    cat.ordered = False
```

## Next Steps


---

*Source: test_api.py:46 | Complexity: Intermediate | Last updated: 2026-06-02*