import os

documentation_template = '''"""
Program: {title}
Description: {description}

Topics covered:
{topics}

Learning Outcomes:
{outcomes}
"""

'''

file_details = {
    "01_basic_range.py": {
        "title": "Basic Range Examples",
        "description": "Demonstration of range() function usage in Python for loops",
        "topics": "1. Using range() with single parameter\n2. Using range() with start and stop\n3. Using range() with step",
        "outcomes": "- Understanding range() function basics\n- Different range() parameters\n- Forward and backward counting"
    },
    "02_nested_loops.py": {
        "title": "Nested Loop Patterns",
        "description": "Examples of nested for loops and their applications",
        "topics": "1. Basic nested loops\n2. Pattern creation\n3. Matrix traversal",
        "outcomes": "- Understanding nested loop structure\n- Creating patterns using nested loops\n- Matrix manipulation"
    },
    "03_pattern_printing.py": {
        "title": "Pattern Printing",
        "description": "Various pattern printing examples using for loops",
        "topics": "1. Triangle patterns\n2. Number patterns\n3. Star patterns",
        "outcomes": "- Understanding pattern logic\n- Nested loop implementation\n- Space and character manipulation"
    },
    "04_list_iteration.py": {
        "title": "List Iteration",
        "description": "Examples of iterating through lists using for loops",
        "topics": "1. List traversal\n2. List element manipulation\n3. Index-based iteration",
        "outcomes": "- Understanding list iteration\n- Accessing list elements\n- List modification techniques"
    },
    "05_string_iteration.py": {
        "title": "String Iteration",
        "description": "Examples of string manipulation using for loops",
        "topics": "1. Character iteration\n2. String analysis\n3. String transformation",
        "outcomes": "- Character-by-character processing\n- String manipulation techniques\n- Building new strings"
    },
    "06_loop_control.py": {
        "title": "Loop Control Statements",
        "description": "Demonstration of break and continue statements in loops",
        "topics": "1. Break statement\n2. Continue statement\n3. Loop control flow",
        "outcomes": "- Control flow manipulation\n- Loop termination\n- Skip iterations"
    },
    "07_sequence_generator.py": {
        "title": "Sequence Generator",
        "description": "Generate various number sequences using for loops",
        "topics": "1. Arithmetic sequences\n2. Geometric sequences\n3. Custom sequences",
        "outcomes": "- Sequence generation logic\n- Pattern recognition\n- Mathematical series"
    },
    "08_multiplication_table.py": {
        "title": "Multiplication Table",
        "description": "Generate multiplication tables using nested loops",
        "topics": "1. Table generation\n2. Formatted output\n3. Range-based multiplication",
        "outcomes": "- Mathematical operations\n- Table formatting\n- Nested loop application"
    },
    "09_sum_series.py": {
        "title": "Sum of Series",
        "description": "Calculate sum of various mathematical series",
        "topics": "1. Series calculation\n2. Mathematical formulas\n3. Running sum",
        "outcomes": "- Series computation\n- Mathematical logic\n- Accumulator pattern"
    },
    "10_factorial_calculator.py": {
        "title": "Factorial Calculator",
        "description": "Calculate factorial of numbers using loops",
        "topics": "1. Factorial computation\n2. Number theory\n3. Loop-based calculation",
        "outcomes": "- Factorial logic\n- Number manipulation\n- Multiplication series"
    },
    "11_fibonacci_series.py": {
        "title": "Fibonacci Series",
        "description": "Generate Fibonacci sequence using loops",
        "topics": "1. Fibonacci sequence\n2. Series generation\n3. Number patterns",
        "outcomes": "- Sequence generation\n- Mathematical patterns\n- Variable manipulation"
    },
    "12_prime_numbers.py": {
        "title": "Prime Numbers",
        "description": "Prime number operations and checks using loops",
        "topics": "1. Prime number testing\n2. Prime generation\n3. Factor checking",
        "outcomes": "- Prime number concepts\n- Optimization techniques\n- Mathematical logic"
    },
    "13_pattern_advanced.py": {
        "title": "Advanced Pattern Printing",
        "description": "Complex pattern printing using nested loops",
        "topics": "1. Complex patterns\n2. Multi-level nesting\n3. Advanced formatting",
        "outcomes": "- Advanced pattern logic\n- Complex nested loops\n- Pattern optimization"
    },
    "14_loop_combinations.py": {
        "title": "Loop Combinations",
        "description": "Combining different types of loops and control statements",
        "topics": "1. Mixed loop types\n2. Control flow combinations\n3. Complex iterations",
        "outcomes": "- Loop interaction\n- Control flow mastery\n- Complex problem solving"
    }
}

def update_file_documentation(filepath, details):
    try:
        with open(filepath, 'r') as file:
            content = file.read()
        
        # Create new content with documentation
        new_content = documentation_template.format(
            title=details["title"],
            description=details["description"],
            topics=details["topics"],
            outcomes=details["outcomes"]
        )
        
        # Remove any existing docstring
        if content.startswith('"""'):
            content = content[content.find('"""', 3) + 3:].strip()
        
        new_content += content
        
        # Write back to file
        with open(filepath, 'w') as file:
            file.write(new_content)
            
        print(f"Updated documentation for {filepath}")
            
    except Exception as e:
        print(f"Error processing {filepath}: {str(e)}")

def main():
    # Get the current directory where the script is located
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Process each .py file in the current directory
    for filename in os.listdir(current_dir):
        if filename.endswith('.py') and filename != 'update_docs.py':
            filepath = os.path.join(current_dir, filename)
            if filename in file_details:
                update_file_documentation(filepath, file_details[filename])
            else:
                print(f"No documentation template found for {filename}")

if __name__ == "__main__":
    main()