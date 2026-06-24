# How To: Degree Sequence Tree

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test degree sequence tree

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `networkx`

**Setup Required:**
```python
# Fixtures: deg_seq
```

## Step-by-Step Guide

### Step 1: Assign G = nx.degree_sequence_tree(...)

```python
G = nx.degree_sequence_tree(deg_seq)
```

**Verification:**
```python
assert sorted(dict(G.degree).values()) == sorted(deg_seq)
```


## Complete Example

```python
# Setup
# Fixtures: deg_seq

# Workflow
G = nx.degree_sequence_tree(deg_seq)
assert sorted(dict(G.degree).values()) == sorted(deg_seq)
assert nx.is_tree(G)
```

## Next Steps


---

*Source: test_degree_seq.py:173 | Complexity: Beginner | Last updated: 2026-06-02*