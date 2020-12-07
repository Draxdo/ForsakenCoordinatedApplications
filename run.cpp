#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;

bool replace(std::string& str, const std::string& from, const std::string& to) {
    size_t start_pos = str.find(from);
    if(start_pos == std::string::npos)
        return false;
    str.replace(start_pos, from.length(), to);
    return true;
}

int main (int argc, char** argv) {
	int status;
	cout << argc << endl;
  if (argc != 1) {
		cout << "Usage: hexa <file>\n";
		status = 1;
	} else {
		const char* x = "hexa.py ";
		const char* file = argv[1];
		string result = string(x) + string(file);
		char *cstr = &result[0];
		status = system(cstr);
		replace(result, ".hxa", "1.py");
		string result2 = "python3 " + result;
		char *cstr2 = &result2[0];
		system(cstr2);
		string result3 = "pyinstaller " + result;
		char *cstr3 = &result3[0];
		system(cstr3);
		string result4 = "rm " + result;
		char *cstr4 = &result4[0];
		system(cstr4);
	}

  return status;
}