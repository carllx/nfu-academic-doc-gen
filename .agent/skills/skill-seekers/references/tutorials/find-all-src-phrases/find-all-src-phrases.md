# How To: Find All Src Phrases

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test find all src phrases

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

### Step 2: Assign stack_decoder = StackDecoder(...)

```python
stack_decoder = StackDecoder(phrase_table, None)
```

### Step 3: Assign sentence = value

```python
sentence = ('my', 'hovercraft', 'is', 'full', 'of', 'eels')
```

### Step 4: Assign src_phrase_spans = stack_decoder.find_all_src_phrases(...)

```python
src_phrase_spans = stack_decoder.find_all_src_phrases(sentence)
```

### Step 5: Call self.assertEqual()

```python
self.assertEqual(src_phrase_spans[0], [2])
```

### Step 6: Call self.assertEqual()

```python
self.assertEqual(src_phrase_spans[1], [2])
```

### Step 7: Call self.assertEqual()

```python
self.assertEqual(src_phrase_spans[2], [3])
```

### Step 8: Call self.assertEqual()

```python
self.assertEqual(src_phrase_spans[3], [5, 6])
```

### Step 9: Call self.assertFalse()

```python
self.assertFalse(src_phrase_spans[4])
```

### Step 10: Call self.assertEqual()

```python
self.assertEqual(src_phrase_spans[5], [6])
```


## Complete Example

```python
# Workflow
phrase_table = TestStackDecoder.create_fake_phrase_table()
stack_decoder = StackDecoder(phrase_table, None)
sentence = ('my', 'hovercraft', 'is', 'full', 'of', 'eels')
src_phrase_spans = stack_decoder.find_all_src_phrases(sentence)
self.assertEqual(src_phrase_spans[0], [2])
self.assertEqual(src_phrase_spans[1], [2])
self.assertEqual(src_phrase_spans[2], [3])
self.assertEqual(src_phrase_spans[3], [5, 6])
self.assertFalse(src_phrase_spans[4])
self.assertEqual(src_phrase_spans[5], [6])
```

## Next Steps


---

*Source: test_stack_decoder.py:21 | Complexity: Advanced | Last updated: 2026-06-02*