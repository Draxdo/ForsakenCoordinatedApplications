#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main (int argc, char** argv) {
	int status;
  if (argc < 1) {
		cout << "Usage: hexa <file>";
		status = 1;
	} else {
		file = argv[1];
		status = system("hexa.py " + file);
	}

  return status;
}