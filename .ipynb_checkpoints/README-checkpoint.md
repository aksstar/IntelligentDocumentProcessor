# Intelligent Financial Document Processor with Gemini 2.5 Flash

## Overview

This project presents an intelligent document processing pipeline designed to automate and enhance the handling of scanned financial documents. Leveraging **Google's Gemini 2.5 Flash**, a powerful and highly efficient multimodal AI model available via Vertex AI, this solution addresses common challenges in document automation, such as poor readability, incorrect orientation, irrelevant content, and data accuracy.

The application systematically processes images to assess readability, auto-correct orientation, intelligently crop relevant sections, suggest quality enhancements, and finally, extract and verify structured data from key financial fields. The entire workflow is presented through an interactive web interface.

## Features

This pipeline orchestrates a series of intelligent steps to clean, analyze, and extract structured data from images:

1.  **Readability Assessment:** Determines if text within the document image is clearly legible, providing a preliminary quality check.
2.  **Auto-Rotation:** Automatically detects and corrects incorrect document orientation (0, 90, 180, 270 degrees) for optimal processing.
3.  **Smart Cropping with Bounding Boxes:** Identifies and crops the most significant text regions or objects to focus processing on relevant content, reducing noise and improving efficiency.
4.  **Image Enhancement Suggestions:** Analyzes image quality and suggests potential enhancements like brightening, sharpening, contrast adjustment, upscaling, or noise removal.
5.  **Structured Data Extraction:** Extracts specific, predefined financial data fields (e.g., Name, Father's Name, PAN Number, Date of Birth) into a reliable JSON format.
6.  **Intelligent Data Verification:** Verifies the presence and validity of extracted key fields, providing a confidence score for the data.

## Business Value for Finance & Banking

Implementing this intelligent document processing pipeline powered by Gemini 2.5 Flash offers substantial advantages for financial institutions:

* **Significant Cost Reduction:** Automates tasks like data entry and validation, drastically reducing manual labor needs and associated operational costs.
* **Accelerated Efficiency & Speed:** Enables faster processing of scanned documents, leading to quicker client onboarding, expedited loan approvals, and more rapid transaction processing.
* **Enhanced Accuracy & Compliance:** Minimizes human error in data extraction and provides automated verification, ensuring higher data quality and consistency crucial for meeting regulatory requirements (e.g., KYC, AML).
* **Improved Customer Experience:** Streamlined backend processes result in faster service for customers, reducing friction in applications and inquiries.
* **Unmatched Scalability:** The AI-driven pipeline can efficiently handle massive volumes of documents without a proportional increase in headcount, supporting growth phases.
* **Better Fraud Detection & Risk Management:** More accurate and validated data provides a stronger foundation for analytics, aiding in the identification of anomalies and potential fraudulent activities.
* **Strategic Resource Reallocation:** By offloading repetitive, low-value tasks to AI, highly skilled staff can be reallocated to more complex, strategic, and customer-facing roles.

## Technical Overview

The core of this solution leverages the `google-generativeai` client library to interact with Gemini 2.5 Flash on Google Cloud's Vertex AI.

* **Multimodal Input:** Images (converted to bytes) are sent alongside text prompts for comprehensive understanding.
* **Structured Output (`response_schema`):** A key feature of Gemini on Vertex AI is the ability to define a JSON schema for the expected response. This enforces strict output formatting, making the model's responses highly reliable and easy to parse programmatically. For instance, the `rotation_angle` is explicitly defined to be one of `"0"`, `"90"`, `"180"`, or `"270"` as strings, a common pitfall without explicit schema definition.
* **Pydantic for Data Validation:** The `BoundingBox` model uses Pydantic to ensure the structural integrity and type correctness of the extracted bounding box data.
* **Interactive UI:** The user interface is built using `Gradio`, providing a simple yet effective way to interact with the pipeline and visualize the processing steps and results.

## Prerequisites

Before you begin, ensure you have the following:

* **Python 3.8+** installed.
* A **Google Cloud Project**.
* **Vertex AI API enabled** in your Google Cloud Project.
* **GCP Authentication:** Set up `gcloud` and authenticate to your project on your local machine.
    ```bash
    gcloud auth application-default login
    gcloud config set project your-project-id
    ```

## Setup & Installation

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/aksstar/IntelligentDocumentProcessor.git
    cd IntelligentDocumentProcessor
    ```

2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    # .\venv\Scripts\activate  # On Windows
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Project ID and Location:**
    Open the `Intelligent Document Processor.ipynb` notebook and update the `PROJECT_ID` and `LOCATION` variables in the second code cell with your specific Google Cloud Project ID and Vertex AI region (e.g., `'us-central1'`).

    ```python
    PROJECT_ID = "your-gcp-project-id"  # e.g., "aakash-test-env"
    LOCATION = "your-gcp-region"      # e.g., "us-central1"
    ```

## Usage

1.  **Start Jupyter Notebook:**
    ```bash
    jupyter notebook
    ```

2.  **Open and Run the Notebook:**
    In the Jupyter interface, open the `Intelligent Document Processor.ipynb` notebook and run the cells sequentially. The Gradio interface will launch in the notebook.
