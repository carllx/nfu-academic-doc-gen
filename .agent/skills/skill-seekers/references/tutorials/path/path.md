# How To: Path

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test path

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `math`
- `pytest`
- `networkx`

**Setup Required:**
```python
# Fixtures: method
```

## Step-by-Step Guide

### Step 1: Call pytest.importorskip()

```python
pytest.importorskip('scipy')
```

**Verification:**
```python
assert ac == pytest.approx(sigma, abs=1e-07)
```

### Step 2: Assign G = nx.path_graph(...)

```python
G = nx.path_graph(8)
```

### Step 3: Assign A = nx.laplacian_matrix(...)

```python
A = nx.laplacian_matrix(G)
```

### Step 4: Assign sigma = value

```python
sigma = 2 - sqrt(2 + sqrt(2))
```

### Step 5: Assign ac = nx.algebraic_connectivity(...)

```python
ac = nx.algebraic_connectivity(G, tol=1e-12, method=method)
```

**Verification:**
```python
assert ac == pytest.approx(sigma, abs=1e-07)
```

### Step 6: Assign x = nx.fiedler_vector(...)

```python
x = nx.fiedler_vector(G, tol=1e-12, method=method)
```

### Step 7: Call check_eigenvector()

```python
check_eigenvector(A, sigma, x)
```


## Complete Example

```python
# Setup
# Fixtures: method

# Workflow
pytest.importorskip('scipy')
G = nx.path_graph(8)
A = nx.laplacian_matrix(G)
sigma = 2 - sqrt(2 + sqrt(2))
ac = nx.algebraic_connectivity(G, tol=1e-12, method=method)
assert ac == pytest.approx(sigma, abs=1e-07)
x = nx.fiedler_vector(G, tol=1e-12, method=method)
check_eigenvector(A, sigma, x)
```

## Next Steps


---

*Source: test_algebraic_connectivity.py:145 | Complexity: Intermediate | Last updated: 2026-06-02*