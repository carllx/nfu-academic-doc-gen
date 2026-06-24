# How To: Sample

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test sample

## Prerequisites

**Required Modules:**
- `unittest`
- `collections`
- `nltk.translate`
- `nltk.translate.ibm_model`


## Step-by-Step Guide

### Step 1: Assign sentence_pair = AlignedSent(...)

```python
sentence_pair = AlignedSent(TestIBMModel.__TEST_TRG_SENTENCE, TestIBMModel.__TEST_SRC_SENTENCE)
```

### Step 2: Assign ibm_model = IBMModel(...)

```python
ibm_model = IBMModel([])
```

### Step 3: Assign ibm_model.prob_t_a_given_s = value

```python
ibm_model.prob_t_a_given_s = lambda x: 0.001
```

### Step 4: Assign unknown = ibm_model.sample(...)

```python
samples, best_alignment = ibm_model.sample(sentence_pair)
```

### Step 5: Call self.assertEqual()

```python
self.assertEqual(len(samples), 61)
```


## Complete Example

```python
# Workflow
sentence_pair = AlignedSent(TestIBMModel.__TEST_TRG_SENTENCE, TestIBMModel.__TEST_SRC_SENTENCE)
ibm_model = IBMModel([])
ibm_model.prob_t_a_given_s = lambda x: 0.001
samples, best_alignment = ibm_model.sample(sentence_pair)
self.assertEqual(len(samples), 61)
```

## Next Steps


---

*Source: test_ibm_model.py:257 | Complexity: Intermediate | Last updated: 2026-06-02*