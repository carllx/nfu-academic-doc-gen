# How To: Examples

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: Test the Basic Examples from the TGrep2 manual.

## Prerequisites

**Required Modules:**
- `unittest`
- `nltk`
- `nltk.tree`


## Step-by-Step Guide

### Step 1: '\n        Test the Basic Examples from the TGrep2 manual.\n        '

```python
'\n        Test the Basic Examples from the TGrep2 manual.\n        '
```

### Step 2: Assign tree = ParentedTree.fromstring(...)

```python
tree = ParentedTree.fromstring('(S (NP (AP x)) (NP (PP x)))')
```

### Step 3: Call self.assertEqual()

```python
self.assertEqual(list(tgrep.tgrep_positions('NP < PP', [tree])), [[(1,)]])
```

### Step 4: Assign tree = ParentedTree.fromstring(...)

```python
tree = ParentedTree.fromstring('(S (NP x) (VP x) (NP (PP x)) (VP x))')
```

### Step 5: Call self.assertEqual()

```python
self.assertEqual(list(tgrep.tgrep_positions('NP << PP . VP', [tree])), [[(2,)]])
```

### Step 6: Assign tree = ParentedTree.fromstring(...)

```python
tree = ParentedTree.fromstring('(S (NP (AP x)) (NP (PP x)) (NP (DET x) (NN x)) (VP x))')
```

### Step 7: Call self.assertEqual()

```python
self.assertEqual(list(tgrep.tgrep_positions('NP << PP | . VP', [tree])), [[(1,), (2,)]])
```

### Step 8: Assign tree = ParentedTree.fromstring(...)

```python
tree = ParentedTree.fromstring('(S (NP (NP (PP x)) (NP (AP x))) (VP (AP (NP (PP x)) (NP (AP x)))) (NP (RC (NP (AP x)))))')
```

### Step 9: Call self.assertEqual()

```python
self.assertEqual(list(tgrep.tgrep_positions('NP !<< PP [> NP | >> VP]', [tree])), [[(0, 1), (1, 0, 1)]])
```

### Step 10: Assign tree = ParentedTree.fromstring(...)

```python
tree = ParentedTree.fromstring('(S (NP (AP (PP x) (VP x))) (NP (AP (PP x) (NP x))) (NP x))')
```

### Step 11: Call self.assertEqual()

```python
self.assertEqual(list(tgrep.tgrep_positions('NP << (PP . VP)', [tree])), [[(0,)]])
```

### Step 12: Assign tree = ParentedTree.fromstring(...)

```python
tree = ParentedTree.fromstring('(S (NP (DET a) (NN cat) (PP (IN on) (NP x))) (NP (DET a) (NN cat) (PP (IN on) (NP x)) (PP x)) (NP x))')
```

### Step 13: Call self.assertEqual()

```python
self.assertEqual(list(tgrep.tgrep_positions("NP <' (PP <, (IN < on))", [tree])), [[(0,)]])
```

### Step 14: Assign tree = ParentedTree.fromstring(...)

```python
tree = ParentedTree.fromstring('(S (S (C x) (A (B x))) (S (C x) (A x)) (S (D x) (A (B x))))')
```

### Step 15: Call self.assertEqual()

```python
self.assertEqual(list(tgrep.tgrep_positions('S < (A < B) < C', [tree])), [[(0,)]])
```

### Step 16: Assign tree = ParentedTree.fromstring(...)

```python
tree = ParentedTree.fromstring('(S (S (A (B x) (C x))) (S (S (C x) (A (B x)))))')
```

### Step 17: Call self.assertEqual()

```python
self.assertEqual(list(tgrep.tgrep_positions('S < ((A < B) < C)', [tree])), [[(0,)]])
```

### Step 18: Call self.assertEqual()

```python
self.assertEqual(list(tgrep.tgrep_positions('S < (A < B < C)', [tree])), [[(0,)]])
```


## Complete Example

```python
# Workflow
'\n        Test the Basic Examples from the TGrep2 manual.\n        '
tree = ParentedTree.fromstring('(S (NP (AP x)) (NP (PP x)))')
self.assertEqual(list(tgrep.tgrep_positions('NP < PP', [tree])), [[(1,)]])
tree = ParentedTree.fromstring('(S (NP x) (VP x) (NP (PP x)) (VP x))')
self.assertEqual(list(tgrep.tgrep_positions('NP << PP . VP', [tree])), [[(2,)]])
tree = ParentedTree.fromstring('(S (NP (AP x)) (NP (PP x)) (NP (DET x) (NN x)) (VP x))')
self.assertEqual(list(tgrep.tgrep_positions('NP << PP | . VP', [tree])), [[(1,), (2,)]])
tree = ParentedTree.fromstring('(S (NP (NP (PP x)) (NP (AP x))) (VP (AP (NP (PP x)) (NP (AP x)))) (NP (RC (NP (AP x)))))')
self.assertEqual(list(tgrep.tgrep_positions('NP !<< PP [> NP | >> VP]', [tree])), [[(0, 1), (1, 0, 1)]])
tree = ParentedTree.fromstring('(S (NP (AP (PP x) (VP x))) (NP (AP (PP x) (NP x))) (NP x))')
self.assertEqual(list(tgrep.tgrep_positions('NP << (PP . VP)', [tree])), [[(0,)]])
tree = ParentedTree.fromstring('(S (NP (DET a) (NN cat) (PP (IN on) (NP x))) (NP (DET a) (NN cat) (PP (IN on) (NP x)) (PP x)) (NP x))')
self.assertEqual(list(tgrep.tgrep_positions("NP <' (PP <, (IN < on))", [tree])), [[(0,)]])
tree = ParentedTree.fromstring('(S (S (C x) (A (B x))) (S (C x) (A x)) (S (D x) (A (B x))))')
self.assertEqual(list(tgrep.tgrep_positions('S < (A < B) < C', [tree])), [[(0,)]])
tree = ParentedTree.fromstring('(S (S (A (B x) (C x))) (S (S (C x) (A (B x)))))')
self.assertEqual(list(tgrep.tgrep_positions('S < ((A < B) < C)', [tree])), [[(0,)]])
self.assertEqual(list(tgrep.tgrep_positions('S < (A < B < C)', [tree])), [[(0,)]])
```

## Next Steps


---

*Source: test_tgrep.py:535 | Complexity: Advanced | Last updated: 2026-06-02*