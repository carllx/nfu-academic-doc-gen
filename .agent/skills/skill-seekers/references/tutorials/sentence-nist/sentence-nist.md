# How To: Sentence Nist

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test sentence nist

## Prerequisites

**Required Modules:**
- `io`
- `unittest`
- `nltk.data`
- `nltk.translate.nist_score`


## Step-by-Step Guide

### Step 1: Assign ref_file = find(...)

```python
ref_file = find('models/wmt15_eval/ref.ru')
```

**Verification:**
```python
assert abs(mteval_nist - nltk_nist) < 0.05
```

### Step 2: Assign hyp_file = find(...)

```python
hyp_file = find('models/wmt15_eval/google.ru')
```

### Step 3: Assign mteval_output_file = find(...)

```python
mteval_output_file = find('models/wmt15_eval/mteval-13a.output')
```

### Step 4: Assign mteval_nist_scores = map(...)

```python
mteval_nist_scores = map(float, mteval_fin.readlines()[-4].split()[1:-1])
```

### Step 5: Assign hypotheses = list(...)

```python
hypotheses = list(map(lambda x: x.split(), hyp_fin))
```

### Step 6: Assign references = list(...)

```python
references = list(map(lambda x: [x.split()], ref_fin))
```

### Step 7: Assign nltk_nist = corpus_nist(...)

```python
nltk_nist = corpus_nist(references, hypotheses, i)
```

**Verification:**
```python
assert abs(mteval_nist - nltk_nist) < 0.05
```


## Complete Example

```python
# Workflow
ref_file = find('models/wmt15_eval/ref.ru')
hyp_file = find('models/wmt15_eval/google.ru')
mteval_output_file = find('models/wmt15_eval/mteval-13a.output')
with open(mteval_output_file) as mteval_fin:
    mteval_nist_scores = map(float, mteval_fin.readlines()[-4].split()[1:-1])
with open(ref_file, encoding='utf8') as ref_fin:
    with open(hyp_file, encoding='utf8') as hyp_fin:
        hypotheses = list(map(lambda x: x.split(), hyp_fin))
        references = list(map(lambda x: [x.split()], ref_fin))
        for i, mteval_nist in zip(range(1, 10), mteval_nist_scores):
            nltk_nist = corpus_nist(references, hypotheses, i)
            assert abs(mteval_nist - nltk_nist) < 0.05
```

## Next Steps


---

*Source: test_nist.py:13 | Complexity: Intermediate | Last updated: 2026-06-02*