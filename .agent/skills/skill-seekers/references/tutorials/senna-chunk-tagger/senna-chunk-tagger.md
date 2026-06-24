# How To: Senna Chunk Tagger

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test senna chunk tagger

## Prerequisites

**Required Modules:**
- `unittest`
- `os`
- `nltk.classify`
- `nltk.tag`


## Step-by-Step Guide

### Step 1: Assign chktagger = SennaChunkTagger(...)

```python
chktagger = SennaChunkTagger(SENNA_EXECUTABLE_PATH)
```

### Step 2: Assign result_1 = chktagger.tag(...)

```python
result_1 = chktagger.tag('What is the airspeed of an unladen swallow ?'.split())
```

### Step 3: Assign expected_1 = value

```python
expected_1 = [('What', 'B-NP'), ('is', 'B-VP'), ('the', 'B-NP'), ('airspeed', 'I-NP'), ('of', 'B-PP'), ('an', 'B-NP'), ('unladen', 'I-NP'), ('swallow', 'I-NP'), ('?', 'O')]
```

### Step 4: Assign result_2 = list(...)

```python
result_2 = list(chktagger.bio_to_chunks(result_1, chunk_type='NP'))
```

### Step 5: Assign expected_2 = value

```python
expected_2 = [('What', '0'), ('the airspeed', '2-3'), ('an unladen swallow', '5-6-7')]
```

### Step 6: Call self.assertEqual()

```python
self.assertEqual(result_1, expected_1)
```

### Step 7: Call self.assertEqual()

```python
self.assertEqual(result_2, expected_2)
```


## Complete Example

```python
# Workflow
chktagger = SennaChunkTagger(SENNA_EXECUTABLE_PATH)
result_1 = chktagger.tag('What is the airspeed of an unladen swallow ?'.split())
expected_1 = [('What', 'B-NP'), ('is', 'B-VP'), ('the', 'B-NP'), ('airspeed', 'I-NP'), ('of', 'B-PP'), ('an', 'B-NP'), ('unladen', 'I-NP'), ('swallow', 'I-NP'), ('?', 'O')]
result_2 = list(chktagger.bio_to_chunks(result_1, chunk_type='NP'))
expected_2 = [('What', '0'), ('the airspeed', '2-3'), ('an unladen swallow', '5-6-7')]
self.assertEqual(result_1, expected_1)
self.assertEqual(result_2, expected_2)
```

## Next Steps


---

*Source: test_senna.py:64 | Complexity: Intermediate | Last updated: 2026-06-02*