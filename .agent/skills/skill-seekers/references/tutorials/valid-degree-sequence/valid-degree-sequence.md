# How To: Valid Degree Sequence

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test valid degree sequence

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `networkx`

**Setup Required:**
```python
# Fixtures: deg_seq, valid, reason
```

## Step-by-Step Guide

### Step 1: Assign unknown = nx.utils.is_valid_tree_degree_sequence(...)

```python
v, r = nx.utils.is_valid_tree_degree_sequence(deg_seq)
```

**Verification:**
```python
assert v == valid
```


## Complete Example

```python
# Setup
# Fixtures: deg_seq, valid, reason

# Workflow
v, r = nx.utils.is_valid_tree_degree_sequence(deg_seq)
assert v == valid
assert reason in r
```

## Next Steps


---

*Source: test_random_sequence.py:22 | Complexity: Beginner | Last updated: 2026-06-02*