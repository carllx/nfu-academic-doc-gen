# How To: Find Duplicate

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test find duplicate

## Prerequisites

**Required Modules:**
- `collections.abc`
- `pickle`
- `textwrap`
- `io`
- `os`
- `pathlib`
- `pytest`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign l1 = value

```python
l1 = [1, 2, 3, 4, 5, 6]
```

**Verification:**
```python
assert_(np.rec.find_duplicate(l1) == [])
```

### Step 2: Call assert_()

```python
assert_(np.rec.find_duplicate(l1) == [])
```

**Verification:**
```python
assert_(np.rec.find_duplicate(l2) == [1])
```

### Step 3: Assign l2 = value

```python
l2 = [1, 2, 1, 4, 5, 6]
```

**Verification:**
```python
assert_(np.rec.find_duplicate(l3) == [1, 2])
```

### Step 4: Call assert_()

```python
assert_(np.rec.find_duplicate(l2) == [1])
```

**Verification:**
```python
assert_(np.rec.find_duplicate(l3) == [2, 1])
```

### Step 5: Assign l3 = value

```python
l3 = [1, 2, 1, 4, 1, 6, 2, 3]
```

### Step 6: Call assert_()

```python
assert_(np.rec.find_duplicate(l3) == [1, 2])
```

### Step 7: Assign l3 = value

```python
l3 = [2, 2, 1, 4, 1, 6, 2, 3]
```

### Step 8: Call assert_()

```python
assert_(np.rec.find_duplicate(l3) == [2, 1])
```


## Complete Example

```python
# Workflow
l1 = [1, 2, 3, 4, 5, 6]
assert_(np.rec.find_duplicate(l1) == [])
l2 = [1, 2, 1, 4, 5, 6]
assert_(np.rec.find_duplicate(l2) == [1])
l3 = [1, 2, 1, 4, 1, 6, 2, 3]
assert_(np.rec.find_duplicate(l3) == [1, 2])
l3 = [2, 2, 1, 4, 1, 6, 2, 3]
assert_(np.rec.find_duplicate(l3) == [2, 1])
```

## Next Steps


---

*Source: test_records.py:533 | Complexity: Advanced | Last updated: 2026-06-02*