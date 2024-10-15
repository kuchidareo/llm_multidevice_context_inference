import os
import random

from openai import OpenAI

activity_comprehension_ex_questions = [
    """
This CSV file provides timestamps along with human activity labels captured by different independent sensors.
Could you help explain step by step what might have happened and determine what situation the person might be in?
    """,
    """
Based on the context, what might have happened
    """,
]
duration_comprehension_ex_questions = [
        """
This CSV file provides timestamps along with human activity labels captured by different independent sensors.
Calculate the duration of each activity: Relaxing, Coffee time, Early morning, Cleanup, and Sandwich time.
    """,
]

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_response(conversation, gpt_model):
    response = client.chat.completions.create(
        model=gpt_model,
        messages=conversation
    )

    return response.choices[0].message.content

def generate_llm_conversation(gpt_model, questions):
    conversation = [{"role": "system", "content": "You are a helpful assstant. You'll read sensor label table and analyze what might have happened."}]
    
    for question in questions:
        conversation.append({"role": "user", "content": question})
        answer = get_response(conversation, gpt_model)
        conversation.append({"role": "assistant", "content": answer})

    return conversation

def activity_comprehension_ex(csv_text, gpt_model, misclassified_df, misclassified_row_indices):
    first_question = f"{activity_comprehension_ex_questions[0]}\n{csv_text}"
    random_row_index = random.choice(misclassified_row_indices) if misclassified_row_indices else 0
    relative_time = misclassified_df.loc[random_row_index, "relative_time(s)"]
    second_question = f"{activity_comprehension_ex_questions[1]} at {relative_time} seconds."

    questions = [first_question, second_question]
    conversation = generate_llm_conversation(gpt_model, questions)

    return conversation

def duration_comprehension_ex(csv_text, gpt_model):
    first_question = f"{duration_comprehension_ex_questions[0]}\n{csv_text}"
    questions = [first_question]
    conversation = generate_llm_conversation(gpt_model, questions)

    return conversation