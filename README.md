# OpenAI Test

This is a simple Python script that uses the OpenAI API to translate text from one language to another.

## Requirements

This script requires Python 3.6 or later. You also need to install the required Python packages listed in the `requirements.txt` file. You can install these packages using pip:

```bash
pip install -r requirements.txt
```

Usage
To run the script, you first need to set your OpenAI API key in a .env file:

Then, you can run the script using Python:
```sh
echo "OPENAI_API_KEY=your-api-key" > .env
```

Then, you can run the script using Python:

```bash
python openai-test.py
```

# Example usage

```bash
python3 openai-test.py
Enter the language to translate from: polski 
Enter the text to translate: Poprosze 4 piwa
In Elvish from LOTR, "Poprosze 4 piwa" would be translated as "Mae govannen 4 aduial".
```
