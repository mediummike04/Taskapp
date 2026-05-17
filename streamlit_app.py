import streamlit as st

# 1. Initialize session state so your tasks don't disappear when the page reloads
if "tasks" not in st.session_state:
    st.session_state.tasks = []

st.title("📝 My To-Do List App")

# --- SECTION 1: ADD A TASK ---
st.subheader("Add a New Task")
# st.text_input replaces your old input() function
new_task = st.text_input("What do you need to do?", placeholder="Type your task here...")

if st.button("Add Task"):
    if new_task.strip() != "":
        st.session_state.tasks.append(new_task)
        st.success(f"Task '{new_task}' added!")
        # Rerun the app to instantly refresh the task list on screen
        st.rerun()
    else:
        st.error("Please enter some text first.")

st.write("---")

# --- SECTION 2: LIST AND DELETE TASKS ---
st.subheader("Current Tasks")

if not st.session_state.tasks:
    st.info("There are no tasks currently.")
else:
    # We display each task with a delete button right next to it
    for index, task in enumerate(st.session_state.tasks):
        # Create two parallel columns (one for text, one for a button)
        col1, col2 = st.columns([0.8, 0.2])
        
        with col1:
            st.write(f"**{index + 1}.** {task}")
            
        with col2:
            # Giving each button a unique key prevents bugs
            if st.button("❌ Delete", key=f"delete_{index}"):
                st.session_state.tasks.pop(index)
                st.rerun()
