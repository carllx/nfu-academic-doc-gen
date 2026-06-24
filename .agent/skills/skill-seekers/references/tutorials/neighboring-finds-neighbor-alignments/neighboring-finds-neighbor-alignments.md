# How To: Neighboring Finds Neighbor Alignments

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test neighboring finds neighbor alignments

## Prerequisites

**Required Modules:**
- `unittest`
- `collections`
- `nltk.translate`
- `nltk.translate.ibm_model`


## Step-by-Step Guide

### Step 1: Assign a_info = AlignmentInfo(...)

```python
a_info = AlignmentInfo((0, 3, 2), (None, 'des', 'œufs', 'verts'), ('UNUSED', 'green', 'eggs'), [[], [], [2], [1]])
```

### Step 2: Assign ibm_model = IBMModel(...)

```python
ibm_model = IBMModel([])
```

### Step 3: Assign neighbors = ibm_model.neighboring(...)

```python
neighbors = ibm_model.neighboring(a_info)
```

### Step 4: Assign neighbor_alignments = set(...)

```python
neighbor_alignments = set()
```

### Step 5: Assign expected_alignments = value

```python
expected_alignments = {(0, 0, 2), (0, 1, 2), (0, 2, 2), (0, 3, 0), (0, 3, 1), (0, 3, 3), (0, 2, 3), (0, 3, 2)}
```

### Step 6: Call self.assertEqual()

```python
self.assertEqual(neighbor_alignments, expected_alignments)
```

### Step 7: Call neighbor_alignments.add()

```python
neighbor_alignments.add(neighbor.alignment)
```


## Complete Example

```python
# Workflow
a_info = AlignmentInfo((0, 3, 2), (None, 'des', 'œufs', 'verts'), ('UNUSED', 'green', 'eggs'), [[], [], [2], [1]])
ibm_model = IBMModel([])
neighbors = ibm_model.neighboring(a_info)
neighbor_alignments = set()
for neighbor in neighbors:
    neighbor_alignments.add(neighbor.alignment)
expected_alignments = {(0, 0, 2), (0, 1, 2), (0, 2, 2), (0, 3, 0), (0, 3, 1), (0, 3, 3), (0, 2, 3), (0, 3, 2)}
self.assertEqual(neighbor_alignments, expected_alignments)
```

## Next Steps


---

*Source: test_ibm_model.py:137 | Complexity: Intermediate | Last updated: 2026-06-02*