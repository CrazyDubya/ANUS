# 🍑 ANUS Framework - Interactive Demos

This directory contains comprehensive demonstrations of the ANUS (Autonomous Networked Utility System) framework capabilities.

## Available Demos

### 1. Simple Demo (`simple_demo.py`)
A quick demonstration of core functionality:
```bash
python simple_demo.py
```

### 2. Comprehensive Demo (`demo.py`)
Full feature demonstration including:
- All tool capabilities (Calculator, Text, Search, Code)
- Single vs Multi-agent modes
- Memory and context management
- Error handling
- Easter eggs and humor
- Performance metrics

```bash
python demo.py
```

### 3. Web Interface Demo (`web_demo.py`)
Interactive Streamlit web interface:
```bash
streamlit run web_demo.py
```

Then visit http://localhost:8501 in your browser.

### 4. Command Line Interface
Interactive CLI mode:
```bash
python -m anus
```

Or execute single tasks:
```bash
python -m anus --task "calculate 2 + 2"
python -m anus --task "search for python programming"
python -m anus --task 'count words in "hello world"'
```

## Example Tasks

### Calculator Tool
- `calculate 2 + 2`
- `calculate (10 + 5) * 3`
- `calculate 2 ** 8`
- `calculate 42 * 69` (Easter egg!)

### Text Processing Tool
- `count characters in "Hello World"`
- `count words in "This is a test"`
- `reverse "ANUS"`
- `uppercase "make this loud"`
- `lowercase "MAKE THIS QUIET"`
- `capitalize "title case this"`

### Search Tool
- `search for python programming`
- `search for artificial intelligence`
- `find information about machine learning`
- `look up deep learning`
- `search for anus` (Easter egg!)

### Code Execution Tool
- `run code ```python\nprint("Hello ANUS!")\n```'`
- `run code ```python\nresult = sum([1,2,3,4,5])\nprint(result)\n```'`
- `run code ```python\nimport math\nprint(math.pi)\n```'`

### Multi-Agent Complex Tasks
- `search for python and calculate the word count of results`
- `find AI tutorials and analyze their complexity`
- `research machine learning and create a summary`

## Features Demonstrated

✅ **Single-Agent Mode**: Simple tasks handled efficiently  
✅ **Multi-Agent Mode**: Complex tasks decomposed and handled by specialized agents  
✅ **Tool Integration**: Calculator, Text Processing, Search, Code Execution  
✅ **Memory Management**: Short-term and long-term memory systems  
✅ **Error Handling**: Graceful handling of errors and edge cases  
✅ **Security**: Safe code execution in restricted environment  
✅ **Easter Eggs**: Humorous responses and special number handling  
✅ **Performance**: Fast execution and metrics tracking  
✅ **Interactive UI**: Both CLI and web interfaces  

## Architecture Highlights

- **Hybrid Agent System**: Automatically switches between single and multi-agent modes
- **Tool Ecosystem**: Extensible tool system with security restrictions
- **Memory Systems**: Context retention and task history
- **Complexity Assessment**: Intelligent task complexity analysis
- **Security First**: Restricted code execution environment
- **Humor Integration**: Easter eggs and playful logging messages

## Getting Started

1. Install dependencies:
   ```bash
   pip install -e .
   ```

2. Run any demo:
   ```bash
   python simple_demo.py
   ```

3. Try the web interface:
   ```bash
   streamlit run web_demo.py
   ```

4. Explore interactive mode:
   ```bash
   python -m anus
   ```

## Next Steps

- Check out the main README.md for detailed documentation
- Explore the `anus/` directory for source code
- Create custom tools by extending the base tool classes
- Integrate ANUS into your own applications using the API

---

🍑 **ANUS Framework** - Making AI agents less awkward, one task at a time.