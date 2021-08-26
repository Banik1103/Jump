from codegen.model import CodeGen

if __name__ == "__main__":
    model = CodeGen()
    model.add_loop(["adccs", "sihasjkv"])
    model.add_loop(["aod", "0028e03", "sidjao", "sdio"])
    model.add_loop([])
    model.finish()
    print(model.result)
