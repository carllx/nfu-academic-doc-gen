# How To: Interval Graph Check Invalid

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Tests for conditions that raise Exceptions

## Prerequisites

**Required Modules:**
- `math`
- `pytest`
- `networkx`
- `networkx.generators.interval_graph`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: 'Tests for conditions that raise Exceptions'

```python
'Tests for conditions that raise Exceptions'
```

### Step 2: Assign invalids_having_none = value

```python
invalids_having_none = [None, (1, 2)]
```

### Step 3: Assign invalids_having_set = value

```python
invalids_having_set = [{1, 2}]
```

### Step 4: Assign invalids_having_seq_but_not_length2 = value

```python
invalids_having_seq_but_not_length2 = [(1, 2, 3)]
```

### Step 5: Assign invalids_interval = value

```python
invalids_interval = [[3, 2]]
```

### Step 6: Call interval_graph()

```python
interval_graph(invalids_having_none)
```

### Step 7: Call interval_graph()

```python
interval_graph(invalids_having_set)
```

### Step 8: Call interval_graph()

```python
interval_graph(invalids_having_seq_but_not_length2)
```

### Step 9: Call interval_graph()

```python
interval_graph(invalids_interval)
```


## Complete Example

```python
# Workflow
'Tests for conditions that raise Exceptions'
invalids_having_none = [None, (1, 2)]
with pytest.raises(TypeError):
    interval_graph(invalids_having_none)
invalids_having_set = [{1, 2}]
with pytest.raises(TypeError):
    interval_graph(invalids_having_set)
invalids_having_seq_but_not_length2 = [(1, 2, 3)]
with pytest.raises(TypeError):
    interval_graph(invalids_having_seq_but_not_length2)
invalids_interval = [[3, 2]]
with pytest.raises(ValueError):
    interval_graph(invalids_interval)
```

## Next Steps


---

*Source: test_interval_graph.py:19 | Complexity: Advanced | Last updated: 2026-06-02*