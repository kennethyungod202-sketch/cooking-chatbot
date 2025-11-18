"""
Setup script for the Cooking Chatbot project.
Helps with initial configuration and database setup.
"""

import os
import subprocess
import sys
from pathlib import Path


def run_command(command, description):
    """Run a shell command and handle errors."""
    print(f"\n{'='*60}")
    print(f"📍 {description}")
    print(f"{'='*60}")
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"✅ {description} completed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error during {description}: {e}")
        return False


def setup_project():
    """Main setup function."""
    print("\n")
    print("╔" + "="*58 + "╗")
    print("║" + " "*15 + "🍳 Cooking Chatbot Setup" + " "*18 + "║")
    print("╚" + "="*58 + "╝")

    # Check Python version
    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ is required!")
        sys.exit(1)

    # Check if venv exists
    if not Path("venv").exists():
        print("⚠️  Virtual environment not found!")
        print("Please create a virtual environment first:")
        print("\nWindows (PowerShell):")
        print("  python -m venv venv")
        print("  .\\venv\\Scripts\\Activate.ps1")
        print("\nmacOS/Linux:")
        print("  python3 -m venv venv")
        print("  source venv/bin/activate")
        sys.exit(1)

    # Install dependencies
    if not run_command("pip install -r requirements.txt", "Installing dependencies"):
        sys.exit(1)

    # Check if .env exists
    if not Path(".env").exists():
        print("\n⚠️  .env file not found!")
        print("Creating .env from template...")
        if Path(".env.example").exists():
            with open(".env.example", "r") as f:
                content = f.read()
            with open(".env", "w") as f:
                f.write(content)
            print("✅ .env file created!")
            print("\n📝 Please edit .env file and add your OpenAI API key!")
            print("   Get it from: https://platform.openai.com/api-keys")
        else:
            print("❌ .env.example file not found!")
            sys.exit(1)
    else:
        print("\n✅ .env file already exists")

    # Run migrations
    if not run_command("python manage.py migrate", "Running database migrations"):
        sys.exit(1)

    # Collect static files
    if not run_command("python manage.py collectstatic --noinput", "Collecting static files"):
        print("⚠️  Warning: Static files collection had issues, but continuing...")

    print("\n")
    print("╔" + "="*58 + "╗")
    print("║" + " "*20 + "✅ Setup Complete!" + " "*20 + "║")
    print("╚" + "="*58 + "╝")

    print("\n📋 Next Steps:")
    print("1. Edit .env file with your OpenAI API key")
    print("2. Run: python manage.py runserver")
    print("3. Open: http://127.0.0.1:8000/")
    print("\n💡 To create an admin account (optional):")
    print("   python manage.py createsuperuser")
    print("   Then visit: http://127.0.0.1:8000/admin/")
    print("\n")


if __name__ == "__main__":
    setup_project()
