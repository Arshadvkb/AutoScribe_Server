# AutoScribe Server

> A powerful FastAPI backend service that analyzes text and documents to automatically generate structured study materials using AI.

AutoScribe Server provides API endpoints to process raw text or uploaded documents (PDF, TXT, MD, CSV) and uses Google GenAI to extract key points, create summaries, generate detailed notes, and build text-based mind maps. This makes studying complex topics simpler and more organized.

## Features

*   **Text Analysis**: Direct text input processing for immediate summarization and notes generation.
*   **Document Processing**: Support for uploading and parsing `.pdf`, `.txt`, `.md`, and `.csv` files using PyMuPDF and built-in Python tools.
*   **AI-Powered Insights**: Leveraging AI to automatically generate:
    *   Concise summaries
    *   Detailed, structured notes
    *   Key bullet points
    *   Hierarchical brain maps (mind maps)
*   **CORS Enabled**: Pre-configured for standard frontend development frameworks (e.g., `localhost:3000`, `localhost:5173`).

## Prerequisites

*   Python 3.8+
*   Google GenAI API Key (or specific AI service credentials referenced in your `.env`)

## Getting Started

Follow these steps to set up the project locally.

> [!IMPORTANT]
> Make sure you have the required AI API keys before starting the server, or the analysis endpoints will fail to connect.

1.  **Clone the Repository** and navigate to the project directory:

    ```bash
    git clone <repository-url>
    cd AutoScribe_Server
    ```

2.  **Create and Activate a Virtual Environment**:

    ```bash
    # Create the virtual environment
    python -m venv env

    # Activate on Windows
    .\env\Scripts\activate

    # Activate on Linux/macOS
    source env/bin/activate
    ```

3.  **Install Dependencies**:

    ```bash
    pip install -r req.txt
    ```

4.  **Set Up Environment Variables**: 
    Create a `.env` file in the root of your project directory and add your necessary environment variables:

    ```env
    # Example .env configuration
    GOOGLE_API_KEY=your_genai_api_key_here
    ```

## Usage

Start the FastAPI development server:

```bash
uvicorn main:app --reload
```

The server will be running at `http://127.0.0.1:8000`. You can test the endpoints interactively at `http://127.0.0.1:8000/docs`.

### API Endpoints

*   `GET /ping`: Health check endpoint. Returns `{"ping": "pong"}`.
*   `POST /analyze/text`: Accepts a JSON body with `{"text": "content to analyze"}` and returns structured study materials.
*   `POST /analyze/document`: Accepts a multipart form-data file upload (the `file` field) and returns the corresponding analysis. Supported formats are PDF, TXT, MD, and CSV.
