from tkinter import ttk

def make_inputs(form_frame, text_variables):
    for i, field in enumerate(text_variables):
        col = i * 2  # each field uses 2 columns (label + entry)

        ttk.Label(form_frame, text=field["text"]).grid(
            row=0, column=col, padx=5, pady=5
        )
        ttk.Entry(form_frame, textvariable=field["textvariable"]).grid(
            row=0, column=col + 1, padx=5, pady=5
        )
        
        