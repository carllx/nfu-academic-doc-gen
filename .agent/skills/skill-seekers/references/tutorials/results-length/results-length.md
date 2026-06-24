# How To: Results Length

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: there is a result for every node

## Prerequisites

**Required Modules:**
- `networkx`


## Step-by-Step Guide

### Step 1: 'there is a result for every node'

```python
'there is a result for every node'
```

**Verification:**
```python
assert len(disp) == len(G)
```

### Step 2: Assign G = small_ego_G(...)

```python
G = small_ego_G()
```

**Verification:**
```python
assert len(disp_Gu) == len(G) - 1
```

### Step 3: Assign disp = nx.dispersion(...)

```python
disp = nx.dispersion(G)
```

**Verification:**
```python
assert isinstance(disp_uv, float)
```

### Step 4: Assign disp_Gu = nx.dispersion(...)

```python
disp_Gu = nx.dispersion(G, 'u')
```

### Step 5: Assign disp_uv = nx.dispersion(...)

```python
disp_uv = nx.dispersion(G, 'u', 'h')
```

**Verification:**
```python
assert len(disp) == len(G)
```


## Complete Example

```python
# Workflow
'there is a result for every node'
G = small_ego_G()
disp = nx.dispersion(G)
disp_Gu = nx.dispersion(G, 'u')
disp_uv = nx.dispersion(G, 'u', 'h')
assert len(disp) == len(G)
assert len(disp_Gu) == len(G) - 1
assert isinstance(disp_uv, float)
```

## Next Steps


---

*Source: test_dispersion.py:51 | Complexity: Intermediate | Last updated: 2026-06-02*