# PDF AI

This is a Streamlit app that allows you to upload a PDF document and ask questions about its content. It uses the Llama Index framework, powered by OpenAI's ChatGPT and Hugging Face's Sentence Transformers model, to perform semantic search and provide answers based on your queries.

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/your_username/your_repository.git
   ```

2. Install the required dependencies:

   ```shell
   pip install streamlit llama-index python-dotenv sentence_transformers pypdf
   ```

3. Set up environment variables:

   - Create a file named `.env` in the root directory of the project.
   - Add your OpenAI API key to the `.env` file:

     ```text
     OPENAI_API_KEY=your_api_key
     ```
     
   - Add a password for the app:

     ```text
     PASSWORD=your_password
     ```

## Usage

1. Run the Streamlit app:

   ```shell
   streamlit run app.py
   ```

2. Enter the password you set up in the app.

3. Upload a PDF document by clicking the "Upload your PDF" button.

4. Enter your question in the provided text area.

5. Click the "Send" button to get the answer.

The app will perform semantic search on the uploaded PDF document and provide the answer to your question. It will also display the sources and additional information related to the answer.

Note: Make sure the PDF document is stored in the `data` directory.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
