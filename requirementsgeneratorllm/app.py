"""Module containing the code to the user app"""

import streamlit as st

from requirementsgeneratorllm.prompt_builder import build_prompts
from requirementsgeneratorllm.prompt_executor import execute_prompts
from requirementsgeneratorllm.requirements_writer import save_requirements
from requirementsgeneratorllm.constants import COUNTRIES, LANGUAGES, REQUIREMENT_TYPES

st.title("LLM-Powered Requirements Generator")

st.markdown(
    """
This tool helps you generate technical requirements based on [IREB](https://www.ireb.org/en/) best practices, using LLMs.
"""
)

# Project Description
project_description = st.text_area("Describe your software:", height=200)

# Requirement Types
selected_requirements_types = st.multiselect(
    "Select the requirement types you want to generate:",
    sorted(REQUIREMENT_TYPES.keys()),
)
# Requirement Type Descriptions
with st.expander("Requirement Type Descriptions"):
    for req_type, req_desc in sorted(REQUIREMENT_TYPES.items()):
        st.markdown(
            f"<div style='font-size: 0.85em;'><b>{req_type}</b>: {req_desc.description}</div>",
            unsafe_allow_html=True,
        )

# Deployment Countries
selected_countries = st.multiselect(
    "Select countries where the application will be deployed:", COUNTRIES
)

# Requirements Language
selected_language = st.selectbox("Select the requirements language:", LANGUAGES)


# Submit Button
if st.button("Generate Requirements"):
    if (
        not project_description
        or not selected_requirements_types
        or not selected_language
    ):
        st.error("Please complete all fields before generating requirements.")
    else:
        with st.spinner("Generating requirements using LLM..."):
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

            st.success("Prompt generated and requirements saved.")
            st.download_button(
                "Download Requirements",
                data="\n".join(answers),
                file_name=FILEPATH,
            )
