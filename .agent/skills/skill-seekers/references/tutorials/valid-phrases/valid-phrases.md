# How To: Valid Phrases

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test valid phrases

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
hypothesis.untranslated_spans = lambda _: [(0, 2), (3, 6)]
```

### Step 3: Assign all_phrases_from = value

```python
all_phrases_from = [[1, 4], [2], [], [5], [5, 6, 7], [], [7]]
```

### Step 4: Assign phrase_spans = StackDecoder.valid_phrases(...)

```python
phrase_spans = StackDecoder.valid_phrases(all_phrases_from, hypothesis)
```

### Step 5: Call self.assertEqual()

```python
self.assertEqual(phrase_spans, [(0, 1), (1, 2), (3, 5), (4, 5), (4, 6)])
```


## Complete Example

```python
# Workflow
hypothesis = _Hypothesis()
hypothesis.untranslated_spans = lambda _: [(0, 2), (3, 6)]
all_phrases_from = [[1, 4], [2], [], [5], [5, 6, 7], [], [7]]
phrase_spans = StackDecoder.valid_phrases(all_phrases_from, hypothesis)
self.assertEqual(phrase_spans, [(0, 1), (1, 2), (3, 5), (4, 5), (4, 6)])
```

## Next Steps


---

*Source: test_stack_decoder.py:122 | Complexity: Intermediate | Last updated: 2026-06-02*