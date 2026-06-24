# How To: Pos Template

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test pos template

## Prerequisites

**Required Modules:**
- `unittest`
- `nltk.corpus`
- `nltk.tag`
- `nltk.tbl`


## Step-by-Step Guide

### Step 1: Assign train_sents = value

```python
train_sents = treebank.tagged_sents()[:1000]
```

### Step 2: Assign tagger = UnigramTagger(...)

```python
tagger = UnigramTagger(train_sents)
```

### Step 3: Assign trainer = brill_trainer.BrillTaggerTrainer(...)

```python
trainer = brill_trainer.BrillTaggerTrainer(tagger, [brill.Template(brill.Pos([-1]))])
```

### Step 4: Assign brill_tagger = trainer.train(...)

```python
brill_tagger = trainer.train(train_sents)
```

### Step 5: Assign result = brill_tagger.tag(...)

```python
result = brill_tagger.tag('This is a foo bar sentence'.split())
```

### Step 6: Assign expected = value

```python
expected = [('This', 'DT'), ('is', 'VBZ'), ('a', 'DT'), ('foo', None), ('bar', 'NN'), ('sentence', None)]
```

### Step 7: Call self.assertEqual()

```python
self.assertEqual(result, expected)
```


## Complete Example

```python
# Workflow
train_sents = treebank.tagged_sents()[:1000]
tagger = UnigramTagger(train_sents)
trainer = brill_trainer.BrillTaggerTrainer(tagger, [brill.Template(brill.Pos([-1]))])
brill_tagger = trainer.train(train_sents)
result = brill_tagger.tag('This is a foo bar sentence'.split())
expected = [('This', 'DT'), ('is', 'VBZ'), ('a', 'DT'), ('foo', None), ('bar', 'NN'), ('sentence', None)]
self.assertEqual(result, expected)
```

## Next Steps


---

*Source: test_brill.py:13 | Complexity: Intermediate | Last updated: 2026-06-02*