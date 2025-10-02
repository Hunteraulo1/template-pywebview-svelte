#!/usr/bin/env python3
"""
Development script to launch the application in development mode
"""
import sys
import subprocess
import time
import threading
from pathlib import Path
from app import app


def start_flask_dev():
    """Start Flask in development mode"""
    print("🐍 Starting Flask server...")
    # Import and start Flask directly without pywebview
    app.run(host='127.0.0.1', port=5000, debug=True, use_reloader=False)


def start_vite_dev():
    """Start Vite in development mode"""
    print("⚡ Starting Vite server...")
    # Use subprocess for better control and ensure --host is used
    try:
        subprocess.run(['pnpm', 'run', 'dev', '--', '--host'], check=True)
    except subprocess.CalledProcessError:
        # Fallback if pnpm fails
        subprocess.run(['npm', 'run', 'dev', '--', '--host'], check=True)


def main():
    """Main function for development mode"""
    print("=" * 50)
    print("🔧 Development Mode - PyWebView + Svelte 5")
    print("=" * 50)

    # Check that dependencies are installed
    if not Path("node_modules").exists():
        print("📦 Installing frontend dependencies...")
        subprocess.run(['pnpm', 'install'], check=True)

    if not Path("requirements.txt").exists():
        print("❌ requirements.txt file not found")
        sys.exit(1)

    print("🚀 Starting development servers...")
    print("📱 Frontend: http://localhost:3000 (or your machine's IP)")
    print("🐍 Backend: http://localhost:5000")
    print("🌐 Open http://localhost:3000 in your browser")
    print("💡 If localhost doesn't work, use the IP displayed by Vite")
    print("\n💡 Press Ctrl+C to stop all servers\n")

    try:
        # Start Flask and Vite in parallel
        flask_thread = threading.Thread(target=start_flask_dev, daemon=True)
        vite_thread = threading.Thread(target=start_vite_dev, daemon=True)

        flask_thread.start()
        time.sleep(2)  # Wait for Flask to start
        vite_thread.start()

        # Wait for threads to finish
        flask_thread.join()
        vite_thread.join()

    except KeyboardInterrupt:
        print("\n👋 Stopping development servers")


if __name__ == "__main__":
    main()
