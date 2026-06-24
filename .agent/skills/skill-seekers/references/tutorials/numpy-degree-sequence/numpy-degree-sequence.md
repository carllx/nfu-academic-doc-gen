# How To: Numpy Degree Sequence

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test numpy degree sequence

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.generators`


## Step-by-Step Guide

### Step 1: Assign np = pytest.importorskip(...)

```python
np = pytest.importorskip('numpy')
```

**Verification:**
```python
assert nx.is_graphical(ds, 'eg')
```

### Step 2: Assign ds = np.array(...)

```python
ds = np.array([1, 2, 2, 2, 1], dtype=np.int64)
```

**Verification:**
```python
assert nx.is_graphical(ds, 'hh')
```

### Step 3: Assign ds = np.array(...)

```python
ds = np.array([1, 2, 2, 2, 1], dtype=np.float64)
```

**Verification:**
```python
assert nx.is_graphical(ds, 'eg')
```

### Step 4: Assign ds = np.array(...)

```python
ds = np.array([1.1, 2, 2, 2, 1], dtype=np.float64)
```

**Verification:**
```python
assert nx.is_graphical(ds, 'hh')
```

### Step 5: Call pytest.raises()

```python
pytest.raises(nx.NetworkXException, nx.is_graphical, ds, 'eg')
```

### Step 6: Call pytest.raises()

```python
pytest.raises(nx.NetworkXException, nx.is_graphical, ds, 'hh')
```


## Complete Example

```python
# Workflow
np = pytest.importorskip('numpy')
ds = np.array([1, 2, 2, 2, 1], dtype=np.int64)
assert nx.is_graphical(ds, 'eg')
assert nx.is_graphical(ds, 'hh')
ds = np.array([1, 2, 2, 2, 1], dtype=np.float64)
assert nx.is_graphical(ds, 'eg')
assert nx.is_graphical(ds, 'hh')
ds = np.array([1.1, 2, 2, 2, 1], dtype=np.float64)
pytest.raises(nx.NetworkXException, nx.is_graphical, ds, 'eg')
pytest.raises(nx.NetworkXException, nx.is_graphical, ds, 'hh')
```

## Next Steps


---

*Source: test_graphical.py:153 | Complexity: Intermediate | Last updated: 2026-06-02*