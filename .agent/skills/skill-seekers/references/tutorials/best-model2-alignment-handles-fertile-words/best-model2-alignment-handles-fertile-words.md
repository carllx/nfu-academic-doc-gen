# How To: Best Model2 Alignment Handles Fertile Words

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test best model2 alignment handles fertile words

## Prerequisites

**Required Modules:**
- `unittest`
- `collections`
- `nltk.translate`
- `nltk.translate.ibm_model`


## Step-by-Step Guide

### Step 1: Assign sentence_pair = AlignedSent(...)

```python
sentence_pair = AlignedSent(['i', 'really', ',', 'really', 'love', 'ham'], TestIBMModel.__TEST_SRC_SENTENCE)
```

### Step 2: Assign translation_table = value

```python
translation_table = {'i': {"j'": 0.9, 'aime': 0.05, 'bien': 0.02, 'jambon': 0.03, None: 0}, 'really': {"j'": 0, 'aime': 0, 'bien': 0.9, 'jambon': 0.01, None: 0.09}, ',': {"j'": 0, 'aime': 0, 'bien': 0.3, 'jambon': 0, None: 0.7}, 'love': {"j'": 0.05, 'aime': 0.9, 'bien': 0.01, 'jambon': 0.01, None: 0.03}, 'ham': {"j'": 0, 'aime': 0.01, 'bien': 0, 'jambon': 0.99, None: 0}}
```

### Step 3: Assign alignment_table = defaultdict(...)

```python
alignment_table = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: 0.2))))
```

### Step 4: Assign ibm_model = IBMModel(...)

```python
ibm_model = IBMModel([])
```

### Step 5: Assign ibm_model.translation_table = translation_table

```python
ibm_model.translation_table = translation_table
```

### Step 6: Assign ibm_model.alignment_table = alignment_table

```python
ibm_model.alignment_table = alignment_table
```

### Step 7: Assign a_info = ibm_model.best_model2_alignment(...)

```python
a_info = ibm_model.best_model2_alignment(sentence_pair)
```

### Step 8: Call self.assertEqual()

```python
self.assertEqual(a_info.alignment[1:], (1, 3, 0, 3, 2, 4))
```

### Step 9: Call self.assertEqual()

```python
self.assertEqual(a_info.cepts, [[3], [1], [5], [2, 4], [6]])
```


## Complete Example

```python
# Workflow
sentence_pair = AlignedSent(['i', 'really', ',', 'really', 'love', 'ham'], TestIBMModel.__TEST_SRC_SENTENCE)
translation_table = {'i': {"j'": 0.9, 'aime': 0.05, 'bien': 0.02, 'jambon': 0.03, None: 0}, 'really': {"j'": 0, 'aime': 0, 'bien': 0.9, 'jambon': 0.01, None: 0.09}, ',': {"j'": 0, 'aime': 0, 'bien': 0.3, 'jambon': 0, None: 0.7}, 'love': {"j'": 0.05, 'aime': 0.9, 'bien': 0.01, 'jambon': 0.01, None: 0.03}, 'ham': {"j'": 0, 'aime': 0.01, 'bien': 0, 'jambon': 0.99, None: 0}}
alignment_table = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: 0.2))))
ibm_model = IBMModel([])
ibm_model.translation_table = translation_table
ibm_model.alignment_table = alignment_table
a_info = ibm_model.best_model2_alignment(sentence_pair)
self.assertEqual(a_info.alignment[1:], (1, 3, 0, 3, 2, 4))
self.assertEqual(a_info.cepts, [[3], [1], [5], [2, 4], [6]])
```

## Next Steps


---

*Source: test_ibm_model.py:84 | Complexity: Advanced | Last updated: 2026-06-02*