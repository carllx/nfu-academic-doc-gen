# How To: Corpus Bleu With Multiple Weights

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test corpus bleu with multiple weights

## Prerequisites

**Required Modules:**
- `unittest`
- `numpy`
- `nltk.data`
- `nltk.translate.bleu_score`


## Step-by-Step Guide

### Step 1: Assign hyp1 = value

```python
hyp1 = ['It', 'is', 'a', 'guide', 'to', 'action', 'which', 'ensures', 'that', 'the', 'military', 'always', 'obeys', 'the', 'commands', 'of', 'the', 'party']
```

**Verification:**
```python
assert bleu_scores[0] == corpus_bleu([[ref1a, ref1b, ref1c], [ref2a]], [hyp1, hyp2], weight_1)
```

### Step 2: Assign ref1a = value

```python
ref1a = ['It', 'is', 'a', 'guide', 'to', 'action', 'that', 'ensures', 'that', 'the', 'military', 'will', 'forever', 'heed', 'Party', 'commands']
```

**Verification:**
```python
assert bleu_scores[1] == corpus_bleu([[ref1a, ref1b, ref1c], [ref2a]], [hyp1, hyp2], weight_2)
```

### Step 3: Assign ref1b = value

```python
ref1b = ['It', 'is', 'the', 'guiding', 'principle', 'which', 'guarantees', 'the', 'military', 'forces', 'always', 'being', 'under', 'the', 'command', 'of', 'the', 'Party']
```

**Verification:**
```python
assert bleu_scores[2] == corpus_bleu([[ref1a, ref1b, ref1c], [ref2a]], [hyp1, hyp2], weight_3)
```

### Step 4: Assign ref1c = value

```python
ref1c = ['It', 'is', 'the', 'practical', 'guide', 'for', 'the', 'army', 'always', 'to', 'heed', 'the', 'directions', 'of', 'the', 'party']
```

### Step 5: Assign hyp2 = value

```python
hyp2 = ['he', 'read', 'the', 'book', 'because', 'he', 'was', 'interested', 'in', 'world', 'history']
```

### Step 6: Assign ref2a = value

```python
ref2a = ['he', 'was', 'interested', 'in', 'world', 'history', 'because', 'he', 'read', 'the', 'book']
```

### Step 7: Assign weight_1 = value

```python
weight_1 = (1, 0, 0, 0)
```

### Step 8: Assign weight_2 = value

```python
weight_2 = (0.25, 0.25, 0.25, 0.25)
```

### Step 9: Assign weight_3 = value

```python
weight_3 = (0, 0, 0, 0, 1)
```

### Step 10: Assign bleu_scores = corpus_bleu(...)

```python
bleu_scores = corpus_bleu(list_of_references=[[ref1a, ref1b, ref1c], [ref2a]], hypotheses=[hyp1, hyp2], weights=[weight_1, weight_2, weight_3])
```

**Verification:**
```python
assert bleu_scores[0] == corpus_bleu([[ref1a, ref1b, ref1c], [ref2a]], [hyp1, hyp2], weight_1)
```


## Complete Example

```python
# Workflow
hyp1 = ['It', 'is', 'a', 'guide', 'to', 'action', 'which', 'ensures', 'that', 'the', 'military', 'always', 'obeys', 'the', 'commands', 'of', 'the', 'party']
ref1a = ['It', 'is', 'a', 'guide', 'to', 'action', 'that', 'ensures', 'that', 'the', 'military', 'will', 'forever', 'heed', 'Party', 'commands']
ref1b = ['It', 'is', 'the', 'guiding', 'principle', 'which', 'guarantees', 'the', 'military', 'forces', 'always', 'being', 'under', 'the', 'command', 'of', 'the', 'Party']
ref1c = ['It', 'is', 'the', 'practical', 'guide', 'for', 'the', 'army', 'always', 'to', 'heed', 'the', 'directions', 'of', 'the', 'party']
hyp2 = ['he', 'read', 'the', 'book', 'because', 'he', 'was', 'interested', 'in', 'world', 'history']
ref2a = ['he', 'was', 'interested', 'in', 'world', 'history', 'because', 'he', 'read', 'the', 'book']
weight_1 = (1, 0, 0, 0)
weight_2 = (0.25, 0.25, 0.25, 0.25)
weight_3 = (0, 0, 0, 0, 1)
bleu_scores = corpus_bleu(list_of_references=[[ref1a, ref1b, ref1c], [ref2a]], hypotheses=[hyp1, hyp2], weights=[weight_1, weight_2, weight_3])
assert bleu_scores[0] == corpus_bleu([[ref1a, ref1b, ref1c], [ref2a]], [hyp1, hyp2], weight_1)
assert bleu_scores[1] == corpus_bleu([[ref1a, ref1b, ref1c], [ref2a]], [hyp1, hyp2], weight_2)
assert bleu_scores[2] == corpus_bleu([[ref1a, ref1b, ref1c], [ref2a]], [hyp1, hyp2], weight_3)
```

## Next Steps


---

*Source: test_bleu.py:296 | Complexity: Advanced | Last updated: 2026-06-02*