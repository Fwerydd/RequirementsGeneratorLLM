"""Module to write requirements in a output file"""

from typing import List


def save_requirements(
    project_settings: str,
    requirements_text: List[str],
    filename: str = "requirements.txt",
) -> str:
    """Save requirements in a file

    Args:
        project_settings (str): Configuration of the software for the generation
        requirements_text (str): Requirements LLM answers
        filename (str, optional): Output filename. Defaults to "requirements.txt".

    Returns:
        str: _description_
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(project_settings)
        f.writelines(
            [req.replace("#", "").replace("*", "") for req in requirements_text]
        )
    return filename
