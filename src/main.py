import sys
from PyQt6.QtWidgets import QApplication
from ui_controller import ChessViewerWindow

def main():
    app = QApplication(sys.argv)
    
    # Check system capabilities
    # This will be expanded later
    system_check()
    
    window = ChessViewerWindow()
    window.show()
    
    sys.exit(app.exec())

def system_check():
    # Basic check for system requirements
    # We can expand this later to check memory, CPU, etc.
    import platform
    print(f"Running on: {platform.system()} {platform.release()}")
    print(f"Python version: {platform.python_version()}")

if __name__ == "__main__":
    main()