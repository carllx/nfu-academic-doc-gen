# How To: String

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test string

## Prerequisites

**Required Modules:**
- `collections`
- `gc`
- `hashlib`
- `io`
- `itertools`
- `pickle`
- `random`
- `sys`
- `time`
- `concurrent.futures`
- `decimal`
- `joblib.func_inspect`
- `joblib.hashing`
- `joblib.memory`
- `joblib.test.common`
- `joblib.testing`


## Step-by-Step Guide

### Step 1: Assign string = 'foo'

```python
string = 'foo'
```

**Verification:**
```python
assert hash([a, b]) == hash([a, c])
```

### Step 2: Assign a = value

```python
a = {string: 'bar'}
```

### Step 3: Assign b = value

```python
b = {string: 'bar'}
```

### Step 4: Assign c = pickle.loads(...)

```python
c = pickle.loads(pickle.dumps(b))
```

**Verification:**
```python
assert hash([a, b]) == hash([a, c])
```


## Complete Example

```python
# Workflow
string = 'foo'
a = {string: 'bar'}
b = {string: 'bar'}
c = pickle.loads(pickle.dumps(b))
assert hash([a, b]) == hash([a, c])
```

## Next Steps


---

*Source: test_hashing.py:344 | Complexity: Intermediate | Last updated: 2026-06-02*