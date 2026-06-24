# How To: Senna Pipeline

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: Senna pipeline interface

## Prerequisites

**Required Modules:**
- `unittest`
- `os`
- `nltk.classify`
- `nltk.tag`


## Step-by-Step Guide

### Step 1: 'Senna pipeline interface'

```python
'Senna pipeline interface'
```

### Step 2: Assign pipeline = Senna(...)

```python
pipeline = Senna(SENNA_EXECUTABLE_PATH, ['pos', 'chk', 'ner'])
```

### Step 3: Assign sent = unknown.split(...)

```python
sent = 'Dusseldorf is an international business center'.split()
```

### Step 4: Assign result = value

```python
result = [(token['word'], token['chk'], token['ner'], token['pos']) for token in pipeline.tag(sent)]
```

### Step 5: Assign expected = value

```python
expected = [('Dusseldorf', 'B-NP', 'B-LOC', 'NNP'), ('is', 'B-VP', 'O', 'VBZ'), ('an', 'B-NP', 'O', 'DT'), ('international', 'I-NP', 'O', 'JJ'), ('business', 'I-NP', 'O', 'NN'), ('center', 'I-NP', 'O', 'NN')]
```

### Step 6: Call self.assertEqual()

```python
self.assertEqual(result, expected)
```


## Complete Example

```python
# Workflow
'Senna pipeline interface'
pipeline = Senna(SENNA_EXECUTABLE_PATH, ['pos', 'chk', 'ner'])
sent = 'Dusseldorf is an international business center'.split()
result = [(token['word'], token['chk'], token['ner'], token['pos']) for token in pipeline.tag(sent)]
expected = [('Dusseldorf', 'B-NP', 'B-LOC', 'NNP'), ('is', 'B-VP', 'O', 'VBZ'), ('an', 'B-NP', 'O', 'DT'), ('international', 'I-NP', 'O', 'JJ'), ('business', 'I-NP', 'O', 'NN'), ('center', 'I-NP', 'O', 'NN')]
self.assertEqual(result, expected)
```

## Next Steps


---

*Source: test_senna.py:24 | Complexity: Intermediate | Last updated: 2026-06-02*