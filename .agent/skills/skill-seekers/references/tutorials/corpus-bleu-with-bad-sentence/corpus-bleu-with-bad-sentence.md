# How To: Corpus Bleu With Bad Sentence

**Difficulty**: Advanced
**Estimated Time**: 10 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test corpus bleu with bad sentence

## Prerequisites

**Required Modules:**
- `unittest`
- `numpy`
- `nltk.data`
- `nltk.translate.bleu_score`


## Step-by-Step Guide

### Step 1: Assign hyp = 'Teo S yb , oe uNb , R , T t , , t Tue Ar saln S , , 5istsi l , 5oe R ulO sae oR R'

```python
hyp = 'Teo S yb , oe uNb , R , T t , , t Tue Ar saln S , , 5istsi l , 5oe R ulO sae oR R'
```

### Step 2: Assign ref = str(...)

```python
ref = str('Their tasks include changing a pump on the faulty stokehold .Likewise , two species that are very similar in morphology were distinguished using genetics .')
```

### Step 3: Assign references = value

```python
references = [[ref.split()]]
```

### Step 4: Assign hypotheses = value

```python
hypotheses = [hyp.split()]
```

### Step 5: Call self.assertAlmostEqual()

```python
self.assertAlmostEqual(corpus_bleu(references, hypotheses), 0.0, places=4)
```

### Step 6: Call self.assertAlmostEqual()

```python
self.assertAlmostEqual(corpus_bleu(references, hypotheses), 0.0, places=4)
```


## Complete Example

```python
# Workflow
hyp = 'Teo S yb , oe uNb , R , T t , , t Tue Ar saln S , , 5istsi l , 5oe R ulO sae oR R'
ref = str('Their tasks include changing a pump on the faulty stokehold .Likewise , two species that are very similar in morphology were distinguished using genetics .')
references = [[ref.split()]]
hypotheses = [hyp.split()]
try:
    with self.assertWarns(UserWarning):
        self.assertAlmostEqual(corpus_bleu(references, hypotheses), 0.0, places=4)
except AttributeError:
    self.assertAlmostEqual(corpus_bleu(references, hypotheses), 0.0, places=4)
```

## Next Steps


---

*Source: test_bleu.py:274 | Complexity: Advanced | Last updated: 2026-06-02*