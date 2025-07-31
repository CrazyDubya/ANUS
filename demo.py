#!/usr/bin/env python3
"""
ANUS Comprehensive Demo Script

This script demonstrates the full functionality of the ANUS (Autonomous Networked Utility System) framework.
It showcases all tools, both single-agent and multi-agent modes, and various types of tasks.
"""

import os
import sys
import time
import json
from typing import List, Dict, Any

# Add the project root to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from anus.core.orchestrator import AgentOrchestrator
from anus.ui.cli import CLI


class ANUSDemo:
    """Comprehensive demonstration of ANUS capabilities."""
    
    def __init__(self):
        """Initialize the demo with orchestrator and CLI."""
        print("🍑 ANUS Demo - Initializing...")
        self.orchestrator = AgentOrchestrator()
        self.cli = CLI(verbose=True)
        
    def print_section(self, title: str, subtitle: str = ""):
        """Print a formatted section header."""
        print("\n" + "="*80)
        print(f"🍑 {title}")
        if subtitle:
            print(f"   {subtitle}")
        print("="*80)
        
    def execute_and_display(self, task: str, description: str = "", mode: str = None):
        """Execute a task and display the results nicely."""
        if description:
            print(f"\n📝 Description: {description}")
        print(f"🎯 Task: {task}")
        print("⏳ Processing...")
        
        start_time = time.time()
        result = self.orchestrator.execute_task(task, mode=mode)
        end_time = time.time()
        
        print(f"✅ Completed in {end_time - start_time:.2f}s")
        print(f"🔄 Mode: {result.get('mode', 'unknown')}")
        print(f"📊 Answer: {result.get('answer', 'No answer generated')}")
        
        return result
    
    def demo_calculator_tool(self):
        """Demonstrate the calculator tool capabilities."""
        self.print_section("Calculator Tool Demo", "Basic arithmetic operations")
        
        tasks = [
            ("2 + 2", "Simple addition"),
            ("15 * 7", "Multiplication"),
            ("100 / 4", "Division"),
            ("2 ** 8", "Exponentiation"),
            ("(5 + 3) * (10 - 2)", "Complex expression with parentheses"),
            ("42 * 69", "Special numbers (notice the logs)"),
            ("404 / 2", "More special numbers")
        ]
        
        for expression, desc in tasks:
            task = f"calculate {expression}"
            self.execute_and_display(task, desc)
            time.sleep(0.5)
    
    def demo_text_tool(self):
        """Demonstrate the text processing tool capabilities."""
        self.print_section("Text Tool Demo", "Various text processing operations")
        
        tasks = [
            ('count characters in "Hello, ANUS framework!"', "Character counting"),
            ('count words in "This is a comprehensive text processing demo"', "Word counting"),
            ('reverse "ANUS"', "Text reversal"),
            ('uppercase "make this loud"', "Uppercase transformation"),
            ('lowercase "CONVERT THIS TO QUIET"', "Lowercase transformation"),
            ('capitalize "make this title case"', "Title case transformation"),
        ]
        
        for task, desc in tasks:
            self.execute_and_display(task, desc)
            time.sleep(0.5)
    
    def demo_search_tool(self):
        """Demonstrate the search tool capabilities."""
        self.print_section("Search Tool Demo", "Web search simulation")
        
        tasks = [
            ("search for python programming", "Programming language search"),
            ("search for artificial intelligence", "AI topic search"),
            ("search for anus framework", "Framework-specific search (with easter eggs)"),
            ("find information about calculators", "Information retrieval"),
            ("look up machine learning", "Alternative search syntax"),
        ]
        
        for task, desc in tasks:
            self.execute_and_display(task, desc)
            time.sleep(0.5)
    
    def demo_code_tool(self):
        """Demonstrate the code execution tool capabilities."""
        self.print_section("Code Tool Demo", "Python code execution in secure environment")
        
        code_examples = [
            ('print("Hello from ANUS!")', "Simple print statement"),
            ('result = 2 + 2; print(f"2 + 2 = {result}")', "Variable assignment and calculation"),
            ('import math; print(f"Pi is approximately {math.pi:.4f}")', "Using allowed modules"),
            ('numbers = [1, 2, 3, 4, 5]; print(f"Sum: {sum(numbers)}")', "List processing"),
            ('for i in range(3): print(f"ANUS iteration {i}")', "Loop demonstration"),
        ]
        
        for code, desc in code_examples:
            task = f'run code ```python\n{code}\n```'
            self.execute_and_display(task, desc)
            time.sleep(0.5)
    
    def demo_single_vs_multi_agent(self):
        """Demonstrate the difference between single and multi-agent modes."""
        self.print_section("Single vs Multi-Agent Demo", "Comparing execution modes")
        
        # Simple task (should use single-agent)
        print("\n🎯 Simple Task - Should trigger single-agent mode:")
        self.execute_and_display("calculate 5 + 5", "Simple calculation")
        
        # Complex task (should use multi-agent)
        print("\n🎯 Complex Task - Should trigger multi-agent mode:")
        complex_task = "search for python programming and calculate the average length of the results and count words in the first result"
        self.execute_and_display(complex_task, "Multi-step complex task")
        
        # Force single mode on complex task
        print("\n🎯 Complex Task Forced to Single Mode:")
        self.execute_and_display(complex_task, "Same task but forced single-agent", mode="single")
        
        # Force multi mode on simple task
        print("\n🎯 Simple Task Forced to Multi Mode:")
        self.execute_and_display("calculate 3 * 7", "Simple task but forced multi-agent", mode="multi")
    
    def demo_memory_and_context(self):
        """Demonstrate memory and context capabilities."""
        self.print_section("Memory and Context Demo", "Agent memory and task history")
        
        # Execute a few tasks to build history
        self.execute_and_display("calculate 10 + 15", "First calculation")
        self.execute_and_display("search for machine learning", "Search task")
        self.execute_and_display("count characters in \"memory test\"", "Text processing")
        
        # Show task history
        print("\n📚 Task History:")
        history = self.orchestrator.get_task_history(limit=5)
        for i, task_record in enumerate(history, 1):
            print(f"  {i}. {task_record['task']} (Mode: {task_record['mode']}, "
                  f"Time: {task_record['execution_time']:.3f}s)")
        
        # Show agent information
        print("\n🤖 Available Agents:")
        agents = self.orchestrator.list_agents()
        for agent in agents:
            primary_text = " (PRIMARY)" if agent['primary'] else ""
            print(f"  - {agent['name']} ({agent['type']}){primary_text}")
    
    def demo_error_handling(self):
        """Demonstrate error handling capabilities."""
        self.print_section("Error Handling Demo", "How ANUS handles various error conditions")
        
        error_tasks = [
            ("calculate 10 / 0", "Division by zero"),
            ("calculate invalid_expression", "Invalid expression"),
            ('run code ```python\nimport os\n```', "Forbidden import"),
            ('run code ```python\nexec("malicious code")\n```', "Forbidden function"),
        ]
        
        for task, desc in error_tasks:
            try:
                print(f"\n🚨 Testing: {desc}")
                result = self.execute_and_display(task, desc)
                if "error" in str(result).lower():
                    print("✅ Error handled gracefully")
            except Exception as e:
                print(f"❌ Unexpected error: {e}")
    
    def demo_easter_eggs(self):
        """Demonstrate the humorous easter eggs in ANUS."""
        self.print_section("Easter Eggs Demo", "Hidden humor and special responses")
        
        easter_egg_tasks = [
            ("calculate 42", "The meaning of life calculation"),
            ("calculate 69", "Maintaining composure calculation"),
            ("search for anus", "Self-referential search"),
            ("search for jokes", "Humor search"),
            ("status", "System status check"),
            ("clean", "System cleanup"),
            ("expand", "Capability expansion"),
        ]
        
        for task, desc in easter_egg_tasks:
            self.execute_and_display(task, desc)
            time.sleep(0.5)
    
    def demo_performance_metrics(self):
        """Demonstrate performance and metrics."""
        self.print_section("Performance Metrics Demo", "Speed and efficiency analysis")
        
        # Quick tasks
        quick_tasks = [
            "calculate 1 + 1",
            "calculate 2 * 2", 
            "calculate 3 + 3",
            "calculate 4 * 4",
            "calculate 5 + 5"
        ]
        
        print("⚡ Speed Test - Quick Calculations:")
        total_time = 0
        for task in quick_tasks:
            start = time.time()
            self.orchestrator.execute_task(task)
            duration = time.time() - start
            total_time += duration
            print(f"  {task}: {duration:.4f}s")
        
        print(f"📊 Average time per calculation: {total_time/len(quick_tasks):.4f}s")
        print(f"📊 Total time for {len(quick_tasks)} calculations: {total_time:.4f}s")
    
    def run_full_demo(self):
        """Run the complete comprehensive demo."""
        print("🚀 Starting ANUS Comprehensive Demo")
        print("🍑 Autonomous Networked Utility System - Full Functionality Showcase")
        
        # Welcome message
        self.cli.display_welcome()
        
        try:
            # Individual tool demos
            self.demo_calculator_tool()
            self.demo_text_tool()
            self.demo_search_tool()
            self.demo_code_tool()
            
            # Advanced features
            self.demo_single_vs_multi_agent()
            self.demo_memory_and_context()
            self.demo_error_handling()
            self.demo_easter_eggs()
            self.demo_performance_metrics()
            
            # Final summary
            self.print_section("Demo Complete", "ANUS has successfully demonstrated all capabilities")
            print("🎉 All features demonstrated successfully!")
            print("🍑 ANUS is ready for production use!")
            print("\n📖 For more information, check out:")
            print("   - README.md for detailed documentation")
            print("   - examples/ directory for usage examples") 
            print("   - Run 'python -m anus --help' for CLI options")
            print("   - Run 'python -m anus' for interactive mode")
            
        except KeyboardInterrupt:
            print("\n\n🛑 Demo interrupted by user")
        except Exception as e:
            print(f"\n\n❌ Demo error: {e}")
            import traceback
            traceback.print_exc()


def main():
    """Main entry point for the demo."""
    # Check if we're in the right directory
    if not os.path.exists("anus"):
        print("❌ Error: Please run this demo from the ANUS project root directory")
        print("   Example: cd /path/to/ANUS && python demo.py")
        sys.exit(1)
    
    # Run the demo
    demo = ANUSDemo()
    demo.run_full_demo()


if __name__ == "__main__":
    main()