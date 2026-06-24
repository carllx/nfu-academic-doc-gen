# How To: Case V Plus Not In A Cal

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test case V plus not in A cal

## Prerequisites

**Required Modules:**
- `itertools`
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign L = value

```python
L = {0: [2, 5], 1: [3, 4], 2: [0, 8], 3: [1, 7], 4: [1, 6], 5: [0, 6], 6: [4, 5], 7: [3], 8: [2]}
```

### Step 2: Assign F = value

```python
F = {0: 0, 1: 0, 2: 1, 3: 1, 4: 1, 5: 1, 6: 2, 7: 2, 8: 2}
```

### Step 3: Assign C = nx.algorithms.coloring.equitable_coloring.make_C_from_F(...)

```python
C = nx.algorithms.coloring.equitable_coloring.make_C_from_F(F)
```

### Step 4: Assign N = nx.algorithms.coloring.equitable_coloring.make_N_from_L_C(...)

```python
N = nx.algorithms.coloring.equitable_coloring.make_N_from_L_C(L, C)
```

### Step 5: Assign H = nx.algorithms.coloring.equitable_coloring.make_H_from_C_N(...)

```python
H = nx.algorithms.coloring.equitable_coloring.make_H_from_C_N(C, N)
```

### Step 6: Call nx.algorithms.coloring.equitable_coloring.procedure_P()

```python
nx.algorithms.coloring.equitable_coloring.procedure_P(V_minus=0, V_plus=1, N=N, H=H, F=F, C=C, L=L)
```

### Step 7: Call check_state()

```python
check_state(L=L, N=N, H=H, F=F, C=C)
```


## Complete Example

```python
# Workflow
L = {0: [2, 5], 1: [3, 4], 2: [0, 8], 3: [1, 7], 4: [1, 6], 5: [0, 6], 6: [4, 5], 7: [3], 8: [2]}
F = {0: 0, 1: 0, 2: 1, 3: 1, 4: 1, 5: 1, 6: 2, 7: 2, 8: 2}
C = nx.algorithms.coloring.equitable_coloring.make_C_from_F(F)
N = nx.algorithms.coloring.equitable_coloring.make_N_from_L_C(L, C)
H = nx.algorithms.coloring.equitable_coloring.make_H_from_C_N(C, N)
nx.algorithms.coloring.equitable_coloring.procedure_P(V_minus=0, V_plus=1, N=N, H=H, F=F, C=C, L=L)
check_state(L=L, N=N, H=H, F=F, C=C)
```

## Next Steps


---

*Source: test_coloring.py:137 | Complexity: Intermediate | Last updated: 2026-06-02*