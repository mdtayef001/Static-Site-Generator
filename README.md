# Static Site Generator

A static site generator built from scratch in Python — no frameworks, no markdown
libraries. It reads Markdown files from `content/`, converts them to HTML, and writes
a complete website to `docs/`.

**Live site:** https://mdtayef001.github.io/Static-Site-Generator/

Built as part of the [Boot.dev](https://www.boot.dev/courses/build-static-site-generator-python)
course.

## What it does

```
content/*.md  →  parse markdown  →  build HTML tree  →  docs/*.html
static/*      →  copy assets     →  docs/
```

Given a Markdown file, it produces a full HTML page using `template.html`, handling:

- Headings (`#` through `######`)
- Paragraphs, blockquotes, and fenced code blocks
- Ordered and unordered lists
- Inline **bold**, _italic_, and `code`
- Images and links
- Nested content directories, mirrored into the output

## Running it

```bash
./main.sh      # build and serve at http://localhost:8888
./test.sh      # run the test suite (90 tests)
./build.sh     # build for GitHub Pages, with the repo basepath
```

## How it works

The conversion happens in two layers.

**Inline parsing** turns a line of text into typed pieces. A raw string is wrapped in a
single `TextNode`, then passed through a chain of splitters — one per delimiter, then
images, then links. Each splitter only touches nodes that are still plain text, so once
a chunk is tagged as bold or code, later passes leave it alone.

**Block parsing** splits the whole document on blank lines, identifies what each block is
(heading, list, quote, code…), and builds the matching HTML node. The result is a tree of
`HTMLNode` objects wrapped in a single `<div>`, which renders itself to a string
recursively.

### Project layout

```
src/
├── textnode.py            TextNode, TextType, and text → HTML conversion
├── htmlnode.py            HTMLNode, LeafNode, ParentNode
├── split_nodes.py         inline splitters and text_to_textnodes
├── extract_mardown.py     regex extraction of images and links
├── markdown_to_blocks.py  block splitting and block type detection
├── mardown_to_html.py     the full markdown → HTML tree conversion
├── extract_title.py       pulls the h1 for the page <title>
├── generate_page.py       renders pages into the template
├── copystatic.py          recursive static asset copying
├── main.py                entry point
└── test/                  unit tests
```

## What I learned

**Classes and inheritance.** `LeafNode` and `ParentNode` both extend `HTMLNode`, using
`super().__init__()` to reuse the parent's constructor instead of repeating it. Each
subclass overrides `to_html()` with its own behavior.

**Dunder methods.** Writing `__eq__` is what makes `node1 == node2` compare *contents*
instead of memory identity — without it, two identical nodes are unequal and the tests
can't work. `__repr__` controls what `print()` shows, which turned out to matter a lot
for debugging.

**Recursion.** `ParentNode.to_html()` calls `to_html()` on each of its children, so a tree
of any depth renders with one small function. The same shape appears again in the
directory walkers: handle a file directly, recurse into a folder.

**Enums.** `TextType` and `BlockType` replace loose strings with named values, so a typo
becomes an error instead of a condition that silently never matches.

**Unit testing.** The 90 tests caught bugs I couldn't see by reading — a doubled space in
an HTML tag, an `==` that should have been `!=`. Testing the *negative* cases (a block
that looks like a list but isn't) turned out to matter as much as the positive ones.

**Working with strings.** `.split()` with a maxsplit argument, slicing off prefixes,
`.strip()` versus `.strip(" ")`, and building output with f-strings and `.join()`.

**The filesystem.** `os.path.join` for portable paths, `os.makedirs(exist_ok=True)`,
`shutil.copy` and `rmtree`, and reading and writing files with `with open(...)`.

**Deployment.** Absolute links break when a site is served from a subdirectory, so the
generator takes a basepath argument from `sys.argv` and rewrites `href="/` and `src="/`
at build time — while leaving external URLs untouched.
