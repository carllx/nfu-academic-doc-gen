# How To: Simple

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test simple

## Prerequisites

**Required Modules:**
- `unittest`
- `nltk.classify.naivebayes`


## Step-by-Step Guide

### Step 1: Assign training_features = value

```python
training_features = [({'nice': True, 'good': True}, 'positive'), ({'bad': True, 'mean': True}, 'negative')]
```

### Step 2: Assign classifier = NaiveBayesClassifier.train(...)

```python
classifier = NaiveBayesClassifier.train(training_features)
```

### Step 3: Assign result = classifier.prob_classify(...)

```python
result = classifier.prob_classify({'nice': True})
```

### Step 4: Call self.assertTrue()

```python
self.assertTrue(result.prob('positive') > result.prob('negative'))
```

### Step 5: Call self.assertEqual()

```python
self.assertEqual(result.max(), 'positive')
```

### Step 6: Assign result = classifier.prob_classify(...)

```python
result = classifier.prob_classify({'bad': True})
```

### Step 7: Call self.assertTrue()

```python
self.assertTrue(result.prob('positive') < result.prob('negative'))
```

### Step 8: Call self.assertEqual()

```python
self.assertEqual(result.max(), 'negative')
```


## Complete Example

```python
# Workflow
training_features = [({'nice': True, 'good': True}, 'positive'), ({'bad': True, 'mean': True}, 'negative')]
classifier = NaiveBayesClassifier.train(training_features)
result = classifier.prob_classify({'nice': True})
self.assertTrue(result.prob('positive') > result.prob('negative'))
self.assertEqual(result.max(), 'positive')
result = classifier.prob_classify({'bad': True})
self.assertTrue(result.prob('positive') < result.prob('negative'))
self.assertEqual(result.max(), 'negative')
```

## Next Steps


---

*Source: test_naivebayes.py:7 | Complexity: Advanced | Last updated: 2026-06-02*