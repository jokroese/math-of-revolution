class Cell {

  float x, y;
  float w;

  
  boolean state;  //true if cooperator
  boolean previous;
  
  float score;

  Cell(float x_, float y_, float w_, boolean state_) {
    x = x_;
    y = y_;
    w = w_;
    
    state = state_;
    previous = state;
  }
  
  void savePrevious() {
    previous = state; 
  }

  void newState(boolean s) {
    state = s;
  }

  void display() {
    if (previous == false && state == true) fill(#FFF47C);  //D>C yellow
    else if (state == true) fill(#66C5F0);  //C>C blue
    else if (previous == true && state == false) fill(#77DE60);  //C>D green
    else fill(#DE2666);  //D>D red
    noStroke();   //no line
    //stroke(0);  //black line
    rect(x, y, w, w);
  }
}