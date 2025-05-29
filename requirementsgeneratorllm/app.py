"""Module containing the code to the user app"""

import streamlit as st

from requirementsgeneratorllm.prompt_builder import build_prompts
from requirementsgeneratorllm.prompt_executor import execute_prompts
from requirementsgeneratorllm.requirements_writer import save_requirements
from requirementsgeneratorllm.constants import COUNTRIES, LANGUAGES, REQUIREMENT_TYPES

st.set_page_config(
    page_title="LLM-Powered Requirements Generator",
    page_icon="📄",
    layout="centered",
)

st.title("LLM-Powered Requirements Generator")

st.markdown(
    """
This tool helps you generate technical requirements based on [IREB](https://www.ireb.org/en/) best practices, using LLMs.
"""
)
st.markdown("---")

# Project Description
project_description = st.text_area(
    label="Describe your software:",
    height=200,
    help="Describe your software's expectations precisely",
)

# Requirements Language
selected_language = st.selectbox(
    label="Select the requirements language:",
    options=sorted(LANGUAGES),
    help="Choose the language of the requirements.",
)


# Requirement Types
selected_requirements_types = st.multiselect(
    label="Select the requirement types you want to generate:",
    options=sorted(REQUIREMENT_TYPES.keys()),
    help="Choose the categories of requirements to be generated.",
)
# Requirement Type Descriptions
with st.expander(
    "Requirement Type Descriptions", icon=":material/keyboard_arrow_down:"
):
    for req_type, req_desc in sorted(REQUIREMENT_TYPES.items()):
        st.markdown(
            f"<div style='font-size: 0.85em;'><b>{req_type}</b>: {req_desc.description}</div>",
            unsafe_allow_html=True,
        )

# Deployment Countries
selected_countries = st.multiselect(
    label="Select countries where the application will be deployed (optional):",
    options=sorted(COUNTRIES),
    help="Choose the countries where the software will be deployed.",
)

st.markdown("---")

# Submit Button
disable_button = not (
    project_description and selected_requirements_types and selected_language
)
# Disclaimer note
st.markdown(
    "<p style='font-size: 0.85em; color: gray;'>* When clicking on 'Generate Requirements', you allow Mistral AI to use your data to improve their models.</p>",
    unsafe_allow_html=True,
)
left, middle, right = st.columns(3)
if middle.button("Generate Requirements", type="primary", disabled=disable_button):
    with st.spinner("Generating requirements using Mistral LLM..."):
        prompts = build_prompts(
            project_description=project_description,
            requirement_types=selected_requirements_types,
            selected_countries=selected_countries,
            selected_language=selected_language,
        )
        answers = execute_prompts(prompts=prompts)

        PROJECT_SETTINGS = f"""
            Project description: {project_description},
            Requirement types: {selected_requirements_types},
            Selected countries: {selected_countries},
            Selected language: {selected_language}  
        """

        FILEPATH = save_requirements(
            project_settings=PROJECT_SETTINGS, requirements_text=answers
        )

    st.success("Requirements generated successfully!")
    st.download_button(
        "Download Requirements", data="\n".join(answers), file_name="requirements.txt"
    )
    if answers and len(answers[0].splitlines()) > 10:
        st.markdown("### Preview of Generated Requirements:")
        st.code(
            "\n".join([line for line in answers[0].splitlines()[:10] if line]),
            language="text",
        )
