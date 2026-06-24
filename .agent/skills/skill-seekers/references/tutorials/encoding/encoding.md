# How To: Encoding

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate Graph: Tests for encoding a tree as a Prüfer sequence using the
iterative strategy.

## Prerequisites

**Required Modules:**
- `itertools`
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign tree = nx.Graph(...)

```python
tree = nx.Graph([(0, 3), (1, 3), (2, 3), (3, 4), (4, 5)])
```


## Complete Example

```python
# Workflow
tree = nx.Graph([(0, 3), (1, 3), (2, 3), (3, 4), (4, 5)])
```

## Next Steps


---

*Source: test_coding.py:41 | Complexity: Beginner | Last updated: 2026-06-02*