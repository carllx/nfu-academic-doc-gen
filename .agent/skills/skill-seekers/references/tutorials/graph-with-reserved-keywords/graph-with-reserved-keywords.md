# How To: Graph With Reserved Keywords

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test graph with reserved keywords

## Prerequisites

**Required Modules:**
- `warnings`
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

### Step 2: Assign G = self.build_graph(...)

```python
G = self.build_graph(G)
```

### Step 3: Assign unknown = 'keyword'

```python
G.nodes['E']['n'] = 'keyword'
```

### Step 4: Assign unknown = 'keyword'

```python
G.edges['A', 'B']['u'] = 'keyword'
```

### Step 5: Assign unknown = 'keyword'

```python
G.edges['A', 'B']['v'] = 'keyword'
```

### Step 6: Assign A = nx.nx_agraph.to_agraph(...)

```python
A = nx.nx_agraph.to_agraph(G)
```


## Complete Example

```python
# Workflow
G = nx.Graph()
G = self.build_graph(G)
G.nodes['E']['n'] = 'keyword'
G.edges['A', 'B']['u'] = 'keyword'
G.edges['A', 'B']['v'] = 'keyword'
A = nx.nx_agraph.to_agraph(G)
```

## Next Steps


---

*Source: test_agraph.py:138 | Complexity: Intermediate | Last updated: 2026-06-02*