# How To: Complete Bipartite Graph

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: workflow, integration

## Overview

Workflow: test complete bipartite graph

## Prerequisites

**Required Modules:**
- `io`
- `pytest`
- `networkx`
- `networkx.readwrite.graph6`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign result = BytesIO(...)

```python
result = BytesIO()
```

**Verification:**
```python
assert result.getvalue() == b'N??F~z{~Fw^_~?~?^_?\n'
```

### Step 2: Assign G = nx.complete_bipartite_graph(...)

```python
G = nx.complete_bipartite_graph(6, 9)
```

### Step 3: Call nx.write_graph6()

```python
nx.write_graph6(G, result, header=False)
```

**Verification:**
```python
assert result.getvalue() == b'N??F~z{~Fw^_~?~?^_?\n'
```


## Complete Example

```python
# Workflow
result = BytesIO()
G = nx.complete_bipartite_graph(6, 9)
nx.write_graph6(G, result, header=False)
assert result.getvalue() == b'N??F~z{~Fw^_~?~?^_?\n'
```

## Next Steps


---

*Source: test_graph6.py:88 | Complexity: Beginner | Last updated: 2026-06-02*