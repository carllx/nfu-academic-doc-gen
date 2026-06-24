# How To: Converge To Betweenness

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: percolation centrality: should converge to betweenness
centrality when all nodes are percolated the same

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: 'percolation centrality: should converge to betweenness\n    centrality when all nodes are percolated the same'

```python
'percolation centrality: should converge to betweenness\n    centrality when all nodes are percolated the same'
```

**Verification:**
```python
assert p_answer == pytest.approx(b_answer, abs=0.001)
```

### Step 2: Assign G = nx.florentine_families_graph(...)

```python
G = nx.florentine_families_graph()
```

**Verification:**
```python
assert p_answer == pytest.approx(b_answer, abs=0.001)
```

### Step 3: Assign b_answer = value

```python
b_answer = {'Acciaiuoli': 0.0, 'Albizzi': 0.212, 'Barbadori': 0.093, 'Bischeri': 0.104, 'Castellani': 0.055, 'Ginori': 0.0, 'Guadagni': 0.255, 'Lamberteschi': 0.0, 'Medici': 0.522, 'Pazzi': 0.0, 'Peruzzi': 0.022, 'Ridolfi': 0.114, 'Salviati': 0.143, 'Strozzi': 0.103, 'Tornabuoni': 0.092}
```

### Step 4: Assign p_answer = nx.percolation_centrality(...)

```python
p_answer = nx.percolation_centrality(G)
```

**Verification:**
```python
assert p_answer == pytest.approx(b_answer, abs=0.001)
```

### Step 5: Assign p_states = value

```python
p_states = {k: 0.3 for k, v in b_answer.items()}
```

### Step 6: Assign p_answer = nx.percolation_centrality(...)

```python
p_answer = nx.percolation_centrality(G, states=p_states)
```

**Verification:**
```python
assert p_answer == pytest.approx(b_answer, abs=0.001)
```


## Complete Example

```python
# Workflow
'percolation centrality: should converge to betweenness\n    centrality when all nodes are percolated the same'
G = nx.florentine_families_graph()
b_answer = {'Acciaiuoli': 0.0, 'Albizzi': 0.212, 'Barbadori': 0.093, 'Bischeri': 0.104, 'Castellani': 0.055, 'Ginori': 0.0, 'Guadagni': 0.255, 'Lamberteschi': 0.0, 'Medici': 0.522, 'Pazzi': 0.0, 'Peruzzi': 0.022, 'Ridolfi': 0.114, 'Salviati': 0.143, 'Strozzi': 0.103, 'Tornabuoni': 0.092}
p_answer = nx.percolation_centrality(G)
assert p_answer == pytest.approx(b_answer, abs=0.001)
p_states = {k: 0.3 for k, v in b_answer.items()}
p_answer = nx.percolation_centrality(G, states=p_states)
assert p_answer == pytest.approx(b_answer, abs=0.001)
```

## Next Steps


---

*Source: test_percolation_centrality.py:52 | Complexity: Intermediate | Last updated: 2026-06-02*