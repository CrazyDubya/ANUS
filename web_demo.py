#!/usr/bin/env python3
"""
ANUS Web Demo using Streamlit

This creates an interactive web interface to demonstrate the ANUS framework capabilities.
Run with: streamlit run web_demo.py
"""

import streamlit as st
import sys
import os
import time
import json
from typing import Dict, Any

# Add the project root to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from anus.core.orchestrator import AgentOrchestrator


def initialize_anus():
    """Initialize ANUS orchestrator with caching."""
    if 'orchestrator' not in st.session_state:
        with st.spinner("Initializing ANUS framework..."):
            st.session_state.orchestrator = AgentOrchestrator()
            st.session_state.task_history = []
    return st.session_state.orchestrator


def execute_task(task: str, mode: str = None) -> Dict[str, Any]:
    """Execute a task and store in history."""
    orchestrator = st.session_state.orchestrator
    
    with st.spinner(f"🍑 ANUS is processing: {task[:50] + '...' if len(task) > 50 else task}"):
        start_time = time.time()
        result = orchestrator.execute_task(task, mode=mode)
        end_time = time.time()
        
        # Add to history
        history_item = {
            "task": task,
            "result": result,
            "execution_time": end_time - start_time,
            "timestamp": time.time()
        }
        st.session_state.task_history.insert(0, history_item)
        
        # Keep only last 20 items
        if len(st.session_state.task_history) > 20:
            st.session_state.task_history = st.session_state.task_history[:20]
    
    return result


def display_result(result: Dict[str, Any], execution_time: float):
    """Display task result in a nice format."""
    st.success("✅ Task completed successfully!")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Execution Time", f"{execution_time:.3f}s")
    with col2:
        st.metric("Mode", result.get('mode', 'unknown'))
    with col3:
        iterations = result.get('iterations', 0)
        st.metric("Iterations", iterations)
    
    st.subheader("📊 Answer")
    st.write(result.get('answer', 'No answer generated'))
    
    # Show details in expander
    with st.expander("🔍 Execution Details"):
        st.json(result)


def main():
    """Main Streamlit app."""
    st.set_page_config(
        page_title="ANUS Framework Demo",
        page_icon="🍑",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Title and description
    st.title("🍑 ANUS Framework Demo")
    st.markdown("**Autonomous Networked Utility System** - Interactive Web Interface")
    
    st.markdown("""
    Welcome to the ANUS framework demonstration! This web interface showcases the capabilities 
    of our AI agent framework in an interactive format.
    """)
    
    # Initialize ANUS
    orchestrator = initialize_anus()
    
    # Sidebar for tool selection and examples
    with st.sidebar:
        st.header("🛠️ Tools & Examples")
        
        tool_category = st.selectbox(
            "Select Tool Category",
            ["Calculator", "Text Processing", "Search", "Code Execution", "Multi-Agent", "Custom"]
        )
        
        # Example tasks based on category
        examples = {
            "Calculator": [
                "calculate 2 + 2",
                "calculate 15 * 7 - 3",
                "calculate (10 + 5) / 3",
                "calculate 2 ** 8",
                "calculate 42 * 69"
            ],
            "Text Processing": [
                'count characters in "Hello ANUS!"',
                'count words in "This is a demo"',
                'reverse "ANUS"',
                'uppercase "make this loud"',
                'capitalize "title case this"'
            ],
            "Search": [
                "search for python programming",
                "search for artificial intelligence",
                "find information about machine learning",
                "search for anus framework",
                "look up deep learning"
            ],
            "Code Execution": [
                'run code ```python\nprint("Hello from ANUS!")\n```',
                'run code ```python\nresult = sum([1,2,3,4,5])\nprint(f"Sum: {result}")\n```',
                'run code ```python\nimport math\nprint(f"Pi: {math.pi:.4f}")\n```',
                'run code ```python\nfor i in range(3): print(f"Step {i}")\n```'
            ],
            "Multi-Agent": [
                "search for AI and calculate the average word count of results",
                "find python tutorials and analyze the complexity",
                "research machine learning and create a summary",
                "optimize and analyze the framework performance"
            ],
            "Custom": []
        }
        
        if tool_category != "Custom":
            st.subheader("💡 Example Tasks")
            for example in examples[tool_category]:
                if st.button(f"📋 {example}", key=f"ex_{example}"):
                    st.session_state.selected_task = example
    
    # Main interface
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("🎯 Task Input")
        
        # Task input
        task_input = st.text_area(
            "Enter your task for ANUS to execute:",
            value=getattr(st.session_state, 'selected_task', ''),
            height=100,
            placeholder="e.g., calculate 2 + 2, search for python, count words in 'hello world'"
        )
        
        # Execution mode
        mode = st.radio(
            "Execution Mode",
            ["Auto", "Single-Agent", "Multi-Agent"],
            help="Auto: Let ANUS decide based on complexity, Single: Force single agent, Multi: Force multi-agent"
        )
        
        mode_mapping = {"Auto": None, "Single-Agent": "single", "Multi-Agent": "multi"}
        selected_mode = mode_mapping[mode]
        
        # Execute button
        if st.button("🚀 Execute Task", type="primary", disabled=not task_input.strip()):
            if task_input.strip():
                result = execute_task(task_input.strip(), selected_mode)
                execution_time = st.session_state.task_history[0]['execution_time']
                display_result(result, execution_time)
    
    with col2:
        st.header("🤖 Framework Info")
        
        # Agent information
        agents = orchestrator.list_agents()
        st.subheader("Available Agents")
        for agent in agents:
            primary_badge = "🌟 PRIMARY" if agent['primary'] else ""
            st.write(f"• **{agent['name']}** ({agent['type']}) {primary_badge}")
        
        # Statistics
        st.subheader("📈 Statistics")
        if st.session_state.task_history:
            total_tasks = len(st.session_state.task_history)
            avg_time = sum(h['execution_time'] for h in st.session_state.task_history) / total_tasks
            
            st.metric("Total Tasks", total_tasks)
            st.metric("Avg. Execution Time", f"{avg_time:.3f}s")
            
            # Mode distribution
            modes = [h['result'].get('mode', 'unknown') for h in st.session_state.task_history]
            mode_counts = {mode: modes.count(mode) for mode in set(modes)}
            
            st.subheader("🔄 Mode Distribution")
            for mode, count in mode_counts.items():
                st.write(f"• {mode}: {count}")
    
    # Task History
    if st.session_state.task_history:
        st.header("📜 Task History")
        
        for i, history_item in enumerate(st.session_state.task_history[:10]):
            with st.expander(f"Task {i+1}: {history_item['task'][:50]}..."):
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.write(f"**Mode:** {history_item['result'].get('mode', 'unknown')}")
                with col2:
                    st.write(f"**Time:** {history_item['execution_time']:.3f}s")
                with col3:
                    st.write(f"**Iterations:** {history_item['result'].get('iterations', 0)}")
                
                st.write(f"**Answer:** {history_item['result'].get('answer', 'No answer')}")
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center'>
        <p>🍑 <strong>ANUS Framework</strong> - Autonomous Networked Utility System</p>
        <p>Built with ❤️ and a sense of humor</p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()