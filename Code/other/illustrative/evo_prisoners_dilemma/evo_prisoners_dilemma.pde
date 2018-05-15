Game game;

void setup() {
  size(displayHeight, displayHeight);
  game = new Game();
}

void draw() {
  background(255);
  frameRate(2);

  game.play();
  game.adopt();
  game.resetScores();
  game.display();
}

// reset board when mouse is pressed
void mousePressed() {
  saveFrame("####.png");
  //game.init(); //comment in to have game reset with click
}
