# ♟️ Chess Game (PyQt5)

A desktop chess game built in **Python** using **PyQt5**.

This project was created to learn object-oriented programming, GUI development, and software architecture by building a chess engine from scratch instead of relying on external libraries.

---

# Features

* 8×8 interactive chess board
* All six chess pieces implemented
* Individual movement validation for every piece
* Turn-based gameplay (White → Black)
* Piece selection and movement using mouse clicks
* Piece capturing
* Sliding-piece collision detection (Rook, Bishop, Queen)
* Modular object-oriented architecture

---

# Project Structure

```text
Chess-Game/
│
├── main.py
├── window.py
├── board.py
├── piece.py
└── README.md
```

---

# File Overview

## main.py

Application entry point.

Responsibilities:

* Creates the QApplication
* Creates the MainWindow
* Starts the application event loop

---

## window.py

Responsible only for the graphical interface.

Responsibilities:

* Creates the chessboard UI
* Displays pieces
* Handles mouse clicks
* Updates the board after moves
* Highlights selected squares

This file **does not contain chess rules**. It only communicates user actions to the Board.

---

## board.py

Contains the core game logic.

Responsibilities:

* Stores the board state
* Places pieces in their starting positions
* Keeps track of turns
* Validates moves through each piece
* Moves pieces
* Handles captures
* Tracks the currently selected square

The Board acts as the controller between the GUI and the chess pieces.

---

## piece.py

Contains every chess piece.

Implemented classes:

* Piece (Abstract Base Class)
* Pawn
* Rook
* Knight
* Bishop
* Queen
* King

Each piece is responsible for validating **its own movement rules**.

Example:

* Pawn knows how pawns move.
* Knight knows how knights move.
* Bishop checks diagonal movement.
* Rook checks horizontal/vertical movement.

This keeps the movement logic independent and easy to extend.

---

# Architecture

The project follows a simple separation of responsibilities.

```text
User Click
      │
      ▼
window.py
      │
      ▼
board.py
      │
      ▼
piece.py
      │
      ▼
Move Valid?
      │
      ▼
Update GUI
```

### Why this design?

Instead of placing all movement rules inside the GUI, each class has a single responsibility.

* **window.py** → Interface
* **board.py** → Game state and turn management
* **piece.py** → Chess movement rules

This makes the project easier to understand, debug, and expand.

---

# Object-Oriented Concepts Used

* Classes
* Inheritance
* Abstract Base Classes (ABC)
* Polymorphism
* Encapsulation
* Properties
* Composition

---

# Current Version

Implemented:

* Piece movement
* Piece captures
* Turn management
* Board setup
* GUI interaction

Planned:

* Check detection
* Checkmate
* Stalemate
* Castling
* En passant
* Pawn promotion
* Move history
* Game restart
* Undo feature

---

# Technologies

* Python 3
* PyQt5

---

# Purpose

This project was built primarily as a learning exercise to improve Python programming, object-oriented design, GUI development, debugging, and software architecture through the implementation of a complete chess game.