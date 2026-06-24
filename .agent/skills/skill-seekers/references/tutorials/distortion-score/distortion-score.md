# How To: Distortion Score

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test distortion score

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

### Step 4: Assign hypothesis.src_phrase_span = value

```python
hypothesis.src_phrase_span = (3, 5)
```

### Step 5: Assign score = stack_decoder.distortion_score(...)

```python
score = stack_decoder.distortion_score(hypothesis, (8, 10))
```

### Step 6: Assign expected_score = value

```python
expected_score = log(stack_decoder.distortion_factor) * (8 - 5)
```

### Step 7: Call self.assertEqual()

```python
self.assertEqual(score, expected_score)
```


## Complete Example

```python
# Workflow
stack_decoder = StackDecoder(None, None)
stack_decoder.distortion_factor = 0.5
hypothesis = _Hypothesis()
hypothesis.src_phrase_span = (3, 5)
score = stack_decoder.distortion_score(hypothesis, (8, 10))
expected_score = log(stack_decoder.distortion_factor) * (8 - 5)
self.assertEqual(score, expected_score)
```

## Next Steps


---

*Source: test_stack_decoder.py:38 | Complexity: Intermediate | Last updated: 2026-06-02*