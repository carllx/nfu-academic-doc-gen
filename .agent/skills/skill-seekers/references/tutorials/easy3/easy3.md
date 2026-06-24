# How To: Easy3

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: If expected disagreement is 0, K-Apha should be 1.

## Prerequisites

**Required Modules:**
- `unittest`
- `nltk.metrics.agreement`


## Step-by-Step Guide

### Step 1: '\n        If expected disagreement is 0, K-Apha should be 1.\n        '

```python
'\n        If expected disagreement is 0, K-Apha should be 1.\n        '
```

### Step 2: Assign data = value

```python
data = [('coder1', '1', 1), ('coder2', '1', 1), ('coder1', '2', 2), ('coder2', '2', 2)]
```

### Step 3: Assign annotation_task = AnnotationTask(...)

```python
annotation_task = AnnotationTask(data)
```

### Step 4: Call self.assertAlmostEqual()

```python
self.assertAlmostEqual(annotation_task.alpha(), 1.0)
```

### Step 5: Assign data = value

```python
data = [('coder1', '1', 1), ('coder2', '1', 1), ('coder1', '2', 2)]
```

### Step 6: Assign annotation_task = AnnotationTask(...)

```python
annotation_task = AnnotationTask(data)
```

### Step 7: Call self.assertAlmostEqual()

```python
self.assertAlmostEqual(annotation_task.alpha(), 1.0)
```


## Complete Example

```python
# Workflow
'\n        If expected disagreement is 0, K-Apha should be 1.\n        '
data = [('coder1', '1', 1), ('coder2', '1', 1), ('coder1', '2', 2), ('coder2', '2', 2)]
annotation_task = AnnotationTask(data)
self.assertAlmostEqual(annotation_task.alpha(), 1.0)
data = [('coder1', '1', 1), ('coder2', '1', 1), ('coder1', '2', 2)]
annotation_task = AnnotationTask(data)
self.assertAlmostEqual(annotation_task.alpha(), 1.0)
```

## Next Steps


---

*Source: test_disagreement.py:43 | Complexity: Intermediate | Last updated: 2026-06-02*