# How To: Bipartite Edgelist Consistent Strip Handling

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: See gh-7462

Input when printed looks like:

    A       B       interaction     2
    B       C       interaction     4
    C       A       interaction

Note the trailing \t in the last line, which indicates the existence of
an empty data field.

## Prerequisites

**Required Modules:**
- `io`
- `pytest`
- `networkx`
- `networkx.algorithms`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: 'See gh-7462\n\n    Input when printed looks like:\n\n        A       B       interaction     2\n        B       C       interaction     4\n        C       A       interaction\n\n    Note the trailing \\t in the last line, which indicates the existence of\n    an empty data field.\n    '

```python
'See gh-7462\n\n    Input when printed looks like:\n\n        A       B       interaction     2\n        B       C       interaction     4\n        C       A       interaction\n\n    Note the trailing \\t in the last line, which indicates the existence of\n    an empty data field.\n    '
```

**Verification:**
```python
assert sorted(G.edges(data='weight')) == expected
```

### Step 2: Assign lines = io.StringIO(...)

```python
lines = io.StringIO('A\tB\tinteraction\t2\nB\tC\tinteraction\t4\nC\tA\tinteraction\t')
```

### Step 3: Assign descr = value

```python
descr = [('type', str), ('weight', str)]
```

### Step 4: Assign G = nx.bipartite.parse_edgelist(...)

```python
G = nx.bipartite.parse_edgelist(lines, delimiter='\t', data=descr)
```

### Step 5: Assign expected = value

```python
expected = [('A', 'B', '2'), ('A', 'C', ''), ('B', 'C', '4')]
```

**Verification:**
```python
assert sorted(G.edges(data='weight')) == expected
```


## Complete Example

```python
# Workflow
'See gh-7462\n\n    Input when printed looks like:\n\n        A       B       interaction     2\n        B       C       interaction     4\n        C       A       interaction\n\n    Note the trailing \\t in the last line, which indicates the existence of\n    an empty data field.\n    '
lines = io.StringIO('A\tB\tinteraction\t2\nB\tC\tinteraction\t4\nC\tA\tinteraction\t')
descr = [('type', str), ('weight', str)]
G = nx.bipartite.parse_edgelist(lines, delimiter='\t', data=descr)
expected = [('A', 'B', '2'), ('A', 'C', ''), ('B', 'C', '4')]
assert sorted(G.edges(data='weight')) == expected
```

## Next Steps


---

*Source: test_edgelist.py:221 | Complexity: Intermediate | Last updated: 2026-06-02*