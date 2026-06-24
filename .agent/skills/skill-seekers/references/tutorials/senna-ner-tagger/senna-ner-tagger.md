# How To: Senna Ner Tagger

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test senna ner tagger

## Prerequisites

**Required Modules:**
- `unittest`
- `os`
- `nltk.classify`
- `nltk.tag`


## Step-by-Step Guide

### Step 1: Assign nertagger = SennaNERTagger(...)

```python
nertagger = SennaNERTagger(SENNA_EXECUTABLE_PATH)
```

### Step 2: Assign result_1 = nertagger.tag(...)

```python
result_1 = nertagger.tag('Shakespeare theatre was in London .'.split())
```

### Step 3: Assign expected_1 = value

```python
expected_1 = [('Shakespeare', 'B-PER'), ('theatre', 'O'), ('was', 'O'), ('in', 'O'), ('London', 'B-LOC'), ('.', 'O')]
```

### Step 4: Assign result_2 = nertagger.tag(...)

```python
result_2 = nertagger.tag('UN headquarters are in NY , USA .'.split())
```

### Step 5: Assign expected_2 = value

```python
expected_2 = [('UN', 'B-ORG'), ('headquarters', 'O'), ('are', 'O'), ('in', 'O'), ('NY', 'B-LOC'), (',', 'O'), ('USA', 'B-LOC'), ('.', 'O')]
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
nertagger = SennaNERTagger(SENNA_EXECUTABLE_PATH)
result_1 = nertagger.tag('Shakespeare theatre was in London .'.split())
expected_1 = [('Shakespeare', 'B-PER'), ('theatre', 'O'), ('was', 'O'), ('in', 'O'), ('London', 'B-LOC'), ('.', 'O')]
result_2 = nertagger.tag('UN headquarters are in NY , USA .'.split())
expected_2 = [('UN', 'B-ORG'), ('headquarters', 'O'), ('are', 'O'), ('in', 'O'), ('NY', 'B-LOC'), (',', 'O'), ('USA', 'B-LOC'), ('.', 'O')]
self.assertEqual(result_1, expected_1)
self.assertEqual(result_2, expected_2)
```

## Next Steps


---

*Source: test_senna.py:88 | Complexity: Intermediate | Last updated: 2026-06-02*