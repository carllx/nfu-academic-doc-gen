# How To: Weights Thresholds

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test weights thresholds

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms.threshold`


## Step-by-Step Guide

### Step 1: Assign wseq = value

```python
wseq = [3, 4, 3, 3, 5, 6, 5, 4, 5, 6]
```

**Verification:**
```python
assert cs == cs2
```

### Step 2: Assign cs = nxt.weights_to_creation_sequence(...)

```python
cs = nxt.weights_to_creation_sequence(wseq, threshold=10)
```

**Verification:**
```python
assert wseq == [s * 0.125 for s in [4, 4, 4, 3, 5, 5, 2, 2, 2, 6, 6, 6, 1, 1, 7, 7, 7]]
```

### Step 3: Assign wseq = nxt.creation_sequence_to_weights(...)

```python
wseq = nxt.creation_sequence_to_weights(cs)
```

**Verification:**
```python
assert wseq == [s * 0.125 for s in [4, 4, 4, 3, 5, 5, 2, 2, 2, 6, 6, 6, 1, 1, 7, 7, 7]]
```

### Step 4: Assign cs2 = nxt.weights_to_creation_sequence(...)

```python
cs2 = nxt.weights_to_creation_sequence(wseq)
```

**Verification:**
```python
assert wseq == [s * 0.1 for s in [5, 5, 4, 6, 3, 3, 3, 7, 2, 8, 1, 9, 0]]
```

### Step 5: Assign wseq = nxt.creation_sequence_to_weights(...)

```python
wseq = nxt.creation_sequence_to_weights(nxt.uncompact([3, 1, 2, 3, 3, 2, 3]))
```

**Verification:**
```python
assert wseq == [s * 0.1 for s in [5, 5, 4, 6, 3, 3, 3, 7, 2, 8, 1, 9, 0]]
```

### Step 6: Assign wseq = nxt.creation_sequence_to_weights(...)

```python
wseq = nxt.creation_sequence_to_weights([3, 1, 2, 3, 3, 2, 3])
```

**Verification:**
```python
assert sum((abs(c - d) for c, d in zip(wseq, ws))) < 1e-14
```

### Step 7: Assign wseq = nxt.creation_sequence_to_weights(...)

```python
wseq = nxt.creation_sequence_to_weights(list(enumerate('ddidiiidididi')))
```

**Verification:**
```python
assert wseq == [s * 0.1 for s in [5, 5, 4, 6, 3, 3, 3, 7, 2, 8, 1, 9, 0]]
```

### Step 8: Assign wseq = nxt.creation_sequence_to_weights(...)

```python
wseq = nxt.creation_sequence_to_weights('ddidiiidididi')
```

**Verification:**
```python
assert wseq == [s * 0.1 for s in [5, 5, 4, 6, 3, 3, 3, 7, 2, 8, 1, 9, 0]]
```

### Step 9: Assign wseq = nxt.creation_sequence_to_weights(...)

```python
wseq = nxt.creation_sequence_to_weights('ddidiiidididid')
```

### Step 10: Assign ws = value

```python
ws = [s / 12 for s in [6, 6, 5, 7, 4, 4, 4, 8, 3, 9, 2, 10, 1, 11]]
```

**Verification:**
```python
assert sum((abs(c - d) for c, d in zip(wseq, ws))) < 1e-14
```


## Complete Example

```python
# Workflow
wseq = [3, 4, 3, 3, 5, 6, 5, 4, 5, 6]
cs = nxt.weights_to_creation_sequence(wseq, threshold=10)
wseq = nxt.creation_sequence_to_weights(cs)
cs2 = nxt.weights_to_creation_sequence(wseq)
assert cs == cs2
wseq = nxt.creation_sequence_to_weights(nxt.uncompact([3, 1, 2, 3, 3, 2, 3]))
assert wseq == [s * 0.125 for s in [4, 4, 4, 3, 5, 5, 2, 2, 2, 6, 6, 6, 1, 1, 7, 7, 7]]
wseq = nxt.creation_sequence_to_weights([3, 1, 2, 3, 3, 2, 3])
assert wseq == [s * 0.125 for s in [4, 4, 4, 3, 5, 5, 2, 2, 2, 6, 6, 6, 1, 1, 7, 7, 7]]
wseq = nxt.creation_sequence_to_weights(list(enumerate('ddidiiidididi')))
assert wseq == [s * 0.1 for s in [5, 5, 4, 6, 3, 3, 3, 7, 2, 8, 1, 9, 0]]
wseq = nxt.creation_sequence_to_weights('ddidiiidididi')
assert wseq == [s * 0.1 for s in [5, 5, 4, 6, 3, 3, 3, 7, 2, 8, 1, 9, 0]]
wseq = nxt.creation_sequence_to_weights('ddidiiidididid')
ws = [s / 12 for s in [6, 6, 5, 7, 4, 4, 4, 8, 3, 9, 2, 10, 1, 11]]
assert sum((abs(c - d) for c, d in zip(wseq, ws))) < 1e-14
```

## Next Steps


---

*Source: test_threshold.py:171 | Complexity: Advanced | Last updated: 2026-06-02*