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
			string result = string(x) + string(file) + " &> /dev/null";
			char *cstr = &result[0];
			status = system(cstr);
			string y = string(file);
			replace(y, ".hxa", ".py");
			string result3 = "pyinstaller " + y + " --onefile &> /dev/null";
			string n = string(file);
			replace(n, ".hxa", "");
			string res = "rm -rf /dist/" + n;
			string r2 = "cp dist/" + n + " " + n;
			string r3 = "rm -rf dist/";
			string r4 = "rm -rf build";
			string r5 = "rm " + n + ".spec";
			char *cstrxx = &res[0];
			char *cstr3 = &result3[0];
			char *cstr9 = &r2[0];
			char *cstr8 = &r3[0];
			char *ro = &r4[0];
			char *ro2 = &r5[0];
			system(cstrxx);
			system(cstr3);
			system(cstr9);
			system(cstr8);
			system(ro);
			system(ro2);
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