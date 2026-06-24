# How To: Omega

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test omega

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign Gl = nx.connected_watts_strogatz_graph(...)

```python
Gl = nx.connected_watts_strogatz_graph(50, 6, 0, seed=rng)
```

**Verification:**
```python
assert omegal < omegas and omegas < omegar
```

### Step 2: Assign Gr = nx.connected_watts_strogatz_graph(...)

```python
Gr = nx.connected_watts_strogatz_graph(50, 6, 1, seed=rng)
```

**Verification:**
```python
assert -1 <= o <= 1
```

### Step 3: Assign Gs = nx.connected_watts_strogatz_graph(...)

```python
Gs = nx.connected_watts_strogatz_graph(50, 6, 0.1, seed=rng)
```

### Step 4: Assign omegal = omega(...)

```python
omegal = omega(Gl, niter=1, nrand=1, seed=rng)
```

### Step 5: Assign omegar = omega(...)

```python
omegar = omega(Gr, niter=1, nrand=1, seed=rng)
```

### Step 6: Assign omegas = omega(...)

```python
omegas = omega(Gs, niter=1, nrand=1, seed=rng)
```

**Verification:**
```python
assert omegal < omegas and omegas < omegar
```

### Step 7: Assign G_barbell = nx.barbell_graph(...)

```python
G_barbell = nx.barbell_graph(5, 1)
```

### Step 8: Assign G_karate = nx.karate_club_graph(...)

```python
G_karate = nx.karate_club_graph()
```

### Step 9: Assign omega_barbell = nx.omega(...)

```python
omega_barbell = nx.omega(G_barbell)
```

### Step 10: Assign omega_karate = nx.omega(...)

```python
omega_karate = nx.omega(G_karate, nrand=2)
```

### Step 11: Assign omegas = value

```python
omegas = (omegal, omegar, omegas, omega_barbell, omega_karate)
```

**Verification:**
```python
assert -1 <= o <= 1
```


## Complete Example

```python
# Workflow
Gl = nx.connected_watts_strogatz_graph(50, 6, 0, seed=rng)
Gr = nx.connected_watts_strogatz_graph(50, 6, 1, seed=rng)
Gs = nx.connected_watts_strogatz_graph(50, 6, 0.1, seed=rng)
omegal = omega(Gl, niter=1, nrand=1, seed=rng)
omegar = omega(Gr, niter=1, nrand=1, seed=rng)
omegas = omega(Gs, niter=1, nrand=1, seed=rng)
assert omegal < omegas and omegas < omegar
G_barbell = nx.barbell_graph(5, 1)
G_karate = nx.karate_club_graph()
omega_barbell = nx.omega(G_barbell)
omega_karate = nx.omega(G_karate, nrand=2)
omegas = (omegal, omegar, omegas, omega_barbell, omega_karate)
for o in omegas:
    assert -1 <= o <= 1
```

## Next Steps


---

*Source: test_smallworld.py:49 | Complexity: Advanced | Last updated: 2026-06-02*