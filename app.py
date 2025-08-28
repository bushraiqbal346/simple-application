import gradio as gr

# Function to handle form submission
def submit_form(name, email, department, cgpa, interests):
    return f"""
    ✅ Application Submitted Successfully!

    👤 Name: {name}
    📧 Email: {email}
    🏫 Department: {department}
    📊 CGPA: {cgpa}
    🎯 Interests: {interests}
    """

# Gradio Interface
with gr.Blocks() as demo:
    gr.Markdown("## 📝 Engineering Application Form")

    with gr.Row():
        name = gr.Textbox(label="Full Name", placeholder="Enter your full name")
        email = gr.Textbox(label="Email", placeholder="Enter your email")

    with gr.Row():
        department = gr.Dropdown(
            ["Computer Engineering", "Electrical Engineering", "Mechanical Engineering", 
             "Civil Engineering", "Software Engineering"],
            label="Department"
        )
        cgpa = gr.Number(label="CGPA", precision=2)

    interests = gr.Textbox(label="Research / Project Interests", lines=3, placeholder="Write your interests...")

    submit_btn = gr.Button("Submit Application")
    output = gr.Textbox(label="Form Output", lines=8)

    submit_btn.click(submit_form, [name, email, department, cgpa, interests], output)

# Launch the app
if __name__ == "__main__":
    demo.launch()
