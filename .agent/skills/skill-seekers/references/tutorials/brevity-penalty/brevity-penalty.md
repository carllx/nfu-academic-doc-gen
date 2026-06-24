# How To: Brevity Penalty

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test brevity penalty

## Prerequisites

**Required Modules:**
- `unittest`
- `numpy`
- `nltk.data`
- `nltk.translate.bleu_score`


## Step-by-Step Guide

### Step 1: Assign references = value

```python
references = [['a'] * 11, ['a'] * 8]
```

**Verification:**
```python
assert brevity_penalty(closest_ref_len, hyp_len) == 1.0
```

### Step 2: Assign hypothesis = value

```python
hypothesis = ['a'] * 7
```

### Step 3: Assign hyp_len = len(...)

```python
hyp_len = len(hypothesis)
```

### Step 4: Assign closest_ref_len = closest_ref_length(...)

```python
closest_ref_len = closest_ref_length(references, hyp_len)
```

### Step 5: Call self.assertAlmostEqual()

```python
self.assertAlmostEqual(brevity_penalty(closest_ref_len, hyp_len), 0.8669, places=4)
```

### Step 6: Assign references = value

```python
references = [['a'] * 11, ['a'] * 8, ['a'] * 6, ['a'] * 7]
```

### Step 7: Assign hypothesis = value

```python
hypothesis = ['a'] * 7
```

### Step 8: Assign hyp_len = len(...)

```python
hyp_len = len(hypothesis)
```

### Step 9: Assign closest_ref_len = closest_ref_length(...)

```python
closest_ref_len = closest_ref_length(references, hyp_len)
```

**Verification:**
```python
assert brevity_penalty(closest_ref_len, hyp_len) == 1.0
```


## Complete Example

```python
# Workflow
references = [['a'] * 11, ['a'] * 8]
hypothesis = ['a'] * 7
hyp_len = len(hypothesis)
closest_ref_len = closest_ref_length(references, hyp_len)
self.assertAlmostEqual(brevity_penalty(closest_ref_len, hyp_len), 0.8669, places=4)
references = [['a'] * 11, ['a'] * 8, ['a'] * 6, ['a'] * 7]
hypothesis = ['a'] * 7
hyp_len = len(hypothesis)
closest_ref_len = closest_ref_length(references, hyp_len)
assert brevity_penalty(closest_ref_len, hyp_len) == 1.0
```

## Next Steps


---

*Source: test_bleu.py:100 | Complexity: Advanced | Last updated: 2026-06-02*