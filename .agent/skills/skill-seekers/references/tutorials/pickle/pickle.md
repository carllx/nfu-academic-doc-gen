# How To: Pickle

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: workflow, integration

## Overview

Workflow: test pickle

## Prerequisites

**Required Modules:**
- `pickle`
- `pytest`
- `networkx`
- `networkx.classes.tests.dispatch_interface`
- `networkx.classes.tests.dispatch_interface`
- `networkx.classes.tests`
- `networkx.classes.tests.dispatch_interface`
- `networkx.classes.tests.dispatch_interface`


## Step-by-Step Guide

### Step 1: Assign count = 0

```python
count = 0
```

**Verification:**
```python
assert pickle.loads(pickled) is func.__wrapped__
```

### Step 2: Assign pickled = pickle.dumps(...)

```python
pickled = pickle.dumps(func.__wrapped__)
```

**Verification:**
```python
assert pickle.loads(pickled) is func
```

### Step 3: Assign pickled = pickle.dumps(...)

```python
pickled = pickle.dumps(func)
```

**Verification:**
```python
assert count > 0
```


## Complete Example

```python
# Workflow
count = 0
for name, func in nx.utils.backends._registered_algorithms.items():
    pickled = pickle.dumps(func.__wrapped__)
    assert pickle.loads(pickled) is func.__wrapped__
    try:
        pickled = pickle.dumps(func)
    except pickle.PicklingError:
        continue
    assert pickle.loads(pickled) is func
    count += 1
assert count > 0
assert pickle.loads(pickle.dumps(nx.inverse_line_graph)) is nx.inverse_line_graph
```

## Next Steps


---

*Source: test_backends.py:24 | Complexity: Beginner | Last updated: 2026-06-02*