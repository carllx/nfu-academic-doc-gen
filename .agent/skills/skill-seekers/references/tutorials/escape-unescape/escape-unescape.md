# How To: Escape Unescape

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test escape unescape

## Prerequisites

**Required Modules:**
- `codecs`
- `io`
- `math`
- `ast`
- `contextlib`
- `textwrap`
- `pytest`
- `networkx`
- `networkx.readwrite.gml`
- `numpy`


## Step-by-Step Guide

### Step 1: Assign gml = 'graph [\n  name "&amp;&#34;&#xf;&#x4444;&#1234567890;&#x1234567890abcdef;&unknown;"\n]'

```python
gml = 'graph [\n  name "&amp;&#34;&#xf;&#x4444;&#1234567890;&#x1234567890abcdef;&unknown;"\n]'
```

**Verification:**
```python
assert '&"\x0f' + chr(17476) + '&#1234567890;&#x1234567890abcdef;&unknown;' == G.name
```

### Step 2: Assign G = nx.parse_gml(...)

```python
G = nx.parse_gml(gml)
```

**Verification:**
```python
assert answer == gml
```

### Step 3: Assign gml = unknown.join(...)

```python
gml = '\n'.join(nx.generate_gml(G))
```

### Step 4: Assign alnu = '#1234567890;&#38;#x1234567890abcdef'

```python
alnu = '#1234567890;&#38;#x1234567890abcdef'
```

### Step 5: Assign answer = value

```python
answer = 'graph [\n  name "&#38;&#34;&#15;&#17476;&#38;' + alnu + ';&#38;unknown;"\n]'
```

**Verification:**
```python
assert answer == gml
```


## Complete Example

```python
# Workflow
gml = 'graph [\n  name "&amp;&#34;&#xf;&#x4444;&#1234567890;&#x1234567890abcdef;&unknown;"\n]'
G = nx.parse_gml(gml)
assert '&"\x0f' + chr(17476) + '&#1234567890;&#x1234567890abcdef;&unknown;' == G.name
gml = '\n'.join(nx.generate_gml(G))
alnu = '#1234567890;&#38;#x1234567890abcdef'
answer = 'graph [\n  name "&#38;&#34;&#15;&#17476;&#38;' + alnu + ';&#38;unknown;"\n]'
assert answer == gml
```

## Next Steps


---

*Source: test_gml.py:458 | Complexity: Intermediate | Last updated: 2026-06-02*