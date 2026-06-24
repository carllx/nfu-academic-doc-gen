# How To: Corpus Bleu

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test corpus bleu

## Prerequisites

**Required Modules:**
- `unittest`
- `numpy`
- `nltk.data`
- `nltk.translate.bleu_score`


## Step-by-Step Guide

### Step 1: Assign ref_file = find(...)

```python
ref_file = find('models/wmt15_eval/ref.ru')
```

**Verification:**
```python
assert abs(mteval_bleu - nltk_bleu) < 0.005
```

### Step 2: Assign hyp_file = find(...)

```python
hyp_file = find('models/wmt15_eval/google.ru')
```

**Verification:**
```python
assert abs(mteval_bleu - nltk_bleu) < 0.005
```

### Step 3: Assign mteval_output_file = find(...)

```python
mteval_output_file = find('models/wmt15_eval/mteval-13a.output')
```

### Step 4: Assign mteval_bleu_scores = map(...)

```python
mteval_bleu_scores = map(float, mteval_fin.readlines()[-2].split()[1:-1])
```

### Step 5: Assign hypothesis = list(...)

```python
hypothesis = list(map(lambda x: x.split(), hyp_fin))
```

### Step 6: Assign references = list(...)

```python
references = list(map(lambda x: [x.split()], ref_fin))
```

### Step 7: Assign chencherry = SmoothingFunction(...)

```python
chencherry = SmoothingFunction()
```

### Step 8: Assign nltk_bleu = corpus_bleu(...)

```python
nltk_bleu = corpus_bleu(references, hypothesis, weights=(1.0 / i,) * i)
```

**Verification:**
```python
assert abs(mteval_bleu - nltk_bleu) < 0.005
```

### Step 9: Assign nltk_bleu = corpus_bleu(...)

```python
nltk_bleu = corpus_bleu(references, hypothesis, weights=(1.0 / i,) * i, smoothing_function=chencherry.method3)
```

**Verification:**
```python
assert abs(mteval_bleu - nltk_bleu) < 0.005
```


## Complete Example

```python
# Workflow
ref_file = find('models/wmt15_eval/ref.ru')
hyp_file = find('models/wmt15_eval/google.ru')
mteval_output_file = find('models/wmt15_eval/mteval-13a.output')
with open(mteval_output_file) as mteval_fin:
    mteval_bleu_scores = map(float, mteval_fin.readlines()[-2].split()[1:-1])
with open(ref_file, encoding='utf8') as ref_fin:
    with open(hyp_file, encoding='utf8') as hyp_fin:
        hypothesis = list(map(lambda x: x.split(), hyp_fin))
        references = list(map(lambda x: [x.split()], ref_fin))
        for i, mteval_bleu in zip(range(1, 10), mteval_bleu_scores):
            nltk_bleu = corpus_bleu(references, hypothesis, weights=(1.0 / i,) * i)
            assert abs(mteval_bleu - nltk_bleu) < 0.005
        chencherry = SmoothingFunction()
        for i, mteval_bleu in zip(range(1, 10), mteval_bleu_scores):
            nltk_bleu = corpus_bleu(references, hypothesis, weights=(1.0 / i,) * i, smoothing_function=chencherry.method3)
            assert abs(mteval_bleu - nltk_bleu) < 0.005
```

## Next Steps


---

*Source: test_bleu.py:231 | Complexity: Advanced | Last updated: 2026-06-02*