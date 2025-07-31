#!/usr/bin/env python3
"""
ANUS Interactive Tutorial

This script provides an interactive tutorial for new users to learn about the ANUS framework.
"""

import os
import sys
import time

# Add the project root to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from anus.core.orchestrator import AgentOrchestrator


def print_header(text: str):
    """Print a formatted header."""
    print("\n" + "="*60)
    print(f"🍑 {text}")
    print("="*60)


def print_step(step: int, description: str):
    """Print a step in the tutorial."""
    print(f"\n📍 Step {step}: {description}")
    print("-" * 40)


def wait_for_user():
    """Wait for user to press Enter."""
    input("\n👉 Press Enter to continue...")


def tutorial():
    """Run the interactive tutorial."""
    print_header("Welcome to the ANUS Framework Tutorial!")
    print("""
🎯 This tutorial will walk you through the key features of ANUS
   (Autonomous Networked Utility System)

💡 You'll learn about:
   • Basic tool usage (Calculator, Text, Search, Code)
   • Single vs Multi-agent modes
   • Task complexity assessment
   • Interactive features

🚀 Let's get started!
    """)
    
    wait_for_user()
    
    # Initialize ANUS
    print_step(1, "Initializing ANUS Framework")
    orchestrator = AgentOrchestrator()
    print("✅ ANUS is ready!")
    
    wait_for_user()
    
    # Demonstrate Calculator Tool
    print_step(2, "Calculator Tool Demonstration")
    print("The calculator tool can perform basic arithmetic operations safely.")
    
    calc_examples = [
        ("2 + 2", "Simple addition"),
        ("(10 + 5) * 2", "Complex expression"),
        ("42", "Special number (watch the logs!)"),
    ]
    
    for expr, desc in calc_examples:
        print(f"\n🧮 {desc}: calculate {expr}")
        result = orchestrator.execute_task(f"calculate {expr}")
        print(f"   Result: {result.get('answer', 'Error')}")
        time.sleep(1)
    
    wait_for_user()
    
    # Demonstrate Text Tool
    print_step(3, "Text Processing Tool Demonstration")
    print("The text tool can manipulate and analyze text in various ways.")
    
    text_examples = [
        ('count characters in "Hello ANUS!"', "Character counting"),
        ('reverse "ANUS"', "Text reversal"),
        ('uppercase "quiet voice"', "Make it loud!"),
    ]
    
    for task, desc in text_examples:
        print(f"\n📝 {desc}: {task}")
        result = orchestrator.execute_task(task)
        print(f"   Result: {result.get('answer', 'Error')}")
        time.sleep(1)
    
    wait_for_user()
    
    # Demonstrate Search Tool
    print_step(4, "Search Tool Demonstration")
    print("The search tool simulates web searches with mock results.")
    
    search_examples = [
        ("search for python programming", "Programming search"),
        ("search for anus", "Self-referential search (easter egg!)"),
    ]
    
    for task, desc in search_examples:
        print(f"\n🔍 {desc}: {task}")
        result = orchestrator.execute_task(task)
        answer = result.get('answer', 'Error')
        # Truncate long answers for display
        if len(answer) > 200:
            answer = answer[:200] + "..."
        print(f"   Result: {answer}")
        time.sleep(1)
    
    wait_for_user()
    
    # Demonstrate Mode Selection
    print_step(5, "Single vs Multi-Agent Modes")
    print("ANUS automatically chooses between single and multi-agent modes based on task complexity.")
    
    print("\n🔸 Simple task (single-agent mode):")
    simple_task = "calculate 5 * 5"
    result = orchestrator.execute_task(simple_task)
    print(f"   Task: {simple_task}")
    print(f"   Mode: {result.get('mode', 'unknown')}")
    print(f"   Result: {result.get('answer', 'Error')}")
    
    time.sleep(2)
    
    print("\n🔸 Complex task (multi-agent mode):")
    complex_task = "search for machine learning and analyze the results"
    result = orchestrator.execute_task(complex_task)
    print(f"   Task: {complex_task}")
    print(f"   Mode: {result.get('mode', 'unknown')}")
    answer = result.get('answer', 'Error')
    if len(answer) > 150:
        answer = answer[:150] + "..."
    print(f"   Result: {answer}")
    
    wait_for_user()
    
    # Show task history
    print_step(6, "Task History and Memory")
    print("ANUS keeps track of all executed tasks:")
    
    history = orchestrator.get_task_history()
    print(f"\n📚 Completed {len(history)} tasks in this session:")
    for i, task_record in enumerate(history[-5:], 1):  # Show last 5
        print(f"   {i}. {task_record['task'][:50]}...")
        print(f"      Mode: {task_record['mode']}, Time: {task_record['execution_time']:.3f}s")
    
    wait_for_user()
    
    # Final demonstration
    print_step(7, "Interactive Challenge")
    print("Now it's your turn! Enter a task for ANUS to execute.")
    print("Examples:")
    print("  • calculate 12 * 34 + 56")
    print("  • count words in \"The quick brown fox jumps\"")
    print("  • search for artificial intelligence")
    print("  • reverse \"challenge\"")
    
    while True:
        user_task = input("\n🎯 Enter your task (or 'quit' to exit): ").strip()
        
        if user_task.lower() in ['quit', 'exit', 'q']:
            break
        
        if user_task:
            try:
                print(f"\n⏳ Executing: {user_task}")
                result = orchestrator.execute_task(user_task)
                print(f"✅ Mode: {result.get('mode', 'unknown')}")
                print(f"📊 Result: {result.get('answer', 'No answer')}")
            except Exception as e:
                print(f"❌ Error: {e}")
        else:
            print("Please enter a valid task.")
    
    # Conclusion
    print_header("Tutorial Complete!")
    print("""
🎉 Congratulations! You've completed the ANUS tutorial!

🔗 What's next?
   • Try the web interface: streamlit run web_demo.py
   • Run the full demo: python demo.py
   • Explore the code in the anus/ directory
   • Read the documentation in README.md

🍑 Thank you for exploring ANUS!
   Remember: It's not just a framework, it's a lifestyle choice.
    """)


if __name__ == "__main__":
    tutorial()