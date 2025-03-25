import chess  # python-chess library

class ChessGameState:
    def __init__(self):
        self.board = chess.Board()
        self.move_history = []
        
    def reset_board(self):
        self.board = chess.Board()
        self.move_history = []
        
    def make_move(self, move_str):
        try:
            move = chess.Move.from_uci(move_str)
            if move in self.board.legal_moves:
                self.board.push(move)
                self.move_history.append(move_str)
                return True, None
            else:
                return False, "Illegal move"
        except ValueError:
            return False, "Invalid move format"
    
    def is_game_over(self):
        return self.board.is_game_over()
    
    def get_board_state(self):
        # Return a representation of the current board state
        return str(self.board)