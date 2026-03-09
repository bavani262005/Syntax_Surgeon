import gradio as gr
import autopep8
import ast

def check_syntax(code):
    try:
        ast.parse(code)
        return "No Syntax Error"
    except SyntaxError as e:
        return f"Syntax Error at line {e.lineno}: {e.msg}"

def fix_code(code):
    fixed_code = autopep8.fix_code(code)
    return fixed_code

def explain_code(code):
    if "def" in code:
        return "This code defines a Python function."
    elif "for" in code:
        return "This code uses a for loop."
    elif "while" in code:
        return "This code uses a while loop."
    elif "if" in code:
        return "This code contains a conditional statement."
    else:
        return "Python code detected."

def chatbot(user_input):

    if any(word in user_input for word in ["def","for","if","while","class","import"]):

        syntax = check_syntax(user_input)
        fixed = fix_code(user_input)
        explanation = explain_code(user_input)

        return f"{syntax}\n\nFixed Code:\n{fixed}\n\nExplanation:\n{explanation}"

    else:
        return "Paste Python code and I will check errors."

with gr.Blocks() as demo:

    gr.Markdown("# Syntax Surgeon - AI Code Fixer")

    input_box = gr.Textbox(label="Paste Python Code", lines=10)

    output_box = gr.Textbox(label="Result", lines=10)

    run = gr.Button("Fix Code")
    clear = gr.Button("Clear")

    run.click(chatbot, inputs=input_box, outputs=output_box)
    clear.click(lambda:"", None, output_box)

demo.launch()
