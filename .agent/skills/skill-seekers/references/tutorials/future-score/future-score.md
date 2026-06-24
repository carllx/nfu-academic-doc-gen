# How To: Future Score

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test future score

## Prerequisites

**Required Modules:**
- `unittest`
- `collections`
- `math`
- `nltk.translate`
- `nltk.translate.stack_decoder`


## Step-by-Step Guide

### Step 1: Assign hypothesis = _Hypothesis(...)

```python
hypothesis = _Hypothesis()
```

### Step 2: Assign hypothesis.untranslated_spans = value

```python
hypothesis.untranslated_spans = lambda _: [(0, 2), (5, 8)]
```

### Step 3: Assign future_score_table = defaultdict(...)

```python
future_score_table = defaultdict(lambda: defaultdict(float))
```

### Step 4: Assign unknown = 0.4

```python
future_score_table[0][2] = 0.4
```

### Step 5: Assign unknown = 0.5

```python
future_score_table[5][8] = 0.5
```

### Step 6: Assign stack_decoder = StackDecoder(...)

```python
stack_decoder = StackDecoder(None, None)
```

### Step 7: Assign future_score = stack_decoder.future_score(...)

```python
future_score = stack_decoder.future_score(hypothesis, future_score_table, 8)
```

### Step 8: Call self.assertEqual()

```python
self.assertEqual(future_score, 0.4 + 0.5)
```


## Complete Example

```python
# Workflow
hypothesis = _Hypothesis()
hypothesis.untranslated_spans = lambda _: [(0, 2), (5, 8)]
future_score_table = defaultdict(lambda: defaultdict(float))
future_score_table[0][2] = 0.4
future_score_table[5][8] = 0.5
stack_decoder = StackDecoder(None, None)
future_score = stack_decoder.future_score(hypothesis, future_score_table, 8)
self.assertEqual(future_score, 0.4 + 0.5)
```

## Next Steps


---

*Source: test_stack_decoder.py:107 | Complexity: Advanced | Last updated: 2026-06-02*