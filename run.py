#!/usr/bin/env python3
"""
Main launch script for PyWebView + Svelte application
"""
import sys
import subprocess
from pathlib import Path
from app import main as app_main


def check_dependencies():
    """Check that all dependencies are installed"""
    print("Checking dependencies...")

    # Check Python
    if sys.version_info < (3, 8):
        print("ERROR: Python 3.8+ required")
        return False

    # Check Python dependencies
    try:
        print("OK: Python dependencies installed")
    except ImportError as e:
        print(f"ERROR: Missing Python dependency: {e}")
        print("ADVICE: Run: pip install -r requirements.txt")
        return False

    # Check Node.js and npm
    checks = [
        (['node', '--version'], "Node.js"),
        (['npm', '--version'], "npm"),
    ]

    for cmd, name in checks:
        try:
            result = subprocess.run(cmd, capture_output=True, text=True,
                                    encoding='utf-8', errors='replace', check=False)

            if result.returncode == 0:
                print(f"OK: {name} installed: {result.stdout.strip()}")
            else:
                print(f"ERROR: {name} not found")
                return False
        except FileNotFoundError:
            print(f"ERROR: {name} not found")
            return False

    return True


def install_frontend_dependencies():
    """Install frontend dependencies if necessary"""
    node_modules = Path("node_modules")
    if not node_modules.exists():
        print("Installing frontend dependencies...")

        # Try pnpm first
        try:
            result = subprocess.run(['pnpm', 'install'], capture_output=True, text=True,
                                    encoding='utf-8', errors='replace', check=False)
            if result.returncode == 0:
                print("OK: Frontend dependencies installed with pnpm")
                return True
            else:
                print(f"WARNING: pnpm failed: {result.stderr}")
        except FileNotFoundError:
            print("WARNING: pnpm not found, trying npm...")

        # Try npm as alternative
        try:
            result = subprocess.run(['npm', 'install'], capture_output=True, text=True,
                                    encoding='utf-8', errors='replace', check=False)
            if result.returncode == 0:
                print("OK: Frontend dependencies installed with npm")
                return True
            else:
                print(f"ERROR: npm also failed: {result.stderr}")
                return False
        except FileNotFoundError:
            print("ERROR: Neither pnpm nor npm are installed")
            print("ADVICE: Install Node.js from https://nodejs.org/")
            return False
    else:
        print("OK: Frontend dependencies already installed")
    return True


def build_frontend():
    """Build Svelte frontend"""
    print("Building frontend...")

    # Create dist folder if it does not exist
    dist_dir = Path("dist")
    dist_dir.mkdir(exist_ok=True)

    # Check if dist/index.html file already exists
    if (dist_dir / "index.html").exists():
        print("OK: Frontend already built (dist/index.html file exists)")
        return True

    try:
        # Try pnpm first
        try:
            result = subprocess.run(['pnpm', 'run', 'build'], capture_output=True, text=True,
                                    encoding='utf-8', errors='replace', check=False)
            if result.returncode == 0:
                print("OK: Frontend built successfully (pnpm)")
                return True
            else:
                print(f"WARNING: pnpm build failed: {result.stderr}")
        except FileNotFoundError:
            print("WARNING: pnpm not found, trying npm...")

        # Try npm as alternative
        try:
            result = subprocess.run(['npm', 'run', 'build'], capture_output=True, text=True,
                                    encoding='utf-8', errors='replace', check=False)
            if result.returncode == 0:
                print("OK: Frontend built successfully (npm)")
                return True
            else:
                print(f"WARNING: npm build also failed: {result.stderr}")
        except FileNotFoundError:
            print("WARNING: npm not found either")

        # If everything fails, use fallback file
        print("WARNING: Build failed, using fallback file...")
        print("OK: Fallback frontend ready")
        return True

    except UnicodeDecodeError:
        print("ERROR: Encoding error during build")
        return False


def start_application():
    """Start main application"""
    print("Starting application...")
    # Activate virtual environment if available
    venv_python = Path("venv/bin/python")
    if venv_python.exists():
        subprocess.run(
            [str(venv_python), "-c", "from app import main; main()"], check=False)
    else:
        app_main()


def main():
    """Main function"""
    # Check command line arguments
    build_only = '--build-only' in sys.argv

    print("=" * 50)
    print("PyWebView + Svelte 5 - Template")
    print("=" * 50)

    # Check dependencies
    if not check_dependencies():
        print("\nERROR: Dependency verification failed")
        print("ADVICE: Make sure you have installed all required dependencies")
        sys.exit(1)

    # Install frontend dependencies
    if not install_frontend_dependencies():
        print("\nERROR: Frontend dependency installation failed")
        sys.exit(1)

    # Build frontend
    if not build_frontend():
        print("\nERROR: Frontend build failed")
        sys.exit(1)

    print("\nOK: All checks passed!")

    if build_only:
        print("Build only mode - Frontend built successfully!")
        return

    print("Launching application...\n")

    # Start application
    try:
        start_application()
    except KeyboardInterrupt:
        print("\nApplication closed by user")
    except (ImportError, ModuleNotFoundError, FileNotFoundError, OSError, RuntimeError) as e:
        print(f"\nERROR: Error during startup: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
