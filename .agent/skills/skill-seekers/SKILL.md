---
name: skill-seekers
description: Generate LLM skills from documentation, codebases, and GitHub repositories
---

# Skill Seekers

## Prerequisites

```bash
pip install skill-seekers
# Or: uv pip install skill-seekers
```

## Commands

| Source | Command |
|--------|---------|
| Local code | `skill-seekers create ./path` |
| Docs URL | `skill-seekers create https://docs.example.com` |
| GitHub | `skill-seekers create owner/repo` |
| PDF | `skill-seekers create document.pdf` |

## Quick Start

```bash
# Analyze local codebase
skill-seekers create /path/to/project --name my-skill

# Package for Claude
yes | skill-seekers package output/my-skill/ --no-open
```

## Options

| Flag | Description |
|------|-------------|
| `--preset quick/standard/comprehensive` | Analysis preset |
| `--skip-patterns` | Skip pattern detection |
| `--skip-test-examples` | Skip test extraction |

---

# Skill_Seekers Codebase

## Description

Local codebase analysis and documentation generated from code analysis.

**Path:** `/private/tmp/Skill_Seekers`
**Files Analyzed:** 0
**Languages:** 
**Analysis Depth:** surface

## When to Use This Skill

Use this skill when you need to:
- Understand the codebase architecture and design patterns
- Find implementation examples and usage patterns
- Review API documentation extracted from code
- Check configuration patterns and best practices
- Explore test examples and real-world usage
- Navigate the codebase structure efficiently

## ⚡ Quick Reference

### Codebase Statistics

**Languages:**

**Analysis Performed:**
- ✅ API Reference (C2.5)
- ✅ Dependency Graph (C2.6)
- ✅ Design Patterns (C3.1)
- ✅ Test Examples (C3.2)
- ✅ Configuration Patterns (C3.4)
- ✅ Architectural Analysis (C3.7)
- ✅ Project Documentation (C3.9)

### 🎨 Design Patterns Detected

*From C3.1 codebase analysis (confidence > 0.7)*

- **Builder**: 10 instances
- **Adapter**: 3 instances
- **Factory**: 2 instances
- **Strategy**: 2 instances

*Total: 17 high-confidence patterns*

*See `references/patterns/` for complete pattern analysis*

## 📝 Code Examples

*High-quality examples extracted from test files (C3.2)*

**Workflow: test einsum sorting behavior** (complexity: 1.00)

```python
n1 = 26
x1 = np.random.random((1,) * n1)
path1 = np.einsum_path(x1, range(n1))[1]
output_indices1 = path1.split('->')[-1].strip()
assert all((c.isupper() for c in output_indices1)), f'Output indices for n=26 should use uppercase letters only: {output_indices1}'
assert_equal(output_indices1, ''.join(sorted(output_indices1)), err_msg=f'Output indices for n=26 are not lexicographically sorted: {output_indices1}')
n2 = 27
x2 = np.random.random((1,) * n2)
path2 = np.einsum_path(x2, range(n2))[1]
output_indices2 = path2.split('->')[-1].strip()
assert any((c.islower() for c in output_indices2)), f'Output indices for n=27 should include uppercase letters: {output_indices2}'
assert_equal(output_indices2, ''.join(sorted(output_indices2)), err_msg=f'Output indices for n=27 are not lexicographically sorted: {output_indices2}')
expected_indices = [chr(i + ord('A')) if i < 26 else chr(i - 26 + ord('a')) for i in range(n2)]
assert_equal(output_indices2, ''.join(expected_indices), err_msg=f"Output indices do not map to the correct dimensions. Expected: {''.join(expected_indices)}, Got: {output_indices2}")
```

**Workflow: test einsum fixedstridebug** (complexity: 1.00)

```python
A = np.arange(2 * 3).reshape(2, 3).astype(np.float32)
B = np.arange(2 * 3 * 2731).reshape(2, 3, 2731).astype(np.int16)
es = np.einsum('cl, cpx->lpx', A, B)
tp = np.tensordot(A, B, axes=(0, 0))
assert_equal(es, tp)
A = np.arange(3 * 3).reshape(3, 3).astype(np.float64)
B = np.arange(3 * 3 * 64 * 64).reshape(3, 3, 64, 64).astype(np.float32)
es = np.einsum('cl, cpxy->lpxy', A, B)
tp = np.tensordot(A, B, axes=(0, 0))
assert_equal(es, tp)
```

**Workflow: test different paths** (complexity: 1.00)

```python
dtype = np.dtype(dtype)
arr = (np.arange(7) + 0.5).astype(dtype)
scalar = np.array(2, dtype=dtype)
res = np.einsum('i->', arr)
assert res == arr.sum()
res = np.einsum('i,i->i', arr, arr)
assert_array_equal(res, arr * arr)
res = np.einsum('i,i->i', arr.repeat(2)[::2], arr.repeat(2)[::2])
assert_array_equal(res, arr * arr)
assert np.einsum('i,i->', arr, arr) == (arr * arr).sum()
out = np.ones(7, dtype=dtype)
res = np.einsum('i,->i', arr, dtype.type(2), out=out)
assert_array_equal(res, arr * dtype.type(2))
res = np.einsum(',i->i', scalar, arr)
assert_array_equal(res, arr * dtype.type(2))
res = np.einsum(',i->', scalar, arr)
assert res == np.einsum('i->', scalar * arr)
res = np.einsum('i,->', arr, scalar)
assert res == np.einsum('i->', scalar * arr)
arr = np.array([0.5, 0.5, 0.25, 4.5, 3.0], dtype=dtype)
res = np.einsum('i,i,i->', arr, arr, arr)
assert_array_equal(res, (arr * arr * arr).sum())
res = np.einsum('i,i,i,i->', arr, arr, arr, arr)
assert_array_equal(res, (arr * arr * arr * arr).sum())
```

**Workflow: test broadcasting dot cases** (complexity: 1.00)

```python
a = np.random.rand(1, 5, 4)
b = np.random.rand(4, 6)
c = np.random.rand(5, 6)
d = np.random.rand(10)
self.optimize_compare('ijk,kl,jl', operands=[a, b, c])
self.optimize_compare('ijk,kl,jl,i->i', operands=[a, b, c, d])
e = np.random.rand(1, 1, 5, 4)
f = np.random.rand(7, 7)
self.optimize_compare('abjk,kl,jl', operands=[e, b, c])
self.optimize_compare('abjk,kl,jl,ab->ab', operands=[e, b, c, f])
g = np.arange(64).reshape(2, 4, 8)
self.optimize_compare('obk,ijk->ioj', operands=[g, g])
```

**Workflow: test singleton broadcasting** (complexity: 1.00)

```python
eq = 'ijp,ipq,ikq->ijk'
shapes = ((3, 1, 1), (3, 1, 3), (1, 3, 3))
arrays = [np.random.rand(*shape) for shape in shapes]
self.optimize_compare(eq, operands=arrays)
eq = 'jhcabhijaci,dfijejgh->fgje'
shapes = ((1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1), (3, 1, 3, 1, 1, 1, 1, 2))
arrays = [np.random.rand(*shape) for shape in shapes]
self.optimize_compare(eq, operands=arrays)
eq = 'baegffahgc,hdggeff->dhg'
shapes = ((2, 1, 4, 1, 1, 1, 1, 2, 1, 1), (1, 1, 1, 1, 4, 1, 1))
arrays = [np.random.rand(*shape) for shape in shapes]
self.optimize_compare(eq, operands=arrays)
eq = 'cehgbaifff,fhhdegih->cdghbi'
shapes = ((1, 1, 1, 1, 1, 1, 1, 1, 1, 1), (2, 1, 1, 2, 4, 1, 1, 1))
arrays = [np.random.rand(*shape) for shape in shapes]
self.optimize_compare(eq, operands=arrays)
eq = 'gah,cdbcghefg->ef'
shapes = ((2, 3, 1), (1, 3, 1, 1, 1, 2, 1, 4, 1))
arrays = [np.random.rand(*shape) for shape in shapes]
self.optimize_compare(eq, operands=arrays)
eq = 'cacc,bcb->'
shapes = ((1, 1, 1, 1), (1, 4, 1))
arrays = [np.random.rand(*shape) for shape in shapes]
self.optimize_compare(eq, operands=arrays)
```

**Workflow: test memory contraints** (complexity: 1.00)

```python
outer_test = self.build_operands('a,b,c->abc')
path, path_str = np.einsum_path(*outer_test, optimize=('greedy', 0))
self.assert_path_equal(path, ['einsum_path', (0, 1, 2)])
path, path_str = np.einsum_path(*outer_test, optimize=('optimal', 0))
self.assert_path_equal(path, ['einsum_path', (0, 1, 2)])
long_test = self.build_operands('acdf,jbje,gihb,hfac')
path, path_str = np.einsum_path(*long_test, optimize=('greedy', 0))
self.assert_path_equal(path, ['einsum_path', (0, 1, 2, 3)])
path, path_str = np.einsum_path(*long_test, optimize=('optimal', 0))
self.assert_path_equal(path, ['einsum_path', (0, 1, 2, 3)])
```

**Workflow: test long paths** (complexity: 1.00)

```python
long_test1 = self.build_operands('acdf,jbje,gihb,hfac,gfac,gifabc,hfac')
path, path_str = np.einsum_path(*long_test1, optimize='greedy')
self.assert_path_equal(path, ['einsum_path', (3, 6), (3, 4), (2, 4), (2, 3), (0, 2), (0, 1)])
path, path_str = np.einsum_path(*long_test1, optimize='optimal')
self.assert_path_equal(path, ['einsum_path', (3, 6), (3, 4), (2, 4), (2, 3), (0, 2), (0, 1)])
long_test2 = self.build_operands('chd,bde,agbc,hiad,bdi,cgh,agdb')
path, path_str = np.einsum_path(*long_test2, optimize='greedy')
self.assert_path_equal(path, ['einsum_path', (3, 4), (0, 3), (3, 4), (1, 3), (1, 2), (0, 1)])
path, path_str = np.einsum_path(*long_test2, optimize='optimal')
self.assert_path_equal(path, ['einsum_path', (0, 5), (1, 4), (3, 4), (1, 3), (1, 2), (0, 1)])
```

**Workflow: test edge paths** (complexity: 1.00)

```python
edge_test1 = self.build_operands('eb,cb,fb->cef')
path, path_str = np.einsum_path(*edge_test1, optimize='greedy')
self.assert_path_equal(path, ['einsum_path', (0, 2), (0, 1)])
path, path_str = np.einsum_path(*edge_test1, optimize='optimal')
self.assert_path_equal(path, ['einsum_path', (0, 2), (0, 1)])
edge_test2 = self.build_operands('dd,fb,be,cdb->cef')
path, path_str = np.einsum_path(*edge_test2, optimize='greedy')
self.assert_path_equal(path, ['einsum_path', (0, 3), (0, 1), (0, 1)])
path, path_str = np.einsum_path(*edge_test2, optimize='optimal')
self.assert_path_equal(path, ['einsum_path', (0, 3), (0, 1), (0, 1)])
edge_test3 = self.build_operands('bca,cdb,dbf,afc->')
path, path_str = np.einsum_path(*edge_test3, optimize='greedy')
self.assert_path_equal(path, ['einsum_path', (1, 2), (0, 2), (0, 1)])
path, path_str = np.einsum_path(*edge_test3, optimize='optimal')
self.assert_path_equal(path, ['einsum_path', (1, 2), (0, 2), (0, 1)])
edge_test4 = self.build_operands('dcc,fce,ea,dbf->ab')
path, path_str = np.einsum_path(*edge_test4, optimize='greedy')
self.assert_path_equal(path, ['einsum_path', (1, 2), (0, 1), (0, 1)])
path, path_str = np.einsum_path(*edge_test4, optimize='optimal')
self.assert_path_equal(path, ['einsum_path', (1, 2), (0, 2), (0, 1)])
edge_test4 = self.build_operands('a,ac,ab,ad,cd,bd,bc->', size_dict={'a': 20, 'b': 20, 'c': 20, 'd': 20})
path, path_str = np.einsum_path(*edge_test4, optimize='greedy')
self.assert_path_equal(path, ['einsum_path', (0, 1), (0, 1, 2, 3, 4, 5)])
path, path_str = np.einsum_path(*edge_test4, optimize='optimal')
self.assert_path_equal(path, ['einsum_path', (0, 1), (0, 1, 2, 3, 4, 5)])
```

**Workflow: test convert to integers2** (complexity: 1.00)

```python
G = empty_graph()
G.add_edges_from([('C', 'D'), ('A', 'B'), ('A', 'C'), ('B', 'C')])
H = nx.convert_node_labels_to_integers(G, ordering='sorted')
degH = (d for n, d in H.degree())
degG = (d for n, d in G.degree())
assert sorted(degH) == sorted(degG)
H = nx.convert_node_labels_to_integers(G, ordering='sorted', label_attribute='label')
assert H.nodes[0]['label'] == 'A'
assert H.nodes[1]['label'] == 'B'
assert H.nodes[2]['label'] == 'C'
assert H.nodes[3]['label'] == 'D'
```

**Workflow: test relabel copy name** (complexity: 1.00)

```python
G = nx.Graph()
H = nx.relabel_nodes(G, {}, copy=True)
assert H.graph == G.graph
H = nx.relabel_nodes(G, {}, copy=False)
assert H.graph == G.graph
G.name = 'first'
H = nx.relabel_nodes(G, {}, copy=True)
assert H.graph == G.graph
H = nx.relabel_nodes(G, {}, copy=False)
assert H.graph == G.graph
```

*See `references/test_examples/` for all extracted examples*

## ⚙️ Configuration Patterns

*From C3.4 configuration analysis*

**Configuration Files Analyzed:** 135
**Total Settings:** 10188
**Patterns Detected:** 0

**Configuration Types:**
- unknown: 135 files

*See `references/config_patterns/` for detailed configuration analysis*

## 📖 Project Documentation

*Extracted from markdown files in the project (C3.9)*

**Total Documentation Files:** 200
**Categories:** 10

### Overview

- **AGENTS.md** (`AGENTS.md`)
- **BULLETPROOF_QUICKSTART.md** (`BULLETPROOF_QUICKSTART.md`)
- **CLAUDE.md** (`CLAUDE.md`)
- **DOCUMENTATION_AUDIT_REPORT_2026-05-30.md** (`DOCUMENTATION_AUDIT_REPORT_2026-05-30.md`)
- **QWEN.md** (`QWEN.md`)
- *...and 14 more*

### Architecture

- **2026-03-14-epub-input-support-affected-files.md** (`docs/agents/research/2026-03-14-epub-input-support-affected-files.md`)
- **ARCHITECTURE_VERIFICATION_REPORT.md** (`docs/archive/historical/ARCHITECTURE_VERIFICATION_REPORT.md`)
- **HTTPX_SKILL_GRADING.md** (`docs/archive/historical/HTTPX_SKILL_GRADING.md`)
- **IMPLEMENTATION_SUMMARY_THREE_STREAM.md** (`docs/archive/historical/IMPLEMENTATION_SUMMARY_THREE_STREAM.md`)
- **LOCAL_REPO_TEST_RESULTS.md** (`docs/archive/historical/LOCAL_REPO_TEST_RESULTS.md`)
- *...and 14 more*

### Guides

- **HTTP_TRANSPORT.md** (`docs/guides/HTTP_TRANSPORT.md`)
- **MCP_SETUP.md** (`docs/guides/MCP_SETUP.md`)
- **MIGRATION_GUIDE.md** (`docs/guides/MIGRATION_GUIDE.md`)
- **MULTI_AGENT_SETUP.md** (`docs/guides/MULTI_AGENT_SETUP.md`)
- **SETUP_QUICK_REFERENCE.md** (`docs/guides/SETUP_QUICK_REFERENCE.md`)
- *...and 14 more*

### Features

- **BOOTSTRAP_SKILL.md** (`docs/features/BOOTSTRAP_SKILL.md`)
- **BOOTSTRAP_SKILL_TECHNICAL.md** (`docs/features/BOOTSTRAP_SKILL_TECHNICAL.md`)
- **ENHANCEMENT.md** (`docs/features/ENHANCEMENT.md`)
- **ENHANCEMENT_MODES.md** (`docs/features/ENHANCEMENT_MODES.md`)
- **HOW_TO_GUIDES.md** (`docs/features/HOW_TO_GUIDES.md`)
- *...and 7 more*

### Api

- **README.md** (`api/README.md`)
- **AI_SKILL_STANDARDS.md** (`docs/reference/AI_SKILL_STANDARDS.md`)
- **API_REFERENCE.md** (`docs/reference/API_REFERENCE.md`)
- **C3_x_Router_Architecture.md** (`docs/reference/C3_x_Router_Architecture.md`)
- **CLAUDE_INTEGRATION.md** (`docs/reference/CLAUDE_INTEGRATION.md`)
- *...and 24 more*

### Examples

- **README.md** (`examples/chroma-example/README.md`)
- **README.md** (`examples/cline-django-assistant/README.md`)
- **README.md** (`examples/continue-dev-universal/README.md`)
- **README.md** (`examples/cursor-react-skill/README.md`)
- **README.md** (`examples/cursor-react-skill/example-project/README.md`)
- *...and 8 more*

*See `references/documentation/` for all project documentation*

## 📚 Available References

This skill includes detailed reference documentation:

- **Dependencies**: `references/dependencies/` - Dependency graph and analysis
- **Patterns**: `references/patterns/` - Detected design patterns
- **Examples**: `references/test_examples/` - Usage examples from tests
- **Configuration**: `references/config_patterns/` - Configuration patterns
- **Documentation**: `references/documentation/` - Project documentation

---

**Generated by Skill Seeker** | Codebase Analyzer with C3.x Analysis
