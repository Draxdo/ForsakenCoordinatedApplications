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
  if (argc != 3 && argc != 4) {
		cout << "Usage: hexa <build/run> <file>\n";
		status = 1;
	} else {
		if (string(argv[1]) == "build" || string(argv[1]) == "run") {
			const char* x = "hexa.py ";
			const char* file = argv[2];
			string result = string(x) + string(file);
			char *cstr = &result[0];
			status = system(cstr);
			string y = string(file);
			replace(y, ".hxa", ".py");
			string result3 = "pyinstaller " + y;
			char *cstr3 = &result3[0];
			system(cstr3);
			if (string(argv[1]) == "run") {
				string z = "python3 " + y;
				char *fstr = &z[0];
				if (argc != 4 && argv[3] != "nc") {
					system("clear");
				}
				system(fstr);
			}
			string result4 = "rm " + y;
			char *cstr4 = &result4[0];
			if (argc != 4 && argv[3] != "nd") {
					system(cstr4);
			}
		} else {
			cout << "Unknown stream |" << string(argv[1]) << "|\n";
		}
	}

  return status;
}