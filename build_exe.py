#!/usr/bin/env python3
"""
Build script to create an executable of the PyWebView + Svelte application
"""
import sys
import subprocess
import shutil
from pathlib import Path

def check_dependencies():
    """Check that all dependencies are installed"""
    print("Checking dependencies...")

    # Check PyInstaller
    try:
        print("OK: PyInstaller installed")
    except ImportError:
        print("ERROR: PyInstaller not installed")
        print("ADVICE: Run: pip install pyinstaller")
        return False

    # Check that frontend is built
    dist_path = Path("dist")
    if not dist_path.exists() or not (dist_path / "index.html").exists():
        print("ERROR: Frontend not built")
        print("ADVICE: Run first: python run.py (to build frontend)")
        return False

    print("OK: Built frontend found")
    return True

def clean_build():
    """Clean old builds"""
    print("Cleaning old builds...")

    # Remove build folder
    build_dir = Path("build")
    if build_dir.exists():
        shutil.rmtree(build_dir)
        print("OK: Build folder removed")

    # Remove old executables
    exe_paths = [Path("dist/app.exe"), Path("dist/app")]
    for exe_path in exe_paths:
        if exe_path.exists():
            exe_path.unlink()
            print(f"OK: Old executable removed: {exe_path}")

def build_executable():
    """Build executable with PyInstaller"""
    print("Building executable...")

    # Check if we are in a virtual environment
    venv_python = Path("venv/bin/python")
    if venv_python.exists():
        print("Using virtual environment...")
        python_cmd = str(venv_python)
    else:
        print("Using system Python...")
        python_cmd = "python"

    try:
        # PyInstaller command via Python
        cmd = [
            python_cmd,
            "-m", "PyInstaller",
            "--clean",
            "--noconfirm",
            "app.spec"
        ]

        print(f"Execution: {' '.join(cmd)}")
        result = subprocess.run(
            cmd, capture_output=True, text=True,
            encoding='utf-8', errors='replace', check=False
        )

        if result.returncode != 0:
            print("ERROR: Build failed")
            print(f"Output: {result.stdout}")
            print(f"Errors: {result.stderr}")
            return False

        print("OK: Executable built successfully")
        
        # Rename executable with version and OS
        rename_executable()
        
        return True

    except (subprocess.SubprocessError, OSError) as e:
        print(f"ERROR: Exception during build: {e}")
        return False

def rename_executable():
    """Rename executable with version and OS"""
    import json
    import platform
    
    # Get version from package.json
    try:
        with open('package.json', 'r') as f:
            data = json.load(f)
            version = data.get('version', '1.0.0')
    except:
        version = '1.0.0'
    
    # Get OS name
    system = platform.system().lower()
    if system == 'windows':
        os_name = 'windows'
        old_name = 'app-temp.exe'
        new_name = f'app-{os_name}-v{version}.exe'
    elif system == 'linux':
        os_name = 'linux'
        old_name = 'app-temp'
        new_name = f'app-{os_name}-v{version}'
    elif system == 'darwin':
        os_name = 'macos'
        old_name = 'app-temp'
        new_name = f'app-{os_name}-v{version}'
    else:
        os_name = 'unknown'
        old_name = 'app-temp'
        new_name = f'app-{os_name}-v{version}'
    
    old_path = Path(f"dist/{old_name}")
    new_path = Path(f"dist/{new_name}")
    
    if old_path.exists():
        old_path.rename(new_path)
        print(f"OK: Renamed executable to {new_name}")
    else:
        print(f"WARNING: Executable {old_name} not found for renaming")

def verify_build():
    """Verify that executable was created correctly"""
    print("Verifying build...")

    # Look for renamed executables with version and OS
    exe_paths = []
    for file in Path("dist").glob("app-*-v*"):
        exe_paths.append(file)
    for file in Path("dist").glob("app-*-v*.exe"):
        exe_paths.append(file)

    exe_path = None
    for path in exe_paths:
        if path.exists():
            exe_path = path
            break

    if not exe_path:
        print("ERROR: Executable not found")
        print("Searching in:")
        for path in exe_paths:
            print(f"  - {path}")
        return False

    size_mb = exe_path.stat().st_size / (1024 * 1024)
    print(f"OK: Executable created: {exe_path}")
    print(f"Size: {size_mb:.1f} MB")
    return True

def clean_external_files():
    """Clean external files after onefile build"""
    print("Cleaning external files...")

    # Files to remove (as they are now integrated into the executable)
    files_to_remove = [
        Path("dist/index.html"),
        Path("dist/assets"),
    ]

    for file_path in files_to_remove:
        if file_path.exists():
            if file_path.is_file():
                file_path.unlink()
                print(f"OK: File removed: {file_path}")
            elif file_path.is_dir():
                shutil.rmtree(file_path)
                print(f"OK: Folder removed: {file_path}")

    print("OK: External files cleaned")

def main():
    """Main function"""
    print("=" * 60)
    print("BUILD EXECUTABLE - PyWebView + Svelte")
    print("=" * 60)

    # Check dependencies
    if not check_dependencies():
        print("\nERROR: Dependency verification failed")
        sys.exit(1)

    # Clean old builds
    clean_build()

    # Build executable
    if not build_executable():
        print("\nERROR: Executable build failed")
        sys.exit(1)

    # Verify build
    if not verify_build():
        print("\nERROR: Build verification failed")
        sys.exit(1)

    # Clean external files (as they are integrated into the executable)
    clean_external_files()

    print("\n" + "=" * 60)
    print("BUILD COMPLETED SUCCESSFULLY!")
    print("=" * 60)

    # Find correct executable name
    exe_paths = [Path("dist/app.exe"), Path("dist/app")]
    exe_name = "app"
    for path in exe_paths:
        if path.exists():
            exe_name = str(path)
            break

    print(f"Executable: {exe_name}")
    print("All files are integrated into the executable!")
    print("You can distribute only this file.")
    print("=" * 60)

if __name__ == "__main__":
    main()
