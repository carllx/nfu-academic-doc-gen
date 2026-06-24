# How To: Short Paths Are Better Matches

**Difficulty**: Advanced
**Estimated Time**: 10 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test short paths are better matches

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
shallow = exceptions.ValidationError('Oh no!', path=['baz'])
```

### Step 2: Assign deep = exceptions.ValidationError(...)

```python
deep = exceptions.ValidationError('Oh yes!', path=['foo', 'bar'])
```

### Step 3: Assign match = max(...)

```python
match = max([shallow, deep], key=exceptions.relevance)
```

### Step 4: Call self.assertIs()

```python
self.assertIs(match, shallow)
```

### Step 5: Assign match = max(...)

```python
match = max([deep, shallow], key=exceptions.relevance)
```

### Step 6: Call self.assertIs()

```python
self.assertIs(match, shallow)
```


## Complete Example

```python
# Workflow
shallow = exceptions.ValidationError('Oh no!', path=['baz'])
deep = exceptions.ValidationError('Oh yes!', path=['foo', 'bar'])
match = max([shallow, deep], key=exceptions.relevance)
self.assertIs(match, shallow)
match = max([deep, shallow], key=exceptions.relevance)
self.assertIs(match, shallow)
```

## Next Steps


---

*Source: test_exceptions.py:336 | Complexity: Advanced | Last updated: 2026-06-02*