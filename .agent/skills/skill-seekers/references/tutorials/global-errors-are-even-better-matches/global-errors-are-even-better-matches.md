# How To: Global Errors Are Even Better Matches

**Difficulty**: Advanced
**Estimated Time**: 10 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test global errors are even better matches

## Prerequisites

**Required Modules:**
- `unittest`
- `textwrap`
- `jsonpath_ng`
- `jsonschema`
- `jsonschema.validators`


## Step-by-Step Guide

### Step 1: Assign shallow = exceptions.ValidationError(...)

```python
shallow = exceptions.ValidationError('Oh no!', path=[])
```

### Step 2: Assign deep = exceptions.ValidationError(...)

```python
deep = exceptions.ValidationError('Oh yes!', path=['foo'])
```

### Step 3: Assign errors = sorted(...)

```python
errors = sorted([shallow, deep], key=exceptions.relevance)
```

### Step 4: Call self.assertEqual()

```python
self.assertEqual([list(error.path) for error in errors], [['foo'], []])
```

### Step 5: Assign errors = sorted(...)

```python
errors = sorted([deep, shallow], key=exceptions.relevance)
```

### Step 6: Call self.assertEqual()

```python
self.assertEqual([list(error.path) for error in errors], [['foo'], []])
```


## Complete Example

```python
# Workflow
shallow = exceptions.ValidationError('Oh no!', path=[])
deep = exceptions.ValidationError('Oh yes!', path=['foo'])
errors = sorted([shallow, deep], key=exceptions.relevance)
self.assertEqual([list(error.path) for error in errors], [['foo'], []])
errors = sorted([deep, shallow], key=exceptions.relevance)
self.assertEqual([list(error.path) for error in errors], [['foo'], []])
```

## Next Steps


---

*Source: test_exceptions.py:345 | Complexity: Advanced | Last updated: 2026-06-02*