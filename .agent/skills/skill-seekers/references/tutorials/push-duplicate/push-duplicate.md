# How To: Push Duplicate

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test push duplicate

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx.utils.mapped_queue`


## Step-by-Step Guide

### Step 1: Assign to_push = value

```python
to_push = [2, 1, 0]
```

**Verification:**
```python
assert inserted
```

### Step 2: Assign h_sifted = value

```python
h_sifted = [0, 2, 1]
```

**Verification:**
```python
assert q.heap == h_sifted
```

### Step 3: Assign q = MappedQueue(...)

```python
q = MappedQueue()
```

**Verification:**
```python
assert not inserted
```

### Step 4: Call self._check_map()

```python
self._check_map(q)
```

### Step 5: Assign inserted = q.push(...)

```python
inserted = q.push(1, priority=1)
```

**Verification:**
```python
assert not inserted
```

### Step 6: Assign inserted = q.push(...)

```python
inserted = q.push(elt, priority=elt)
```

**Verification:**
```python
assert inserted
```


## Complete Example

```python
# Workflow
to_push = [2, 1, 0]
h_sifted = [0, 2, 1]
q = MappedQueue()
for elt in to_push:
    inserted = q.push(elt, priority=elt)
    assert inserted
assert q.heap == h_sifted
self._check_map(q)
inserted = q.push(1, priority=1)
assert not inserted
```

## Next Steps


---

*Source: test_mapped_queue.py:244 | Complexity: Intermediate | Last updated: 2026-06-02*