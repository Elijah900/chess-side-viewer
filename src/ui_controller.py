from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton
from PyQt6.QtCore import Qt, QPoint
from board_view import ChessBoardView
from chess_logic import ChessGameState
from ascii_parser import AsciiParser

class ChessViewerWindow(QMainWindow):
    def __init__(self):
        super().__init__(None, Qt.WindowType.WindowStaysOnTopHint)
        self.setWindowTitle("Chess Side Viewer")
        self.setGeometry(100, 100, 500, 600)
        
        # Initialize components
        self.game_state = ChessGameState()
        self.ascii_parser = AsciiParser()
        
        # Set up UI
        self.setup_ui()
        
        # Make window draggable
        self.old_pos = None
        
    def setup_ui(self):
        # Main widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        
        # Chess board view
        self.board_view = ChessBoardView()
        main_layout.addWidget(self.board_view)
        
        # Controls layout
        controls_layout = QHBoxLayout()
        
        # Move input
        self.move_input = QLineEdit()
        self.move_input.setPlaceholderText("Enter move (e.g., e2e4 or Nc3)")
        controls_layout.addWidget(self.move_input)
        
        # Move button
        self.move_button = QPushButton("Make Move")
        self.move_button.clicked.connect(self.on_move_button_clicked)
        controls_layout.addWidget(self.move_button)
        
        main_layout.addLayout(controls_layout)
        
        # ASCII input for board state
        self.ascii_input = QLineEdit()
        self.ascii_input.setPlaceholderText("Paste ASCII board representation")
        main_layout.addWidget(self.ascii_input)
        
        # Parse ASCII button
        self.parse_button = QPushButton("Parse Board")
        self.parse_button.clicked.connect(self.on_parse_button_clicked)
        main_layout.addWidget(self.parse_button)
    
    def on_move_button_clicked(self):
        move_text = self.move_input.text().strip()
        if move_text:
            success, error = self.game_state.make_move(move_text)
            if success:
                self.board_view.set_board_state(self.game_state.get_board_state())
                self.move_input.clear()
            else:
                # Show error message
                print(f"Error: {error}")
    
    def on_parse_button_clicked(self):
        ascii_text = self.ascii_input.text()
        if ascii_text:
            board_state = self.ascii_parser.parse_ascii_board(ascii_text)
            # Update the game state and view
            # This will need to be implemented
    
    # Make window draggable
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.old_pos = event.globalPosition().toPoint()
    
    def mouseMoveEvent(self, event):
        if self.old_pos:
            delta = QPoint(event.globalPosition().toPoint() - self.old_pos)
            self.move(self.pos() + delta)
            self.old_pos = event.globalPosition().toPoint()
    
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.old_pos = None