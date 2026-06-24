# How To: Communicability2

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test communicability2

## Prerequisites

**Required Modules:**
- `collections`
- `pytest`
- `networkx`
- `networkx.algorithms.communicability_alg`


## Step-by-Step Guide

### Step 1: Assign answer_orig = value

```python
answer_orig = {('1', '1'): 1.6445956054135658, ('1', 'Albert'): 0.7430186221096251, ('1', 'Aric'): 0.7430186221096251, ('1', 'Dan'): 1.6208126320442937, ('1', 'Franck'): 0.42639707170035257, ('Albert', '1'): 0.7430186221096251, ('Albert', 'Albert'): 2.436825735871219, ('Albert', 'Aric'): 1.436825735871219, ('Albert', 'Dan'): 2.0472097037446453, ('Albert', 'Franck'): 1.834011167894469, ('Aric', '1'): 0.7430186221096251, ('Aric', 'Albert'): 1.436825735871219, ('Aric', 'Aric'): 2.4368257358712193, ('Aric', 'Dan'): 2.0472097037446457, ('Aric', 'Franck'): 1.834011167894469, ('Dan', '1'): 1.6208126320442937, ('Dan', 'Albert'): 2.0472097037446453, ('Dan', 'Aric'): 2.0472097037446457, ('Dan', 'Dan'): 3.130632849632817, ('Dan', 'Franck'): 1.4860372442192515, ('Franck', '1'): 0.42639707170035257, ('Franck', 'Albert'): 1.834011167894469, ('Franck', 'Aric'): 1.834011167894469, ('Franck', 'Dan'): 1.4860372442192515, ('Franck', 'Franck'): 2.3876142275231915}
```

**Verification:**
```python
assert answer[k1][k2] == pytest.approx(result[k1][k2], abs=1e-07)
```

### Step 2: Assign answer = defaultdict(...)

```python
answer = defaultdict(dict)
```

**Verification:**
```python
assert answer[k1][k2] == pytest.approx(result[k1][k2], abs=1e-07)
```

### Step 3: Assign G1 = nx.Graph(...)

```python
G1 = nx.Graph([('Franck', 'Aric'), ('Aric', 'Dan'), ('Dan', 'Albert'), ('Albert', 'Franck'), ('Dan', '1'), ('Franck', 'Albert')])
```

### Step 4: Assign result = communicability(...)

```python
result = communicability(G1)
```

### Step 5: Assign result = communicability_exp(...)

```python
result = communicability_exp(G1)
```

### Step 6: Assign unknown = v

```python
answer[k1][k2] = v
```

**Verification:**
```python
assert answer[k1][k2] == pytest.approx(result[k1][k2], abs=1e-07)
```


## Complete Example

```python
# Workflow
answer_orig = {('1', '1'): 1.6445956054135658, ('1', 'Albert'): 0.7430186221096251, ('1', 'Aric'): 0.7430186221096251, ('1', 'Dan'): 1.6208126320442937, ('1', 'Franck'): 0.42639707170035257, ('Albert', '1'): 0.7430186221096251, ('Albert', 'Albert'): 2.436825735871219, ('Albert', 'Aric'): 1.436825735871219, ('Albert', 'Dan'): 2.0472097037446453, ('Albert', 'Franck'): 1.834011167894469, ('Aric', '1'): 0.7430186221096251, ('Aric', 'Albert'): 1.436825735871219, ('Aric', 'Aric'): 2.4368257358712193, ('Aric', 'Dan'): 2.0472097037446457, ('Aric', 'Franck'): 1.834011167894469, ('Dan', '1'): 1.6208126320442937, ('Dan', 'Albert'): 2.0472097037446453, ('Dan', 'Aric'): 2.0472097037446457, ('Dan', 'Dan'): 3.130632849632817, ('Dan', 'Franck'): 1.4860372442192515, ('Franck', '1'): 0.42639707170035257, ('Franck', 'Albert'): 1.834011167894469, ('Franck', 'Aric'): 1.834011167894469, ('Franck', 'Dan'): 1.4860372442192515, ('Franck', 'Franck'): 2.3876142275231915}
answer = defaultdict(dict)
for (k1, k2), v in answer_orig.items():
    answer[k1][k2] = v
G1 = nx.Graph([('Franck', 'Aric'), ('Aric', 'Dan'), ('Dan', 'Albert'), ('Albert', 'Franck'), ('Dan', '1'), ('Franck', 'Albert')])
result = communicability(G1)
for k1, val in result.items():
    for k2 in val:
        assert answer[k1][k2] == pytest.approx(result[k1][k2], abs=1e-07)
result = communicability_exp(G1)
for k1, val in result.items():
    for k2 in val:
        assert answer[k1][k2] == pytest.approx(result[k1][k2], abs=1e-07)
```

## Next Steps


---

*Source: test_communicability.py:28 | Complexity: Intermediate | Last updated: 2026-06-02*