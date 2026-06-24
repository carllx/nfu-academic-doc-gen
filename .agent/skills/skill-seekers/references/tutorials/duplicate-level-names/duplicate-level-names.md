# How To: Duplicate Level Names

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test duplicate level names

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `itertools`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: names
```

## Step-by-Step Guide

### Step 1: Assign mi = MultiIndex.from_product(...)

```python
mi = MultiIndex.from_product([[0, 1]] * 3, names=names)
```

**Verification:**
```python
assert mi.names == names
```

### Step 2: Assign mi = MultiIndex.from_product(...)

```python
mi = MultiIndex.from_product([[0, 1]] * 3)
```

**Verification:**
```python
assert mi.names == names
```

### Step 3: Assign mi = mi.rename(...)

```python
mi = mi.rename(names)
```

**Verification:**
```python
assert mi.names == names
```

### Step 4: Call mi.rename()

```python
mi.rename(names[1], level=1, inplace=True)
```

### Step 5: Assign mi = mi.rename(...)

```python
mi = mi.rename([names[0], names[2]], level=[0, 2])
```

**Verification:**
```python
assert mi.names == names
```


## Complete Example

```python
# Setup
# Fixtures: names

# Workflow
mi = MultiIndex.from_product([[0, 1]] * 3, names=names)
assert mi.names == names
mi = MultiIndex.from_product([[0, 1]] * 3)
mi = mi.rename(names)
assert mi.names == names
mi.rename(names[1], level=1, inplace=True)
mi = mi.rename([names[0], names[2]], level=[0, 2])
assert mi.names == names
```

## Next Steps


---

*Source: test_duplicates.py:116 | Complexity: Intermediate | Last updated: 2026-06-02*