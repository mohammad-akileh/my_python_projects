from rich.console import Console

# Create a Console object
console = Console()

# Print a bold message in a specific color
console.print("This is a bold message in red.", style="bold red")
x=[1,3,"  ",4,1]
x[x.index("  ")]=4
print(x)