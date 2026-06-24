# How To: Ribes One Worder

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test ribes one worder

## Prerequisites

**Required Modules:**
- `nltk.translate.ribes_score`


## Step-by-Step Guide

### Step 1: Assign hyp = unknown.split(...)

```python
hyp = 'This is a nice sentence which I quite like'.split()
```

**Verification:**
```python
assert word_rank_alignment(ref, hyp) == [3]
```

### Step 2: Assign ref = unknown.split(...)

```python
ref = "Okay well that's nice and all but the reference's different".split()
```

**Verification:**
```python
assert corpus_ribes(list_of_refs, hypotheses) == 0.0
```

### Step 3: Assign list_of_refs = value

```python
list_of_refs = [[ref]]
```

### Step 4: Assign hypotheses = value

```python
hypotheses = [hyp]
```

**Verification:**
```python
assert corpus_ribes(list_of_refs, hypotheses) == 0.0
```


## Complete Example

```python
# Workflow
hyp = 'This is a nice sentence which I quite like'.split()
ref = "Okay well that's nice and all but the reference's different".split()
assert word_rank_alignment(ref, hyp) == [3]
list_of_refs = [[ref]]
hypotheses = [hyp]
assert corpus_ribes(list_of_refs, hypotheses) == 0.0
```

## Next Steps


---

*Source: test_ribes.py:17 | Complexity: Intermediate | Last updated: 2026-06-02*