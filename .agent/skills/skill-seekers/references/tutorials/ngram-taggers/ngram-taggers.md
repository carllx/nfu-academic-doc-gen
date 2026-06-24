# How To: Ngram Taggers

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test ngram taggers

## Prerequisites

**Required Modules:**
- `unittest`
- `nltk.corpus`
- `nltk.jsontags`
- `nltk.tag`
- `nltk.tag.brill`


## Step-by-Step Guide

### Step 1: Assign unitagger = UnigramTagger(...)

```python
unitagger = UnigramTagger(self.corpus, backoff=self.default_tagger)
```

### Step 2: Assign bitagger = BigramTagger(...)

```python
bitagger = BigramTagger(self.corpus, backoff=unitagger)
```

### Step 3: Assign tritagger = TrigramTagger(...)

```python
tritagger = TrigramTagger(self.corpus, backoff=bitagger)
```

### Step 4: Assign ntagger = NgramTagger(...)

```python
ntagger = NgramTagger(4, self.corpus, backoff=tritagger)
```

### Step 5: Assign encoded = self.encoder.encode(...)

```python
encoded = self.encoder.encode(ntagger)
```

### Step 6: Assign decoded = self.decoder.decode(...)

```python
decoded = self.decoder.decode(encoded)
```

### Step 7: Call self.assertEqual()

```python
self.assertEqual(repr(ntagger), repr(decoded))
```

### Step 8: Call self.assertEqual()

```python
self.assertEqual(repr(tritagger), repr(decoded.backoff))
```

### Step 9: Call self.assertEqual()

```python
self.assertEqual(repr(bitagger), repr(decoded.backoff.backoff))
```

### Step 10: Call self.assertEqual()

```python
self.assertEqual(repr(unitagger), repr(decoded.backoff.backoff.backoff))
```

### Step 11: Call self.assertEqual()

```python
self.assertEqual(repr(self.default_tagger), repr(decoded.backoff.backoff.backoff.backoff))
```


## Complete Example

```python
# Workflow
unitagger = UnigramTagger(self.corpus, backoff=self.default_tagger)
bitagger = BigramTagger(self.corpus, backoff=unitagger)
tritagger = TrigramTagger(self.corpus, backoff=bitagger)
ntagger = NgramTagger(4, self.corpus, backoff=tritagger)
encoded = self.encoder.encode(ntagger)
decoded = self.decoder.decode(encoded)
self.assertEqual(repr(ntagger), repr(decoded))
self.assertEqual(repr(tritagger), repr(decoded.backoff))
self.assertEqual(repr(bitagger), repr(decoded.backoff.backoff))
self.assertEqual(repr(unitagger), repr(decoded.backoff.backoff.backoff))
self.assertEqual(repr(self.default_tagger), repr(decoded.backoff.backoff.backoff.backoff))
```

## Next Steps


---

*Source: test_json_serialization.py:56 | Complexity: Advanced | Last updated: 2026-06-02*