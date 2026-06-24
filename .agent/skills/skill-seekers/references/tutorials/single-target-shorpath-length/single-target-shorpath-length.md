# How To: Single Target Shorpath Length

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test single target shortest path length

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign pl = value

```python
pl = nx.single_target_shortest_path_length
```

**Verification:**
```python
assert pl(self.cycle, 0) == lengths
```

### Step 2: Assign lengths = value

```python
lengths = {0: 0, 1: 1, 2: 2, 3: 3, 4: 3, 5: 2, 6: 1}
```

**Verification:**
```python
assert pl(self.directed_cycle, 0) == lengths
```

### Step 3: Assign lengths = value

```python
lengths = {0: 0, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
```

**Verification:**
```python
assert pl(self.directed_cycle, 0) == lengths
```

### Step 4: Assign target = 8

```python
target = 8
```

### Step 5: Call nx.single_target_shortest_path_length()

```python
nx.single_target_shortest_path_length(self.cycle, target)
```


## Complete Example

```python
# Workflow
pl = nx.single_target_shortest_path_length
lengths = {0: 0, 1: 1, 2: 2, 3: 3, 4: 3, 5: 2, 6: 1}
assert pl(self.cycle, 0) == lengths
lengths = {0: 0, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
assert pl(self.directed_cycle, 0) == lengths
target = 8
with pytest.raises(nx.NodeNotFound, match=f'Target {target} is not in G'):
    nx.single_target_shortest_path_length(self.cycle, target)
```

## Next Steps


---

*Source: test_unweighted.py:92 | Complexity: Intermediate | Last updated: 2026-06-02*