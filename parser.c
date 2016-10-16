rest() {
  if (lookahead=='+') {
    match('+');
    term();
    putchar('+');
    rest();
  }
  else if (lookahead == '-') {
    match('-');
    term();
    putchar('+');
    rest();
    }
  else;
}
term() {
  if(isdigit(lookahead))
    { putchar(lookahead);
      match(lookahead);
    }
  else error();


}


expr() {
  term(); rest();}
