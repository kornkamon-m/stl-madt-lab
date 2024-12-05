import streamlit as st

# ตั้งค่าหน้าหลัก
st.title("AI Advisory for Food Factory Setup")
st.subheader("Get guidance for setting up your food factory with ease!")

# หน้าหลัก: เมนู
menu = st.sidebar.radio(
    "Navigation",
    ["Homepage", "Input Form", "Document Generator"]
)

if menu == "Homepage":
    st.header("Welcome to AI Advisory System")
    st.write("""
    This system provides step-by-step guidance to help you with:
    - Preparing the required documents
    - Complying with legal and environmental regulations
    - Generating customized documents
    """)

elif menu == "Input Form":
    st.header("Factory Information Form")
    # แบบฟอร์มรวบรวมข้อมูล
    factory_name = st.text_input("Factory Name")
    food_type = st.selectbox(
        "Type of Food",
        ["Frozen Food", "Ready-to-eat", "Snacks", "Others"]
    )
    factory_area = st.number_input("Factory Area (sqm)", min_value=1)
    budget = st.number_input("Budget (in million THB)", min_value=0.1, step=0.1)
    environmental_plan = st.radio(
        "Do you have an Environmental Impact Plan?",
        ["Yes", "No"]
    )
    submit = st.button("Submit Information")

    if submit:
        st.success("Information submitted successfully!")
        st.write("Your inputs:")
        st.write(f"- Factory Name: {factory_name}")
        st.write(f"- Food Type: {food_type}")
        st.write(f"- Factory Area: {factory_area} sqm")
        st.write(f"- Budget: {budget} million THB")
        st.write(f"- Environmental Plan: {environmental_plan}")
        
        # คำแนะนำเกี่ยวกับขั้นตอนการดำเนินงาน
        st.header("Recommended Steps for Your Factory Setup")
        st.write("Based on your inputs, here are the suggested steps:")
        if food_type == "Frozen Food":
            st.write("""
            1. Ensure compliance with GMP and HACCP standards.
            2. Submit a factory layout plan that includes cold storage areas.
            3. Prepare an Environmental Impact Plan if the area exceeds 1,000 sqm.
            """)
        elif food_type == "Ready-to-eat":
            st.write("""
            1. Focus on hygienic design of the production area.
            2. Obtain a Food Safety License from the FDA.
            3. Prepare a waste management plan for organic waste.
            """)
        else:
            st.write("""
            1. Consult a legal advisor for specific regulatory requirements.
            2. Design your factory layout with appropriate zoning.
            3. Ensure worker safety measures are in place.
            """)

elif menu == "Document Generator":
    st.header("Document Generator")
    # Mock example for document creation
    st.write("AI is generating documents based on your input...")
    generate_button = st.button("Generate Documents")
    if generate_button:
        st.success("Documents generated successfully!")
        st.download_button(
            label="Download Environmental Plan",
            data="Sample Environmental Plan Document",
            file_name="environmental_plan.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )
        st.download_button(
            label="Download Process Flow Diagram",
            data="Sample Process Flow Diagram Document",
            file_name="process_flow_diagram.pdf",
            mime="application/pdf"
        )
