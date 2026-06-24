# How To: Hillclimb

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: unittest, mock, workflow, integration

## Overview

Workflow: test hillclimb

## Prerequisites

**Required Modules:**
- `unittest`
- `collections`
- `nltk.translate`
- `nltk.translate.ibm_model`


## Step-by-Step Guide

### Step 1: Assign initial_alignment = AlignmentInfo(...)

```python
initial_alignment = AlignmentInfo((0, 3, 2), None, None, None)
```

### Step 2: Assign ibm_model = IBMModel(...)

```python
ibm_model = IBMModel([])
```

### Step 3: Assign ibm_model.neighboring = neighboring_mock

```python
ibm_model.neighboring = neighboring_mock
```

### Step 4: Assign ibm_model.prob_t_a_given_s = prob_t_a_given_s_mock

```python
ibm_model.prob_t_a_given_s = prob_t_a_given_s_mock
```

### Step 5: Assign best_alignment = ibm_model.hillclimb(...)

```python
best_alignment = ibm_model.hillclimb(initial_alignment)
```

### Step 6: Call self.assertEqual()

```python
self.assertEqual(best_alignment.alignment, (0, 4, 4))
```

### Step 7: Assign prob_values = value

```python
prob_values = {(0, 3, 2): 0.5, (0, 2, 2): 0.6, (0, 1, 1): 0.4, (0, 3, 3): 0.6, (0, 4, 4): 0.7}
```


## Complete Example

```python
# Workflow
initial_alignment = AlignmentInfo((0, 3, 2), None, None, None)

def neighboring_mock(a, j):
    if a.alignment == (0, 3, 2):
        return {AlignmentInfo((0, 2, 2), None, None, None), AlignmentInfo((0, 1, 1), None, None, None)}
    elif a.alignment == (0, 2, 2):
        return {AlignmentInfo((0, 3, 3), None, None, None), AlignmentInfo((0, 4, 4), None, None, None)}
    return set()

def prob_t_a_given_s_mock(a):
    prob_values = {(0, 3, 2): 0.5, (0, 2, 2): 0.6, (0, 1, 1): 0.4, (0, 3, 3): 0.6, (0, 4, 4): 0.7}
    return prob_values.get(a.alignment, 0.01)
ibm_model = IBMModel([])
ibm_model.neighboring = neighboring_mock
ibm_model.prob_t_a_given_s = prob_t_a_given_s_mock
best_alignment = ibm_model.hillclimb(initial_alignment)
self.assertEqual(best_alignment.alignment, (0, 4, 4))
```

## Next Steps


---

*Source: test_ibm_model.py:220 | Complexity: Intermediate | Last updated: 2026-06-02*