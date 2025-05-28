"""Module containing constants"""

from dataclasses import dataclass


@dataclass
class RequirementTypeData:
    """Content of the RequirementType"""

    description: str
    llm_description: str


REQUIREMENT_TYPES = {
    "Functional Requirements": RequirementTypeData(
        description="These guarantee what the system must do to meet the user's needs",
        llm_description="""
Your mission is to help me write detailed functional requirements.
These guarantee what the system must do to meet the user's needs.
Example:
- Business rules
- Certification requirements
- Reporting requirements
- Administrative functions
- Authorization levels
- Audit follow-up
- External interfaces
- Data management
- Legal and regulatory requirements
""",
    ),
    "Security Requirements": RequirementTypeData(
        description="Protecting the system against unauthorized access and ensuring data integrity",
        llm_description="""
Your mission is to help me write non-functional requirements of the security type.
Protecting the system against unauthorized access and ensuring data integrity.
Example:
- Multi-factor authentication
- Data encryption (e.g. AES-256)
- etc.
""",
    ),
    "Usability Requirements": RequirementTypeData(
        description="Aim to make the system easy to learn, use and navigate",
        llm_description="""
Your mission is to help me write non-functional requirements of the usability type.
Aim to make the system easy to learn, use and navigate.
Example:
- Task execution time
- Error rates
- User satisfaction scores
- WCAG (Web Content Accessibility Guidelines)
- etc.
""",
    ),
    "Performance Requirements": RequirementTypeData(
        description="Define the system's responsiveness and ability to handle loads efficiently",
        llm_description="""
Your mission is to help me write non-functional requirements of the performance type.
Define the system's responsiveness and ability to handle loads efficiently.
Example:
- Response time (e.g. < 2 seconds for page loading)
- Throughput (requests per second)
- Resource utilization (CPU, memory)
- etc.
""",
    ),
    "Legal & Regulatory Requirements": RequirementTypeData(
        description="Protecting the system to comply with local laws and requirements",
        llm_description="""
Your mission is to help me write non-functional requirements of the legal and regulatory type.
Protecting the system to comply with local laws and requirements.
Example:
- Compliance with standards such as RGPD or HIPAA
- Compliance with FDA guidances
- etc.
""",
    ),
    "Maintainability Requirements": RequirementTypeData(
        description="Guarantee ease of updating, debugging and modifying, thus facilitating long-term adaptability to changes",
        llm_description="""
Your mission is to help me write non-functional requirements of the maintainability type.
Guarantee ease of updating, debugging and modifying, thus facilitating long-term adaptability to changes.
Example:
- Modularity
- Use of clean code practices
- Updating parts of the system independently
- etc.
""",
    ),
    "Fiability Requirements": RequirementTypeData(
        description="Guarantee system stability and reduce errors during operation, boosting user confidence",
        llm_description="""
Your mission is to help me write non-functional requirements of the fiability type.
Guarantee system stability and reduce errors during operation, boosting user confidence.
Example:
- Mean time between failure (MTBF)
- Mean time to recovery (MTTR)
- etc.
""",
    ),
    "Scalability Requirements": RequirementTypeData(
        description="Ability of the system to expand and meet increasing demands without degrading performance",
        llm_description="""
Your mission is to help me write non-functional requirements of the scalability type.
Ability of the system to expand and meet increasing demands without degrading performance.
Example:
- Horizontal scaling (adding additional servers)
- Vertical scaling (upgrading server power)
- etc.
""",
    ),
    "Portability Requirements": RequirementTypeData(
        description="Ability of the system to operate in different environments or platforms, allowing flexibility in deployment",
        llm_description="""
Your mission is to help me write non-functional requirements of the portability type.
Ability of the system to operate in different environments or platforms, allowing flexibility in deployment.
Example:
- Ease of transferring the system to different operating system or hardware environments
- etc.
""",
    ),
}

COUNTRIES = [
    "Germany",
    "France",
    "United States",
    "United Kingdom",
    "Canada",
    "Japan",
    "Australia",
]

LANGUAGES = ["English", "French"]
