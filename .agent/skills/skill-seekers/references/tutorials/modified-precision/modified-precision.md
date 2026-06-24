# How To: Modified Precision

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: Examples from the original BLEU paper
https://www.aclweb.org/anthology/P02-1040.pdf

## Prerequisites

**Required Modules:**
- `unittest`
- `numpy`
- `nltk.data`
- `nltk.translate.bleu_score`


## Step-by-Step Guide

### Step 1: '\n        Examples from the original BLEU paper\n        https://www.aclweb.org/anthology/P02-1040.pdf\n        '

```python
'\n        Examples from the original BLEU paper\n        https://www.aclweb.org/anthology/P02-1040.pdf\n        '
```

**Verification:**
```python
assert round(hyp1_unigram_precision, 4) == 0.2857
```

### Step 2: Assign ref1 = unknown.split(...)

```python
ref1 = 'the cat is on the mat'.split()
```

**Verification:**
```python
assert float(modified_precision(references, hyp1, n=2)) == 0.0
```

### Step 3: Assign ref2 = unknown.split(...)

```python
ref2 = 'there is a cat on the mat'.split()
```

**Verification:**
```python
assert float(modified_precision(references, hyp1, n=1)) == 1.0
```

### Step 4: Assign hyp1 = unknown.split(...)

```python
hyp1 = 'the the the the the the the'.split()
```

**Verification:**
```python
assert float(modified_precision(references, hyp1, n=2)) == 1.0
```

### Step 5: Assign references = value

```python
references = [ref1, ref2]
```

**Verification:**
```python
assert round(hyp1_unigram_precision, 4) == 0.9444
```

### Step 6: Assign hyp1_unigram_precision = float(...)

```python
hyp1_unigram_precision = float(modified_precision(references, hyp1, n=1))
```

**Verification:**
```python
assert round(hyp2_unigram_precision, 4) == 0.5714
```

### Step 7: Call self.assertAlmostEqual()

```python
self.assertAlmostEqual(hyp1_unigram_precision, 0.28571428, places=4)
```

**Verification:**
```python
assert round(hyp1_bigram_precision, 4) == 0.5882
```

### Step 8: Assign ref1 = str.split(...)

```python
ref1 = str('It is a guide to action that ensures that the military will forever heed Party commands').split()
```

**Verification:**
```python
assert round(hyp2_bigram_precision, 4) == 0.0769
```

### Step 9: Assign ref2 = str.split(...)

```python
ref2 = str('It is the guiding principle which guarantees the military forces always being under the command of the Party').split()
```

### Step 10: Assign ref3 = str.split(...)

```python
ref3 = str('It is the practical guide for the army always to heed the directions of the party').split()
```

### Step 11: Assign hyp1 = unknown.split(...)

```python
hyp1 = 'of the'.split()
```

### Step 12: Assign references = value

```python
references = [ref1, ref2, ref3]
```

**Verification:**
```python
assert float(modified_precision(references, hyp1, n=1)) == 1.0
```

### Step 13: Assign hyp1 = str.split(...)

```python
hyp1 = str('It is a guide to action which ensures that the military always obeys the commands of the party').split()
```

### Step 14: Assign hyp2 = str.split(...)

```python
hyp2 = str('It is to insure the troops forever hearing the activity guidebook that party direct').split()
```

### Step 15: Assign references = value

```python
references = [ref1, ref2, ref3]
```

### Step 16: Assign hyp1_unigram_precision = float(...)

```python
hyp1_unigram_precision = float(modified_precision(references, hyp1, n=1))
```

### Step 17: Assign hyp2_unigram_precision = float(...)

```python
hyp2_unigram_precision = float(modified_precision(references, hyp2, n=1))
```

### Step 18: Call self.assertAlmostEqual()

```python
self.assertAlmostEqual(hyp1_unigram_precision, 0.94444444, places=4)
```

### Step 19: Call self.assertAlmostEqual()

```python
self.assertAlmostEqual(hyp2_unigram_precision, 0.57142857, places=4)
```

**Verification:**
```python
assert round(hyp1_unigram_precision, 4) == 0.9444
```

### Step 20: Assign hyp1_bigram_precision = float(...)

```python
hyp1_bigram_precision = float(modified_precision(references, hyp1, n=2))
```

### Step 21: Assign hyp2_bigram_precision = float(...)

```python
hyp2_bigram_precision = float(modified_precision(references, hyp2, n=2))
```

### Step 22: Call self.assertAlmostEqual()

```python
self.assertAlmostEqual(hyp1_bigram_precision, 0.58823529, places=4)
```

### Step 23: Call self.assertAlmostEqual()

```python
self.assertAlmostEqual(hyp2_bigram_precision, 0.07692307, places=4)
```

**Verification:**
```python
assert round(hyp1_bigram_precision, 4) == 0.5882
```


## Complete Example

```python
# Workflow
'\n        Examples from the original BLEU paper\n        https://www.aclweb.org/anthology/P02-1040.pdf\n        '
ref1 = 'the cat is on the mat'.split()
ref2 = 'there is a cat on the mat'.split()
hyp1 = 'the the the the the the the'.split()
references = [ref1, ref2]
hyp1_unigram_precision = float(modified_precision(references, hyp1, n=1))
assert round(hyp1_unigram_precision, 4) == 0.2857
self.assertAlmostEqual(hyp1_unigram_precision, 0.28571428, places=4)
assert float(modified_precision(references, hyp1, n=2)) == 0.0
ref1 = str('It is a guide to action that ensures that the military will forever heed Party commands').split()
ref2 = str('It is the guiding principle which guarantees the military forces always being under the command of the Party').split()
ref3 = str('It is the practical guide for the army always to heed the directions of the party').split()
hyp1 = 'of the'.split()
references = [ref1, ref2, ref3]
assert float(modified_precision(references, hyp1, n=1)) == 1.0
assert float(modified_precision(references, hyp1, n=2)) == 1.0
hyp1 = str('It is a guide to action which ensures that the military always obeys the commands of the party').split()
hyp2 = str('It is to insure the troops forever hearing the activity guidebook that party direct').split()
references = [ref1, ref2, ref3]
hyp1_unigram_precision = float(modified_precision(references, hyp1, n=1))
hyp2_unigram_precision = float(modified_precision(references, hyp2, n=1))
self.assertAlmostEqual(hyp1_unigram_precision, 0.94444444, places=4)
self.assertAlmostEqual(hyp2_unigram_precision, 0.57142857, places=4)
assert round(hyp1_unigram_precision, 4) == 0.9444
assert round(hyp2_unigram_precision, 4) == 0.5714
hyp1_bigram_precision = float(modified_precision(references, hyp1, n=2))
hyp2_bigram_precision = float(modified_precision(references, hyp2, n=2))
self.assertAlmostEqual(hyp1_bigram_precision, 0.58823529, places=4)
self.assertAlmostEqual(hyp2_bigram_precision, 0.07692307, places=4)
assert round(hyp1_bigram_precision, 4) == 0.5882
assert round(hyp2_bigram_precision, 4) == 0.0769
```

## Next Steps


---

*Source: test_bleu.py:21 | Complexity: Advanced | Last updated: 2026-06-02*