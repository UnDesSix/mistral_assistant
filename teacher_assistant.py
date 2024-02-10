import requests
import os


def import_file_to_string(file_path):
    """
    Reads the contents of a file and returns it as a string.

    Parameters:
        file_path (str): The path to the file to be read.

    Returns:
        str: The contents of the file as a string, or None if an error occurs.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

    return None


def write_to_file(file_name, content):
    """
    Writes the given content to a file with the specified file extension.

    :param file_name: The name for the file to be written.
    :param content: The content to write to the file.
    """
    # Open the file with write mode and write the content
    with open(file_name, "w") as file:
        file.write(content)

    print(f"Content written to {file_name}")


def get_mistral_api_response(query: str, model: str = "mistral-medium") -> None:
    """
    Sends a query to the Mistral API and prints the response.

    Parameters:
        query (str): The user query to send to the Mistral API.
        model (str): The Mistral model to use. Defaults to 'mistral-tiny'.
    """
    api_key = os.getenv("API_KEY")
    url = "https://api.mistral.ai/v1/chat/completions"

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {api_key}",
    }

    data = {
        "model": model,
        "messages": [{"role": "user", "content": query}],
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        print("Success:")
        display_response(response.json())
        return response.json()
    else:
        print("Error:", response.status_code)
        print(response.text)


def display_response(response):
    """
    Displays the response from the Mistral API in a readable format.

    Parameters:
        response (dict): The response dictionary from the Mistral API.
    """
    print(response)
    # Check if the response is successful
    if "choices" in response and response["choices"]:
        # Extract the first choice (assuming single completion in this example)
        choice = response["choices"][0]
        message = choice["message"]

        # Print the role and content
        print(f"Role: {message['role']}")
        print("Content:")
        # print(message["content"])
        write_to_file("exercice1.py", message["content"])

        # Optionally, display other information like model used, id, etc.
        print("\nAdditional Information:")
        print(f"Response ID: {response['id']}")
        print(f"Model: {response['model']}")
        print(f"Created at: {response['created']}")
    else:
        print("No response or unexpected format.")


# Example usage
# instruction = """
#     Ecris un ensemble d'exercices, en utilisant le format MarkDown, pour le syllabus ci-apres dans le CONTEXT.
#     Le document ne dois contenir que des exercices.
#     """
# instruction = """
#     Ecris les reponses pour chaque exercice. Separe les reponses par un trait.
#     """
instruction = """
    Donne des explications pour chaque notions presentes dans le code dans le contexte
    """

context = import_file_to_string("./source.md")

footer = ""

query = f"""
    ###INSTRUCTION###
    {instruction}
    ###CONTEXT###
    {context}
    """

response = get_mistral_api_response(query)
