# How To: Full Rary Tree

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test full rary tree

## Prerequisites

**Required Modules:**
- `itertools`
- `typing`
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign r = 2

```python
r = 2
```

**Verification:**
```python
assert t.order() == n
```

### Step 2: Assign n = 9

```python
n = 9
```

**Verification:**
```python
assert nx.is_connected(t)
```

### Step 3: Assign t = nx.full_rary_tree(...)

```python
t = nx.full_rary_tree(r, n)
```

**Verification:**
```python
assert dh[0] == 0
```

### Step 4: Assign dh = nx.degree_histogram(...)

```python
dh = nx.degree_histogram(t)
```

**Verification:**
```python
assert dh[1] == 5
```


## Complete Example

```python
# Workflow
r = 2
n = 9
t = nx.full_rary_tree(r, n)
assert t.order() == n
assert nx.is_connected(t)
dh = nx.degree_histogram(t)
assert dh[0] == 0
assert dh[1] == 5
assert dh[r] == 1
assert dh[r + 1] == 9 - 5 - 1
assert len(dh) == r + 2
```

## Next Steps


---

*Source: test_classic.py:53 | Complexity: Intermediate | Last updated: 2026-06-02*