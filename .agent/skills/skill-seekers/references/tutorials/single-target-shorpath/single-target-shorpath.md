# How To: Single Target Shorpath

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test single target shortest path

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign p = nx.single_target_shortest_path(...)

```python
p = nx.single_target_shortest_path(self.directed_cycle, 0)
```

**Verification:**
```python
assert p[3] == [3, 4, 5, 6, 0]
```

### Step 2: Assign p = nx.single_target_shortest_path(...)

```python
p = nx.single_target_shortest_path(self.cycle, 0)
```

**Verification:**
```python
assert p[3] == [3, 2, 1, 0]
```

### Step 3: Assign p = nx.single_target_shortest_path(...)

```python
p = nx.single_target_shortest_path(self.cycle, 0, cutoff=0)
```

**Verification:**
```python
assert p == {0: [0]}
```

### Step 4: Assign target = 8

```python
target = 8
```

### Step 5: Call nx.single_target_shortest_path()

```python
nx.single_target_shortest_path(self.cycle, target)
```


## Complete Example

```python
# Workflow
p = nx.single_target_shortest_path(self.directed_cycle, 0)
assert p[3] == [3, 4, 5, 6, 0]
p = nx.single_target_shortest_path(self.cycle, 0)
assert p[3] == [3, 2, 1, 0]
p = nx.single_target_shortest_path(self.cycle, 0, cutoff=0)
assert p == {0: [0]}
target = 8
with pytest.raises(nx.NodeNotFound, match=f'Target {target} not in G'):
    nx.single_target_shortest_path(self.cycle, target)
```

## Next Steps


---

*Source: test_unweighted.py:80 | Complexity: Intermediate | Last updated: 2026-06-02*