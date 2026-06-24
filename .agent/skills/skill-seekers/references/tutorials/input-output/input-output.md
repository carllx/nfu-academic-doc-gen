# How To: Input Output

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test input output

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign l = value

```python
l = [nx.Graph([(1, 2)]), nx.Graph([(3, 4)], awesome=True)]
```

**Verification:**
```python
assert len(l) == 2
```

### Step 2: Assign U = nx.disjoint_union_all(...)

```python
U = nx.disjoint_union_all(l)
```

**Verification:**
```python
assert U.graph['awesome']
```

### Step 3: Assign C = nx.compose_all(...)

```python
C = nx.compose_all(l)
```

**Verification:**
```python
assert len(l) == 2
```

### Step 4: Assign l = value

```python
l = [nx.Graph([(1, 2)]), nx.Graph([(1, 2)])]
```

**Verification:**
```python
assert len(l) == 2
```

### Step 5: Assign R = nx.intersection_all(...)

```python
R = nx.intersection_all(l)
```

**Verification:**
```python
assert len(l) == 2
```


## Complete Example

```python
# Workflow
l = [nx.Graph([(1, 2)]), nx.Graph([(3, 4)], awesome=True)]
U = nx.disjoint_union_all(l)
assert len(l) == 2
assert U.graph['awesome']
C = nx.compose_all(l)
assert len(l) == 2
l = [nx.Graph([(1, 2)]), nx.Graph([(1, 2)])]
R = nx.intersection_all(l)
assert len(l) == 2
```

## Next Steps


---

*Source: test_all.py:251 | Complexity: Intermediate | Last updated: 2026-06-02*