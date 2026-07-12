from langchain_core.prompts import PromptTemplate

readme_prompt = PromptTemplate(
    input_variables=[
        "project_name",
        "description",
        "tech_stack",
        "features",
        "installation"
    ],

    template="""
You are an expert software engineer and technical documentation writer.

Generate a professional GitHub README.md for the following project.

Project Name:
{project_name}

Project Description:
{description}

Tech Stack:
{tech_stack}

Features:
{features}

Installation:
{installation}

The README should include:

# Project Title

## Description

## Features

## Tech Stack

## Installation

## Usage

## Future Improvements

## Contributing

## License

Return ONLY Markdown.
"""
)