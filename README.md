# Streamlit LLM

This is a Streamlit app that allows you to upload an document or audio file and ask questions about its content. It uses the Llama Index framework, powered by OpenAI's ChatGPT and Hugging Face's Sentence Transformers model, to perform semantic search and provide answers based on your queries.

# Preview
![image](https://github.com/navopw/streamlit-llm/assets/6507938/9eaa95fc-2767-4c66-97fc-8f6e0d4c17e7)

# Supported file types

- All types of raw text documents
- PDF documents
- Audio files (mp3, wav, ogg)
- Video file (mp4)

# Prerequisites

For audio transcription, you need to have [ffmpeg](https://ffmpeg.org/) installed on your system.

# Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/navopw/streamlit-llm.git
   ```

2. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

3. Set up environment variables:

   - Create a file named `.env` in the root directory of the project.
   - Add your OpenAI API key to the `.env` file:

     ```text
     OPENAI_API_KEY=your_api_key
     ```

## Usage

1. Run the Streamlit app:

   ```shell
   ./start.sh <host> <port>
   ```

## License

This project is licensed under the MIT License.
