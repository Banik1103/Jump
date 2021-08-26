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
using namespace std;
"""

    def add_loop(self, code: List[str]):
        self.loops.append(code)

    def finish(self):
        self.result += r"""void startLoops() {
vector<pair<int,string>> loops = {"""
        for i, k in enumerate(self.loops):
            self.result += f"""pair({i},"todo"),"""
        self.result += "};"
        self.result += r"""
for (auto o : loops) cout << o.first << '|' << o.second << '\n';
}
int main(void) {
    startLoops();
    return 0;
}
"""
