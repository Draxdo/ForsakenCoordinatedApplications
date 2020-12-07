#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;

int main (int argc, char** argv) {
	int status;
  if (argc < 1) {
		cout << "Usage: hexa <file>";
		status = 1;
	} else {
		const char* x = "hexa.py ";
		const char* file = argv[1];
		string result = string(x) + string(file);
		char *cstr = &result[0];
		status = system(cstr);
	}

  return status;
}