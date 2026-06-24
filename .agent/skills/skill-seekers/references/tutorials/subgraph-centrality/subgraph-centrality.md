# How To: Subgraph Centrality

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate Graph: test subgraph centrality

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms.centrality.subgraph_alg`


## Step-by-Step Guide

### Step 1: Assign G1 = nx.Graph(...)

```python
G1 = nx.Graph([('Franck', 'Aric'), ('Aric', 'Dan'), ('Dan', 'Albert'), ('Albert', 'Franck'), ('Dan', '1'), ('Franck', 'Albert')])
```


## Complete Example

```python
# Workflow
G1 = nx.Graph([('Franck', 'Aric'), ('Aric', 'Dan'), ('Dan', 'Albert'), ('Albert', 'Franck'), ('Dan', '1'), ('Franck', 'Albert')])
```

## Next Steps


---

*Source: test_subgraph.py:29 | Complexity: Beginner | Last updated: 2026-06-02*