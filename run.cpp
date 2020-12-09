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
  if (argc != 3) {
		cout << "Usage: hexa <file>\n";
		status = 1;
	} else {
		if (argv[1] == "build" || argv[1] == "run") {
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
			if (argv[1] == "run") {
				string z = y;
				system("clear");
				replace(z, ".py", "");
				string no = z;
			 	z = "./" + z;
				no = "cd " + no; 
				char *cstrx = &no[0];
				char *cstrn = &z[0];
				system(cstrx);
				system(cstrx);
				system(cstrn);
				system("cd ../..");
			}
			string result4 = "rm " + y;
			char *cstr4 = &result4[0];
			system(cstr4);
		}
	}

  return status;
}