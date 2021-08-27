from typing import List


class CodeGen:
    def __init__(self):
        self.result: str = ""
        self.loops: List[List[str]] = []
        self.prelude()

    def prelude(self):
        self.result = r"""
#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <functional> 
using namespace std;
typedef vector<pair<int,const function<void (void)>>>VP;
""".strip()

    def add_loop(self, code: List[str]):
        self.loops.append(code)

    def finish(self):
        self.result += r"""
void startLoops() {
VP loops = {"""
        for i, k in enumerate(self.loops):
            fn = ''.join(k)
            fn = fr"""[](){'{' + fn + '}'}"""
            self.result += fr"""pair({i},{fn}),"""
        self.result += "};"
        self.result += r"""
for (auto o : loops){
cout << "In loop #"<< o.first << ':' << '\n';
o.second();
}
}
int main(void) {
    startLoops();
    return 0;
}
"""
