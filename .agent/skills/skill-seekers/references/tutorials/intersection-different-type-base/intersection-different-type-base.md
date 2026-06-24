# How To: Intersection Different Type Base

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test intersection different type base

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
# Fixtures: klass, sort
```

## Step-by-Step Guide

### Step 1: Assign index = Index(...)

```python
index = Index([0, 'a', 1, 'b', 2, 'c'])
```

**Verification:**
```python
assert equal_contents(result, second)
```

### Step 2: Assign first = value

```python
first = index[:5]
```

### Step 3: Assign second = value

```python
second = index[:3]
```

### Step 4: Assign result = first.intersection(...)

```python
result = first.intersection(klass(second.values), sort=sort)
```

**Verification:**
```python
assert equal_contents(result, second)
```


## Complete Example

```python
# Setup
# Fixtures: klass, sort

# Workflow
index = Index([0, 'a', 1, 'b', 2, 'c'])
first = index[:5]
second = index[:3]
result = first.intersection(klass(second.values), sort=sort)
assert equal_contents(result, second)
```

## Next Steps


---

*Source: test_setops.py:122 | Complexity: Intermediate | Last updated: 2026-06-02*