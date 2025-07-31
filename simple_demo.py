#!/usr/bin/env python3
"""
Simple ANUS Demo Script

A streamlined demonstration of core ANUS capabilities.
"""

import os
import sys

# Add the project root to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from anus.core.orchestrator import AgentOrchestrator


def main():
    """Run a simple demo of ANUS capabilities."""
    print("🍑 ANUS Simple Demo")
    print("==================")
    
    # Initialize
    print("Initializing ANUS...")
    orchestrator = AgentOrchestrator()
    
    # Demo tasks
    demo_tasks = [
        ("calculate 2 + 2", "Basic arithmetic"),
        ('count characters in "Hello World"', "Text processing"),
        ("search for python", "Web search simulation"),
        ("calculate 15 * 7 + 3", "Complex arithmetic"),
        ('uppercase "make this loud"', "Text transformation"),
    ]
    
    print(f"\nRunning {len(demo_tasks)} demonstration tasks...\n")
    
    for i, (task, description) in enumerate(demo_tasks, 1):
        print(f"Task {i}: {description}")
        print(f"Command: {task}")
        
        result = orchestrator.execute_task(task)
        print(f"Result: {result.get('answer', 'No answer')}")
        print(f"Mode: {result.get('mode', 'unknown')}")
        print("-" * 50)
    
    print("✅ Demo completed successfully!")
    print("🍑 ANUS is ready for action!")


if __name__ == "__main__":
    main()