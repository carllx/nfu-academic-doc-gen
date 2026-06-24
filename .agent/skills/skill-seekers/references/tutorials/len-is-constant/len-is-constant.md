# How To: Len Is Constant

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test len is constant

## Prerequisites

**Required Modules:**
- `unittest`
- `collections`
- `timeit`
- `nltk.lm`
- `nltk.corpus.europarl_raw`


## Step-by-Step Guide

### Step 1: Assign small_vocab = Vocabulary(...)

```python
small_vocab = Vocabulary('abcde')
```

### Step 2: Assign large_vocab = Vocabulary(...)

```python
large_vocab = Vocabulary(english.words())
```

### Step 3: Assign small_vocab_len_time = timeit(...)

```python
small_vocab_len_time = timeit('len(small_vocab)', globals=locals())
```

### Step 4: Assign large_vocab_len_time = timeit(...)

```python
large_vocab_len_time = timeit('len(large_vocab)', globals=locals())
```

### Step 5: Call self.assertAlmostEqual()

```python
self.assertAlmostEqual(small_vocab_len_time, large_vocab_len_time, places=1)
```


## Complete Example

```python
# Workflow
small_vocab = Vocabulary('abcde')
from nltk.corpus.europarl_raw import english
large_vocab = Vocabulary(english.words())
small_vocab_len_time = timeit('len(small_vocab)', globals=locals())
large_vocab_len_time = timeit('len(large_vocab)', globals=locals())
self.assertAlmostEqual(small_vocab_len_time, large_vocab_len_time, places=1)
```

## Next Steps


---

*Source: test_vocabulary.py:144 | Complexity: Intermediate | Last updated: 2026-06-02*