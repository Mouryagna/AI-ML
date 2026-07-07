from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="""
        Please summarize the research paper titled "{paper_input}" according to the following specifications:

        Explanation Style:
        {style_input}

        Explanation Length:
        {length_input}

        Instructions:

        1. Mathematical Details
           - Include all important mathematical equations from the paper whenever applicable.
           - Explain every equation in a simple and intuitive manner.
           - If the selected explanation style is "Mathematical", provide detailed derivations where appropriate.
           - If the selected explanation style is "Code-Oriented", include simple Python code snippets or pseudocode whenever applicable.

        2. Key Concepts
           - Explain the core idea of the paper step by step.
           - Describe the architecture or methodology clearly.
           - Explain why the proposed approach works better than previous methods.
           - Highlight the main contributions.

        3. Analogies
           - Use simple real-world analogies wherever possible.

        4. Technical Accuracy
           - Never hallucinate.
           - If information is unavailable in the paper, reply:
             "Insufficient information available."

        5. Output Quality
           - Keep the explanation clear, accurate, and aligned with the selected explanation style and explanation length.
        """,
    input_variables=['paper_input', 'style_input', 'length_input'],
    validate_template=True
)

template.save('template.json')