# How To: Set Consolidation Rosettacode

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test set consolidation rosettacode

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms`
- `networkx.algorithms.connectivity.kcomponents`


## Step-by-Step Guide

### Step 1: Assign question = value

```python
question = [{'A', 'B'}, {'C', 'D'}]
```

**Verification:**
```python
assert {frozenset(s) for s in result} == {frozenset(s) for s in solution}
```

### Step 2: Assign solution = value

```python
solution = [{'A', 'B'}, {'C', 'D'}]
```

### Step 3: Call list_of_sets_equal()

```python
list_of_sets_equal(_consolidate(question, 1), solution)
```

### Step 4: Assign question = value

```python
question = [{'A', 'B'}, {'B', 'C'}]
```

### Step 5: Assign solution = value

```python
solution = [{'A', 'B', 'C'}]
```

### Step 6: Call list_of_sets_equal()

```python
list_of_sets_equal(_consolidate(question, 1), solution)
```

### Step 7: Assign question = value

```python
question = [{'A', 'B'}, {'C', 'D'}, {'D', 'B'}]
```

### Step 8: Assign solution = value

```python
solution = [{'A', 'C', 'B', 'D'}]
```

### Step 9: Call list_of_sets_equal()

```python
list_of_sets_equal(_consolidate(question, 1), solution)
```

### Step 10: Assign question = value

```python
question = [{'H', 'I', 'K'}, {'A', 'B'}, {'C', 'D'}, {'D', 'B'}, {'F', 'G', 'H'}]
```

### Step 11: Assign solution = value

```python
solution = [{'A', 'C', 'B', 'D'}, {'G', 'F', 'I', 'H', 'K'}]
```

### Step 12: Call list_of_sets_equal()

```python
list_of_sets_equal(_consolidate(question, 1), solution)
```

### Step 13: Assign question = value

```python
question = [{'A', 'H'}, {'H', 'I', 'K'}, {'A', 'B'}, {'C', 'D'}, {'D', 'B'}, {'F', 'G', 'H'}]
```

### Step 14: Assign solution = value

```python
solution = [{'A', 'C', 'B', 'D', 'G', 'F', 'I', 'H', 'K'}]
```

### Step 15: Call list_of_sets_equal()

```python
list_of_sets_equal(_consolidate(question, 1), solution)
```

### Step 16: Assign question = value

```python
question = [{'H', 'I', 'K'}, {'A', 'B'}, {'C', 'D'}, {'D', 'B'}, {'F', 'G', 'H'}, {'A', 'H'}]
```

### Step 17: Assign solution = value

```python
solution = [{'A', 'C', 'B', 'D', 'G', 'F', 'I', 'H', 'K'}]
```

### Step 18: Call list_of_sets_equal()

```python
list_of_sets_equal(_consolidate(question, 1), solution)
```

**Verification:**
```python
assert {frozenset(s) for s in result} == {frozenset(s) for s in solution}
```


## Complete Example

```python
# Workflow
def list_of_sets_equal(result, solution):
    assert {frozenset(s) for s in result} == {frozenset(s) for s in solution}
question = [{'A', 'B'}, {'C', 'D'}]
solution = [{'A', 'B'}, {'C', 'D'}]
list_of_sets_equal(_consolidate(question, 1), solution)
question = [{'A', 'B'}, {'B', 'C'}]
solution = [{'A', 'B', 'C'}]
list_of_sets_equal(_consolidate(question, 1), solution)
question = [{'A', 'B'}, {'C', 'D'}, {'D', 'B'}]
solution = [{'A', 'C', 'B', 'D'}]
list_of_sets_equal(_consolidate(question, 1), solution)
question = [{'H', 'I', 'K'}, {'A', 'B'}, {'C', 'D'}, {'D', 'B'}, {'F', 'G', 'H'}]
solution = [{'A', 'C', 'B', 'D'}, {'G', 'F', 'I', 'H', 'K'}]
list_of_sets_equal(_consolidate(question, 1), solution)
question = [{'A', 'H'}, {'H', 'I', 'K'}, {'A', 'B'}, {'C', 'D'}, {'D', 'B'}, {'F', 'G', 'H'}]
solution = [{'A', 'C', 'B', 'D', 'G', 'F', 'I', 'H', 'K'}]
list_of_sets_equal(_consolidate(question, 1), solution)
question = [{'H', 'I', 'K'}, {'A', 'B'}, {'C', 'D'}, {'D', 'B'}, {'F', 'G', 'H'}, {'A', 'H'}]
solution = [{'A', 'C', 'B', 'D', 'G', 'F', 'I', 'H', 'K'}]
list_of_sets_equal(_consolidate(question, 1), solution)
```

## Next Steps


---

*Source: test_kcomponents.py:287 | Complexity: Advanced | Last updated: 2026-06-02*