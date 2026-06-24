# How To: Degree Sequence

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: workflow, integration

## Overview

Workflow: Tests that the degree sequence of the generated graph matches
the input degree sequence.

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: 'Tests that the degree sequence of the generated graph matches\n        the input degree sequence.\n\n        '

```python
'Tests that the degree sequence of the generated graph matches\n        the input degree sequence.\n\n        '
```

**Verification:**
```python
assert sorted(dict(G.degree).values()) == sorted(deg_seq)
```

### Step 2: Assign deg_seq = value

```python
deg_seq = [5, 3, 3, 3, 3, 2, 2, 2, 1, 1, 1]
```

**Verification:**
```python
assert sorted(dict(G.degree(range(len(deg_seq)))).values()) == sorted(deg_seq)
```

### Step 3: Assign G = nx.configuration_model(...)

```python
G = nx.configuration_model(deg_seq, seed=12345678)
```

**Verification:**
```python
assert sorted(dict(G.degree).values()) == sorted(deg_seq)
```


## Complete Example

```python
# Workflow
'Tests that the degree sequence of the generated graph matches\n        the input degree sequence.\n\n        '
deg_seq = [5, 3, 3, 3, 3, 2, 2, 2, 1, 1, 1]
G = nx.configuration_model(deg_seq, seed=12345678)
assert sorted(dict(G.degree).values()) == sorted(deg_seq)
assert sorted(dict(G.degree(range(len(deg_seq)))).values()) == sorted(deg_seq)
```

## Next Steps


---

*Source: test_degree_seq.py:26 | Complexity: Beginner | Last updated: 2026-06-02*