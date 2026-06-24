# How To: Spring Layout Graph Size Heuristic

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: Expect 'force' layout for n < 500 and 'energy' for n >= 500

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `networkx`
- `math`

**Setup Required:**
```python
# Fixtures: num_nodes, expected_method, extra_layout_kwargs
```

## Step-by-Step Guide

### Step 1: "Expect 'force' layout for n < 500 and 'energy' for n >= 500"

```python
"Expect 'force' layout for n < 500 and 'energy' for n >= 500"
```

**Verification:**
```python
assert np.allclose(list(expected.values()), list(actual.values()), atol=1e-05)
```

### Step 2: Assign G = nx.cycle_graph(...)

```python
G = nx.cycle_graph(num_nodes)
```

### Step 3: Assign seed = 163674319

```python
seed = 163674319
```

### Step 4: Assign expected = nx.spring_layout(...)

```python
expected = nx.spring_layout(G, method=expected_method, seed=seed, **extra_layout_kwargs)
```

### Step 5: Assign actual = nx.spring_layout(...)

```python
actual = nx.spring_layout(G, method='auto', seed=seed, **extra_layout_kwargs)
```

**Verification:**
```python
assert np.allclose(list(expected.values()), list(actual.values()), atol=1e-05)
```


## Complete Example

```python
# Setup
# Fixtures: num_nodes, expected_method, extra_layout_kwargs

# Workflow
"Expect 'force' layout for n < 500 and 'energy' for n >= 500"
G = nx.cycle_graph(num_nodes)
seed = 163674319
expected = nx.spring_layout(G, method=expected_method, seed=seed, **extra_layout_kwargs)
actual = nx.spring_layout(G, method='auto', seed=seed, **extra_layout_kwargs)
assert np.allclose(list(expected.values()), list(actual.values()), atol=1e-05)
```

## Next Steps


---

*Source: test_layout.py:618 | Complexity: Intermediate | Last updated: 2026-06-02*