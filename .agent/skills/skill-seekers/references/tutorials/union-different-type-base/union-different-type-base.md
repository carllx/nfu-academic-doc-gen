# How To: Union Different Type Base

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test union different type base

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.algorithms`

**Setup Required:**
```python
# Fixtures: klass
```

## Step-by-Step Guide

### Step 1: Assign index = Index(...)

```python
index = Index([0, 'a', 1, 'b', 2, 'c'])
```

**Verification:**
```python
assert equal_contents(result, index)
```

### Step 2: Assign first = value

```python
first = index[3:]
```

### Step 3: Assign second = value

```python
second = index[:5]
```

### Step 4: Assign result = first.union(...)

```python
result = first.union(klass(second.values))
```

**Verification:**
```python
assert equal_contents(result, index)
```


## Complete Example

```python
# Setup
# Fixtures: klass

# Workflow
index = Index([0, 'a', 1, 'b', 2, 'c'])
first = index[3:]
second = index[:5]
result = first.union(klass(second.values))
assert equal_contents(result, index)
```

## Next Steps


---

*Source: test_setops.py:73 | Complexity: Intermediate | Last updated: 2026-06-02*