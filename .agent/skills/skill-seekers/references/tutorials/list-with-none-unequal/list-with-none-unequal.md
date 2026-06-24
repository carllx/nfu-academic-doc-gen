# How To: List With None Unequal

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test list with none unequal

## Prerequisites

**Required Modules:**
- `math`
- `unittest`
- `jsonschema._utils`


## Step-by-Step Guide

### Step 1: Assign list_1 = value

```python
list_1 = ['a', 'b', None]
```

### Step 2: Assign list_2 = value

```python
list_2 = ['a', 'b', 'c']
```

### Step 3: Call self.assertFalse()

```python
self.assertFalse(equal(list_1, list_2))
```

### Step 4: Assign list_1 = value

```python
list_1 = ['a', 'b', None]
```

### Step 5: Assign list_2 = value

```python
list_2 = [None, 'b', 'c']
```

### Step 6: Call self.assertFalse()

```python
self.assertFalse(equal(list_1, list_2))
```


## Complete Example

```python
# Workflow
list_1 = ['a', 'b', None]
list_2 = ['a', 'b', 'c']
self.assertFalse(equal(list_1, list_2))
list_1 = ['a', 'b', None]
list_2 = [None, 'b', 'c']
self.assertFalse(equal(list_1, list_2))
```

## Next Steps


---

*Source: test_utils.py:102 | Complexity: Intermediate | Last updated: 2026-06-02*