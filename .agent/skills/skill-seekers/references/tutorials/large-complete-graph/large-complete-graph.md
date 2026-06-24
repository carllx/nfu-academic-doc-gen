# How To: Large Complete Graph

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: workflow, integration

## Overview

Workflow: test large complete graph

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
assert result.getvalue() == b'~?@B' + b'~' * 368 + b'w\n'
```

### Step 2: Call nx.write_graph6()

```python
nx.write_graph6(nx.complete_graph(67), result, header=False)
```

**Verification:**
```python
assert result.getvalue() == b'~?@B' + b'~' * 368 + b'w\n'
```


## Complete Example

```python
# Workflow
result = BytesIO()
nx.write_graph6(nx.complete_graph(67), result, header=False)
assert result.getvalue() == b'~?@B' + b'~' * 368 + b'w\n'
```

## Next Steps


---

*Source: test_graph6.py:78 | Complexity: Beginner | Last updated: 2026-06-02*