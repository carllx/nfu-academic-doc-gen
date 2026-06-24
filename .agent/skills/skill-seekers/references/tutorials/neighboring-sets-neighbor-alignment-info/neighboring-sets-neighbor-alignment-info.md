# How To: Neighboring Sets Neighbor Alignment Info

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test neighboring sets neighbor alignment info

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

### Step 4: Call self.assertEqual()

```python
self.assertEqual(moved_alignment.cepts, [[], [], [1, 2], []])
```

### Step 5: Call self.assertEqual()

```python
self.assertEqual(swapped_alignment.cepts, [[], [], [2], [1]])
```

### Step 6: Assign moved_alignment = neighbor

```python
moved_alignment = neighbor
```

### Step 7: Assign swapped_alignment = neighbor

```python
swapped_alignment = neighbor
```


## Complete Example

```python
# Workflow
a_info = AlignmentInfo((0, 3, 2), (None, 'des', 'œufs', 'verts'), ('UNUSED', 'green', 'eggs'), [[], [], [2], [1]])
ibm_model = IBMModel([])
neighbors = ibm_model.neighboring(a_info)
for neighbor in neighbors:
    if neighbor.alignment == (0, 2, 2):
        moved_alignment = neighbor
    elif neighbor.alignment == (0, 3, 2):
        swapped_alignment = neighbor
self.assertEqual(moved_alignment.cepts, [[], [], [1, 2], []])
self.assertEqual(swapped_alignment.cepts, [[], [], [2], [1]])
```

## Next Steps


---

*Source: test_ibm_model.py:169 | Complexity: Intermediate | Last updated: 2026-06-02*