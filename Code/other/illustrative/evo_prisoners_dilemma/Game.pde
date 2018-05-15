class Game {

  int w = 2;  //width of cell
  int columns, rows;

  // Game board
  Cell[][] board;
  
  //Payoff matrix
  float b=1.63;
  float epsilon=0.01;
  float[][] payoffMatrix={  {1,      0},
                            {b,epsilon}  };
                            
  float p=0.9;  //initial density of cooperators


  Game() {
    // Initialize rows, columns and set-up arrays
    columns = width/w;
    rows = height/w;
    board = new Cell[columns][rows];
    init();
  }

  void init() {
    for (int i = 0; i < columns; i++) {
      for (int j = 0; j < rows; j++) {
        
      //with probability 0.5, create a cell that cooperates on first move. Else, defector.
        if(random(0,1)<p) {
          board[i][j] = new Cell(i*w, j*w, w, true);
        }
        else {
          board[i][j] = new Cell(i*w, j*w, w, false);
      }
      
      //comment out to create one defecting cell in the middle
        //if(i==int(columns/2)&&j==int(rows/2)) {
        //    board[i][j] = new Cell(i*w, j*w, w, false);
        //}
        //else {
        //  board[i][j] = new Cell(i*w, j*w, w, true);
        //}
    }
  }
  }

  // Play game against every neighbour
  void play() {
     for ( int i = 0; i < columns;i++) {
      for ( int j = 0; j < rows;j++) {
        board[i][j].savePrevious();
      }
    }
    
    // Loop through every spot in our 2D array and check spots neighbours
    for (int x = 0; x < columns; x++) {
      for (int y = 0; y < rows; y++) {

        // Play game against neighbours (3x3 surrounding grid)
        for (int i = -1; i <= 1; i++) {
          for (int j = -1; j <= 1; j++) {
            int i_= (x+i+columns)%columns;
            int j_= (y+j+rows)%rows;
            //don't play against yourself
            if(x==i_ && y==j_) {
            }  
            else if(board[x][y].previous==true && board[i_][j_].previous==true) {
              board[x][y].score+=1;
            }
            else if(board[x][y].previous==true && board[i_][j_].previous==false) {
              board[x][y].score+=0;
            }
            else if(board[x][y].previous==false && board[i_][j_].previous==true) {
              board[x][y].score+=b;
            }
            else {
              board[x][y].score+=epsilon;
            }
          }
        }
      }
    }
  }
  
  //find best strategy in neighbourhood and adopt
  void adopt() {
    //for each cell
    for ( int x = 0; x < columns;x++) {
      for ( int y = 0; y < rows;y++) {
        
        float bestScore=0;
        int besti=0;
        int bestj=0;
        
        //find the cell in the neighbourhood with the highest score
        for (int i = -1; i <= 1; i++) {
          for (int j = -1; j <= 1; j++) {
            int i_= (x+i+columns)%columns;
            int j_= (y+j+rows)%rows;
            
            if(board[i_][j_].score>bestScore) {
              bestScore=board[i_][j_].score;
              besti=i_;
              bestj=j_;
            }
          }
        }
        //adopt strategy of best neighbour
        board[x][y].newState(board[besti][bestj].previous);
      }
    }     
  }
  
  void resetScores() {
    for ( int i = 0; i < columns;i++) {
      for ( int j = 0; j < rows;j++) {
        board[i][j].score=0;
      }
    }
  }
 
  void display() {
    for ( int i = 0; i < columns;i++) {
      for ( int j = 0; j < rows;j++) {
        board[i][j].display();
      }
    }
  }
}
