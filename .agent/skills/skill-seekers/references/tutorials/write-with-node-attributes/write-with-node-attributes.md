# How To: Write With Node Attributes

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test write with node attributes

## Prerequisites

**Required Modules:**
- `io`
- `time`
- `pytest`
- `networkx`
- `math`


## Step-by-Step Guide

### Step 1: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

**Verification:**
```python
assert expected == obtained
```

### Step 2: Call G.add_edges_from()

```python
G.add_edges_from([(0, 1), (1, 2), (2, 3)])
```

### Step 3: Assign expected = value

```python
expected = f'''<gexf xmlns="http://www.gexf.net/1.2draft" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.gexf.net/1.2draft http://www.gexf.net/1.2draft/gexf.xsd" version="1.2">\n  <meta lastmodifieddate="{time.strftime('%Y-%m-%d')}">\n    <creator>NetworkX {nx.__version__}</creator>\n  </meta>\n  <graph defaultedgetype="undirected" mode="dynamic" name="" timeformat="long">\n    <nodes>\n      <node id="0" label="0" pid="0" start="0" end="1" />\n      <node id="1" label="1" pid="1" start="1" end="2" />\n      <node id="2" label="2" pid="2" start="2" end="3" />\n      <node id="3" label="3" pid="3" start="3" end="4" />\n    </nodes>\n    <edges>\n      <edge source="0" target="1" id="0" />\n      <edge source="1" target="2" id="1" />\n      <edge source="2" target="3" id="2" />\n    </edges>\n  </graph>\n</gexf>'''
```

### Step 4: Assign obtained = unknown.join(...)

```python
obtained = '\n'.join(nx.generate_gexf(G))
```

**Verification:**
```python
assert expected == obtained
```

### Step 5: Assign unknown = i

```python
G.nodes[i]['id'] = i
```

### Step 6: Assign unknown = i

```python
G.nodes[i]['label'] = i
```

### Step 7: Assign unknown = i

```python
G.nodes[i]['pid'] = i
```

### Step 8: Assign unknown = i

```python
G.nodes[i]['start'] = i
```

### Step 9: Assign unknown = value

```python
G.nodes[i]['end'] = i + 1
```


## Complete Example

```python
# Workflow
G = nx.Graph()
G.add_edges_from([(0, 1), (1, 2), (2, 3)])
for i in range(4):
    G.nodes[i]['id'] = i
    G.nodes[i]['label'] = i
    G.nodes[i]['pid'] = i
    G.nodes[i]['start'] = i
    G.nodes[i]['end'] = i + 1
expected = f'''<gexf xmlns="http://www.gexf.net/1.2draft" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.gexf.net/1.2draft http://www.gexf.net/1.2draft/gexf.xsd" version="1.2">\n  <meta lastmodifieddate="{time.strftime('%Y-%m-%d')}">\n    <creator>NetworkX {nx.__version__}</creator>\n  </meta>\n  <graph defaultedgetype="undirected" mode="dynamic" name="" timeformat="long">\n    <nodes>\n      <node id="0" label="0" pid="0" start="0" end="1" />\n      <node id="1" label="1" pid="1" start="1" end="2" />\n      <node id="2" label="2" pid="2" start="2" end="3" />\n      <node id="3" label="3" pid="3" start="3" end="4" />\n    </nodes>\n    <edges>\n      <edge source="0" target="1" id="0" />\n      <edge source="1" target="2" id="1" />\n      <edge source="2" target="3" id="2" />\n    </edges>\n  </graph>\n</gexf>'''
obtained = '\n'.join(nx.generate_gexf(G))
assert expected == obtained
```

## Next Steps


---

*Source: test_gexf.py:332 | Complexity: Advanced | Last updated: 2026-06-02*