from codegen.model import CodeGen

if __name__ == "__main__":
    model = CodeGen()
    model.add_loop(["int a = 5;", "a++;", "cout << a << \"\\n\\n\";"])
    model.add_loop(["auto b = \"Hello, world!\\n\";", "cout<<b<<b<<b<<'\\n';"])
    model.add_loop([])
    model.finish()
    print(model.result)
