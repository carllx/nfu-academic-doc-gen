# How To: Node Tree Position

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: Test matching on nodes based on NLTK tree position.

## Prerequisites

**Required Modules:**
- `unittest`
- `nltk`
- `nltk.tree`


## Step-by-Step Guide

### Step 1: '\n        Test matching on nodes based on NLTK tree position.\n        '

```python
'\n        Test matching on nodes based on NLTK tree position.\n        '
```

### Step 2: Assign tree = ParentedTree.fromstring(...)

```python
tree = ParentedTree.fromstring('(S (NP-SBJ x) (NP x) (NNP x) (VP x))')
```

### Step 3: Assign leaf_positions = value

```python
leaf_positions = {tree.leaf_treeposition(x) for x in range(len(tree.leaves()))}
```

### Step 4: Assign tree_positions = value

```python
tree_positions = [x for x in tree.treepositions() if x not in leaf_positions]
```

### Step 5: Assign node_id = value

```python
node_id = f'N{position}'
```

### Step 6: Assign tgrep_positions = list(...)

```python
tgrep_positions = list(tgrep.tgrep_positions(node_id, [tree]))
```

### Step 7: Call self.assertEqual()

```python
self.assertEqual(len(tgrep_positions[0]), 1)
```

### Step 8: Call self.assertEqual()

```python
self.assertEqual(tgrep_positions[0][0], position)
```


## Complete Example

```python
# Workflow
'\n        Test matching on nodes based on NLTK tree position.\n        '
tree = ParentedTree.fromstring('(S (NP-SBJ x) (NP x) (NNP x) (VP x))')
leaf_positions = {tree.leaf_treeposition(x) for x in range(len(tree.leaves()))}
tree_positions = [x for x in tree.treepositions() if x not in leaf_positions]
for position in tree_positions:
    node_id = f'N{position}'
    tgrep_positions = list(tgrep.tgrep_positions(node_id, [tree]))
    self.assertEqual(len(tgrep_positions[0]), 1)
    self.assertEqual(tgrep_positions[0][0], position)
```

## Next Steps


---

*Source: test_tgrep.py:318 | Complexity: Advanced | Last updated: 2026-06-02*