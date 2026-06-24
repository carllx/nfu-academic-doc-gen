# How To: Compute Future Costs

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test compute future costs

## Prerequisites

**Required Modules:**
- `unittest`
- `collections`
- `math`
- `nltk.translate`
- `nltk.translate.stack_decoder`


## Step-by-Step Guide

### Step 1: Assign phrase_table = TestStackDecoder.create_fake_phrase_table(...)

```python
phrase_table = TestStackDecoder.create_fake_phrase_table()
```

### Step 2: Assign language_model = TestStackDecoder.create_fake_language_model(...)

```python
language_model = TestStackDecoder.create_fake_language_model()
```

### Step 3: Assign stack_decoder = StackDecoder(...)

```python
stack_decoder = StackDecoder(phrase_table, language_model)
```

### Step 4: Assign sentence = value

```python
sentence = ('my', 'hovercraft', 'is', 'full', 'of', 'eels')
```

### Step 5: Assign future_scores = stack_decoder.compute_future_scores(...)

```python
future_scores = stack_decoder.compute_future_scores(sentence)
```

### Step 6: Call self.assertEqual()

```python
self.assertEqual(future_scores[1][2], phrase_table.translations_for(('hovercraft',))[0].log_prob + language_model.probability(('hovercraft',)))
```

### Step 7: Call self.assertEqual()

```python
self.assertEqual(future_scores[0][2], phrase_table.translations_for(('my', 'hovercraft'))[0].log_prob + language_model.probability(('my', 'hovercraft')))
```


## Complete Example

```python
# Workflow
phrase_table = TestStackDecoder.create_fake_phrase_table()
language_model = TestStackDecoder.create_fake_language_model()
stack_decoder = StackDecoder(phrase_table, language_model)
sentence = ('my', 'hovercraft', 'is', 'full', 'of', 'eels')
future_scores = stack_decoder.compute_future_scores(sentence)
self.assertEqual(future_scores[1][2], phrase_table.translations_for(('hovercraft',))[0].log_prob + language_model.probability(('hovercraft',)))
self.assertEqual(future_scores[0][2], phrase_table.translations_for(('my', 'hovercraft'))[0].log_prob + language_model.probability(('my', 'hovercraft')))
```

## Next Steps


---

*Source: test_stack_decoder.py:65 | Complexity: Intermediate | Last updated: 2026-06-02*