print("AstPrinter.py loaded")

class AstPrinter:

    def printAst(self, ast, indent=0):
        spacing = "    " * indent

        for node in ast:
            nodeType = node.get("type")

            match nodeType:

                case "Title":
                    print(f"{spacing}Title")
                    self.printNode(node.get("value"), indent + 1)

                case "Function":
                    name = node.get("name", {}).get("value")
                    print(f"{spacing}Function: {name}")
                    self.printNode(node.get("body"), indent + 1)

                case "Process":
                    statement = node.get("statement", {}).get("value")
                    print(f"{spacing}Process: {statement}")

                case "Statement":
                    print(f"{spacing}Statement: {node.get('value')}")

                case "IO":
                    print(f"{spacing}IO")
                    self.printNode(node.get("process"), indent + 1)

                case "If":
                    condition = node.get("condition", {}).get("value")
                    print(f"{spacing}If: {condition}")
                    self.printNode(node.get("body"), indent + 1)

                    for elifNode in node.get("elif", []):
                        self.printNode(elifNode, indent)

                    elseNode = node.get("else")
                    if elseNode:
                        self.printNode(elseNode, indent)

                case "Elif":
                    condition = node.get("condition", {}).get("value")
                    print(f"{spacing}Elif: {condition}")
                    self.printNode(node.get("body"), indent + 1)

                case "Else":
                    print(f"{spacing}Else")
                    self.printNode(node.get("body"), indent + 1)

                case "While":
                    condition = node.get("condition", {}).get("value")
                    print(f"{spacing}While: {condition}")
                    self.printNode(node.get("body"), indent + 1)

                case "For":
                    initialisation = node.get("initialisation", {}).get("value")
                    condition = node.get("condition", {}).get("value")
                    increment = node.get("increment", {}).get("value")

                    print(f"{spacing}For")
                    print(f"{spacing}    Initialisation: {initialisation}")
                    print(f"{spacing}    Condition: {condition}")
                    print(f"{spacing}    Increment: {increment}")

                    self.printNode(node.get("body"), indent + 1)

                case "Options":
                    print(f"{spacing}Options")

                    for option in node.get("options", []):
                        self.printNode(option, indent + 1)

                case "Option":
                    name = node.get("name", {}).get("value")
                    print(f"{spacing}Option: {name}")
                    self.printNode(node.get("body"), indent + 1)

                case "Block":
                    self.printAst(node.get("statements", []), indent)

                case _:
                    print(f"{spacing}Unknown node: {nodeType}")


    def printNode(self, node, indent=0):
        if node is None:
            return

        if isinstance(node, dict):
            self.printAst([node], indent)

        elif isinstance(node, list):
            self.printAst(node, indent)