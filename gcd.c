//this is a comment, to be annoying
int main() {
    int i = getint(), j = getint();
    while (i != j) {
      if (i > j) i = i - j;
      else j = j - i;
    }
    putint(i);
  }
