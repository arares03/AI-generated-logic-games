import os
import re
import subprocess
import time
import random
from tkinter import messagebox

import google.generativeai as genai
import tkinter as tk
from gen import generatePropositionalLogic

genai.configure(api_key="im not putting this on gh")

model = genai.GenerativeModel("gemini-1.5-flash")

import random

def return_true_with_probability():
    return random.random() < 0.8


def run_prover9():
    original_directory = os.getcwd()

    prover9_directory = "./"

    os.chdir(prover9_directory)

    command = "./prover9 -f ./myProver9.in > ./myProver9.out"
    try:
        subprocess.run(command, shell=True, check=True)
        print("Command executed successfully")
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
    finally:
        os.chdir(original_directory)
        print(f"Returned to original directory: {original_directory}")

def clean_statements(statements):
    all_statements = "\n".join(statements)

    cleaned_statements = re.sub(r"Statement \d+: ", "", all_statements)

    statement_list = cleaned_statements.split("\n")

    statement_list = [statement.strip() + "." if not statement.strip().endswith('.') else statement.strip() for statement in statement_list]

    return "\n".join(statement_list)

def generate_logic_statements():
    odds = return_true_with_probability()
    prover9_statement, prover9_goal = generatePropositionalLogic(odds)
    return prover9_statement, prover9_goal

def generate_story():
    global generated_statements
    global generated_goal

    genre_text = genre_input.get()
    generated_statements, generated_goal = generate_logic_statements()
    print(generated_statements)
    statements_text = generated_statements


    prompt = (f"if i give you some propositional logic statements, can you create a story with following genre: {genre_text}, {statements_text}. Please format with Statement: text_of_statement but do not include the propositional logic. Please include only the story and their statement number, nothing else."
              f"This is the conclusion that should be reached, and you should make it as a final question in such a manner that someone is in doubt whether it is possible or not: Goal of {generated_goal} is true")
    response = model.generate_content(prompt)

    result_text.delete(1.0, "end")
    result_text.insert("end", response.text)

def possible_button_click():
    file_path = "./myProver9.in"

    statements = clean_statements(generated_statements)

    content = f"""
formulas(assumptions).
{statements}
end_of_list.

formulas(goals).
{generated_goal}.
end_of_list.
    """

    try:
        with open(file_path, "w") as file:
            file.write(content)
        print(f"Content written to {file_path}")
    except Exception as e:
        print(f"Error writing to file: {e}")

    time.sleep(1)
    run_prover9()

    time.sleep(2)

    output_file_path = "./myProver9.out"

    if os.path.exists(output_file_path):
        with open(output_file_path, "r") as output_file:
            content = output_file.read()

            if "THEOREM PROVED" in content:
                root = tk.Tk()
                root.withdraw()
                messagebox.showinfo("Result", "You're right!")
                root.destroy()
            else:
                messagebox.showinfo("Result", "You're wrong!")
                print("Theorem not proved.")
    else:
        print(f"Output file {output_file_path} not found.")

def not_possible_button_click():
    file_path = "./myProver9.in"

    statements = clean_statements(generated_statements)

    content = f"""
formulas(assumptions).
{statements}
end_of_list.

formulas(goals).
{generated_goal}.
end_of_list.
        """

    try:
        with open(file_path, "w") as file:
            file.write(content)
        print(f"Content written to {file_path}")
    except Exception as e:
        print(f"Error writing to file: {e}")

    time.sleep(1)
    run_prover9()

    time.sleep(2)

    output_file_path = "./myProver9.out"

    if os.path.exists(output_file_path):
        with open(output_file_path, "r") as output_file:
            content = output_file.read()

            if "THEOREM PROVED" in content:
                root = tk.Tk()
                root.withdraw()
                messagebox.showinfo("Result", "You're wrong!")
                root.destroy()
            else:
                messagebox.showinfo("Result", "You're right!")
                print("Theorem not proved.")
    else:
        print(f"Output file {output_file_path} not found.")

root = tk.Tk()
root.title("AI Story Generator")

genre_label = tk.Label(root, text="Enter Genre:")
genre_label.pack()

genre_input = tk.Entry(root, width=150)
genre_input.pack()

generate_button = tk.Button(root, text="Generate Story", command=generate_story)
generate_button.pack()

result_label = tk.Label(root, text="Generated Story:")
result_label.pack()

result_text = tk.Text(root, height=25, width=150)
result_text.pack()

possible_button = tk.Button(root, text="Possible", command=possible_button_click)
possible_button.pack(side="left", padx=10)

not_possible_button = tk.Button(root, text="Not Possible", command=not_possible_button_click)
not_possible_button.pack(side="left", padx=10)

root.mainloop()
