# How To: Prune

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test prune

## Prerequisites

**Required Modules:**
- `unittest`
- `collections`
- `nltk.translate`
- `nltk.translate.ibm_model`


## Step-by-Step Guide

### Step 1: Assign alignment_infos = value

```python
alignment_infos = [AlignmentInfo((1, 1), None, None, None), AlignmentInfo((1, 2), None, None, None), AlignmentInfo((2, 1), None, None, None), AlignmentInfo((2, 2), None, None, None), AlignmentInfo((0, 0), None, None, None)]
```

### Step 2: Assign min_factor = value

```python
min_factor = IBMModel5.MIN_SCORE_FACTOR
```

### Step 3: Assign best_score = 0.9

```python
best_score = 0.9
```

### Step 4: Assign scores = value

```python
scores = {(1, 1): min(min_factor * 1.5, 1) * best_score, (1, 2): best_score, (2, 1): min_factor * best_score, (2, 2): min_factor * best_score * 0.5, (0, 0): min(min_factor * 1.1, 1) * 1.2}
```

### Step 5: Assign corpus = value

```python
corpus = [AlignedSent(['a'], ['b'])]
```

### Step 6: Assign original_prob_function = value

```python
original_prob_function = IBMModel4.model4_prob_t_a_given_s
```

### Step 7: Assign IBMModel4.model4_prob_t_a_given_s = staticmethod(...)

```python
IBMModel4.model4_prob_t_a_given_s = staticmethod(lambda a, model: scores[a.alignment])
```

### Step 8: Assign model5 = IBMModel5(...)

```python
model5 = IBMModel5(corpus, 0, None, None)
```

### Step 9: Assign pruned_alignments = model5.prune(...)

```python
pruned_alignments = model5.prune(alignment_infos)
```

### Step 10: Call self.assertEqual()

```python
self.assertEqual(len(pruned_alignments), 3)
```

### Step 11: Assign IBMModel4.model4_prob_t_a_given_s = original_prob_function

```python
IBMModel4.model4_prob_t_a_given_s = original_prob_function
```


## Complete Example

```python
# Workflow
alignment_infos = [AlignmentInfo((1, 1), None, None, None), AlignmentInfo((1, 2), None, None, None), AlignmentInfo((2, 1), None, None, None), AlignmentInfo((2, 2), None, None, None), AlignmentInfo((0, 0), None, None, None)]
min_factor = IBMModel5.MIN_SCORE_FACTOR
best_score = 0.9
scores = {(1, 1): min(min_factor * 1.5, 1) * best_score, (1, 2): best_score, (2, 1): min_factor * best_score, (2, 2): min_factor * best_score * 0.5, (0, 0): min(min_factor * 1.1, 1) * 1.2}
corpus = [AlignedSent(['a'], ['b'])]
original_prob_function = IBMModel4.model4_prob_t_a_given_s
IBMModel4.model4_prob_t_a_given_s = staticmethod(lambda a, model: scores[a.alignment])
model5 = IBMModel5(corpus, 0, None, None)
pruned_alignments = model5.prune(alignment_infos)
self.assertEqual(len(pruned_alignments), 3)
IBMModel4.model4_prob_t_a_given_s = original_prob_function
```

## Next Steps


---

*Source: test_ibm5.py:127 | Complexity: Advanced | Last updated: 2026-06-02*