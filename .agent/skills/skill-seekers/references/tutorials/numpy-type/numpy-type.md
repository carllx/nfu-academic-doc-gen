# How To: Numpy Type

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test numpy type

## Prerequisites

**Required Modules:**
- `io`
- `time`
- `pytest`
- `networkx`
- `math`


## Step-by-Step Guide

### Step 1: Assign np = pytest.importorskip(...)

```python
np = pytest.importorskip('numpy')
```

**Verification:**
```python
assert expected == obtained
```

### Step 2: Assign G = nx.path_graph(...)

```python
G = nx.path_graph(4)
```

### Step 3: Call nx.set_node_attributes()

```python
nx.set_node_attributes(G, {n: n for n in np.arange(4)}, 'number')
```

### Step 4: Assign unknown = np.float64(...)

```python
G[0][1]['edge-number'] = np.float64(1.1)
```

### Step 5: Assign expected = value

```python
expected = f'''<gexf xmlns="http://www.gexf.net/1.2draft" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.gexf.net/1.2draft http://www.gexf.net/1.2draft/gexf.xsd" version="1.2">\n  <meta lastmodifieddate="{time.strftime('%Y-%m-%d')}">\n    <creator>NetworkX {nx.__version__}</creator>\n  </meta>\n  <graph defaultedgetype="undirected" mode="static" name="">\n    <attributes mode="static" class="edge">\n      <attribute id="1" title="edge-number" type="float" />\n    </attributes>\n    <attributes mode="static" class="node">\n      <attribute id="0" title="number" type="int" />\n    </attributes>\n    <nodes>\n      <node id="0" label="0">\n        <attvalues>\n          <attvalue for="0" value="0" />\n        </attvalues>\n      </node>\n      <node id="1" label="1">\n        <attvalues>\n          <attvalue for="0" value="1" />\n        </attvalues>\n      </node>\n      <node id="2" label="2">\n        <attvalues>\n          <attvalue for="0" value="2" />\n        </attvalues>\n      </node>\n      <node id="3" label="3">\n        <attvalues>\n          <attvalue for="0" value="3" />\n        </attvalues>\n      </node>\n    </nodes>\n    <edges>\n      <edge source="0" target="1" id="0">\n        <attvalues>\n          <attvalue for="1" value="1.1" />\n        </attvalues>\n      </edge>\n      <edge source="1" target="2" id="1" />\n      <edge source="2" target="3" id="2" />\n    </edges>\n  </graph>\n</gexf>'''
```

### Step 6: Assign obtained = unknown.join(...)

```python
obtained = '\n'.join(nx.generate_gexf(G))
```

**Verification:**
```python
assert expected == obtained
```


## Complete Example

```python
# Workflow
np = pytest.importorskip('numpy')
G = nx.path_graph(4)
nx.set_node_attributes(G, {n: n for n in np.arange(4)}, 'number')
G[0][1]['edge-number'] = np.float64(1.1)
expected = f'''<gexf xmlns="http://www.gexf.net/1.2draft" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.gexf.net/1.2draft http://www.gexf.net/1.2draft/gexf.xsd" version="1.2">\n  <meta lastmodifieddate="{time.strftime('%Y-%m-%d')}">\n    <creator>NetworkX {nx.__version__}</creator>\n  </meta>\n  <graph defaultedgetype="undirected" mode="static" name="">\n    <attributes mode="static" class="edge">\n      <attribute id="1" title="edge-number" type="float" />\n    </attributes>\n    <attributes mode="static" class="node">\n      <attribute id="0" title="number" type="int" />\n    </attributes>\n    <nodes>\n      <node id="0" label="0">\n        <attvalues>\n          <attvalue for="0" value="0" />\n        </attvalues>\n      </node>\n      <node id="1" label="1">\n        <attvalues>\n          <attvalue for="0" value="1" />\n        </attvalues>\n      </node>\n      <node id="2" label="2">\n        <attvalues>\n          <attvalue for="0" value="2" />\n        </attvalues>\n      </node>\n      <node id="3" label="3">\n        <attvalues>\n          <attvalue for="0" value="3" />\n        </attvalues>\n      </node>\n    </nodes>\n    <edges>\n      <edge source="0" target="1" id="0">\n        <attvalues>\n          <attvalue for="1" value="1.1" />\n        </attvalues>\n      </edge>\n      <edge source="1" target="2" id="1" />\n      <edge source="2" target="3" id="2" />\n    </edges>\n  </graph>\n</gexf>'''
obtained = '\n'.join(nx.generate_gexf(G))
assert expected == obtained
```

## Next Steps


---

*Source: test_gexf.py:395 | Complexity: Intermediate | Last updated: 2026-06-02*