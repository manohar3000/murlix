#!/usr/bin/env python3
"""
Setup script for Murlix documentation.
This script helps you set up and serve the documentation locally.
"""

import os
import sys
import subprocess
import venv
from pathlib import Path

def run_command(cmd, cwd=None):
    """Run a command and return success status."""
    try:
        result = subprocess.run(cmd, shell=True, cwd=cwd, check=True, 
                              capture_output=True, text=True)
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, e.stderr

def setup_venv():
    """Create and set up virtual environment."""
    venv_path = Path("docs-env")
    
    if not venv_path.exists():
        print("Creating virtual environment...")
        venv.create(venv_path, with_pip=True)
        print("✓ Virtual environment created")
    else:
        print("✓ Virtual environment already exists")
    
    return venv_path

def install_requirements(venv_path):
    """Install documentation requirements."""
    if os.name == 'nt':  # Windows
        pip_path = venv_path / "Scripts" / "pip"
        python_path = venv_path / "Scripts" / "python"
    else:  # Unix/Linux/macOS
        pip_path = venv_path / "bin" / "pip"
        python_path = venv_path / "bin" / "python"
    
    print("Installing documentation requirements...")
    success, output = run_command(f'"{pip_path}" install -r requirements-docs.txt')
    
    if success:
        print("✓ Requirements installed successfully")
        return python_path
    else:
        print(f"✗ Failed to install requirements: {output}")
        return None

def serve_docs(python_path):
    """Serve the documentation locally."""
    print("Starting documentation server...")
    print("Visit http://127.0.0.1:8000 to view the documentation")
    print("Press Ctrl+C to stop the server")
    
    try:
        subprocess.run([str(python_path), "-m", "mkdocs", "serve"], check=True)
    except KeyboardInterrupt:
        print("\n✓ Documentation server stopped")
    except subprocess.CalledProcessError as e:
        print(f"✗ Failed to serve documentation: {e}")

def main():
    """Main setup function."""
    print("🚀 Murlix Documentation Setup")
    print("=" * 40)
    
    # Check if requirements file exists
    if not Path("requirements-docs.txt").exists():
        print("✗ requirements-docs.txt not found!")
        print("Make sure you're running this script from the project root.")
        sys.exit(1)
    
    # Set up virtual environment
    venv_path = setup_venv()
    
    # Install requirements
    python_path = install_requirements(venv_path)
    if not python_path:
        sys.exit(1)
    
    # Ask user what to do
    print("\nWhat would you like to do?")
    print("1. Serve documentation locally (recommended)")
    print("2. Build documentation only")
    print("3. Exit")
    
    choice = input("Enter your choice (1-3): ").strip()
    
    if choice == "1":
        serve_docs(python_path)
    elif choice == "2":
        print("Building documentation...")
        success, output = run_command(f'"{python_path}" -m mkdocs build')
        if success:
            print("✓ Documentation built successfully in 'site' directory")
        else:
            print(f"✗ Build failed: {output}")
    elif choice == "3":
        print("Goodbye! 👋")
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()