# How To: Generic Multiedge Match

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test generic multiedge match

## Prerequisites

**Required Modules:**
- `operator`
- `networkx`
- `networkx.algorithms`


## Step-by-Step Guide

### Step 1: Assign full_match = iso.generic_multiedge_match(...)

```python
full_match = iso.generic_multiedge_match(['id', 'flowMin', 'flowMax'], [None] * 3, [eq] * 3)
```

**Verification:**
```python
assert flow_match(self.G1[1][2], self.G2[2][3])
```

### Step 2: Assign flow_match = iso.generic_multiedge_match(...)

```python
flow_match = iso.generic_multiedge_match(['flowMin', 'flowMax'], [None] * 2, [eq] * 2)
```

**Verification:**
```python
assert min_flow_match(self.G1[1][2], self.G2[2][3])
```

### Step 3: Assign min_flow_match = iso.generic_multiedge_match(...)

```python
min_flow_match = iso.generic_multiedge_match('flowMin', None, eq)
```

**Verification:**
```python
assert id_match(self.G1[1][2], self.G2[2][3])
```

### Step 4: Assign id_match = iso.generic_multiedge_match(...)

```python
id_match = iso.generic_multiedge_match('id', None, eq)
```

**Verification:**
```python
assert full_match(self.G1[1][2], self.G2[2][3])
```


## Complete Example

```python
# Workflow
full_match = iso.generic_multiedge_match(['id', 'flowMin', 'flowMax'], [None] * 3, [eq] * 3)
flow_match = iso.generic_multiedge_match(['flowMin', 'flowMax'], [None] * 2, [eq] * 2)
min_flow_match = iso.generic_multiedge_match('flowMin', None, eq)
id_match = iso.generic_multiedge_match('id', None, eq)
assert flow_match(self.G1[1][2], self.G2[2][3])
assert min_flow_match(self.G1[1][2], self.G2[2][3])
assert id_match(self.G1[1][2], self.G2[2][3])
assert full_match(self.G1[1][2], self.G2[2][3])
assert flow_match(self.G3[3][4], self.G4[4][5])
assert min_flow_match(self.G3[3][4], self.G4[4][5])
assert not id_match(self.G3[3][4], self.G4[4][5])
assert not full_match(self.G3[3][4], self.G4[4][5])
```

## Next Steps


---

*Source: test_match_helpers.py:48 | Complexity: Intermediate | Last updated: 2026-06-02*