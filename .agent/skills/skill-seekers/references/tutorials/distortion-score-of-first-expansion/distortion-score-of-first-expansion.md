# How To: Distortion Score Of First Expansion

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test distortion score of first expansion

## Prerequisites

**Required Modules:**
- `unittest`
- `collections`
- `math`
- `nltk.translate`
- `nltk.translate.stack_decoder`


## Step-by-Step Guide

### Step 1: Assign stack_decoder = StackDecoder(...)

```python
stack_decoder = StackDecoder(None, None)
```

### Step 2: Assign stack_decoder.distortion_factor = 0.5

```python
stack_decoder.distortion_factor = 0.5
```

### Step 3: Assign hypothesis = _Hypothesis(...)

```python
hypothesis = _Hypothesis()
```

### Step 4: Assign score = stack_decoder.distortion_score(...)

```python
score = stack_decoder.distortion_score(hypothesis, (8, 10))
```

### Step 5: Call self.assertEqual()

```python
self.assertEqual(score, 0.0)
```


## Complete Example

```python
# Workflow
stack_decoder = StackDecoder(None, None)
stack_decoder.distortion_factor = 0.5
hypothesis = _Hypothesis()
score = stack_decoder.distortion_score(hypothesis, (8, 10))
self.assertEqual(score, 0.0)
```

## Next Steps


---

*Source: test_stack_decoder.py:52 | Complexity: Intermediate | Last updated: 2026-06-02*