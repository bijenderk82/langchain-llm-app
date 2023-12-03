import openai  # for making OpenAI API requests
 
 
num_stories = 10
prompts = ["Once upon a time,"] * num_stories
 
# batched example, with 10 story completions per request
response = openai.Completion.create(
    model="curie",
    prompt=prompts,
    max_tokens=20,
)
 
# match completions to prompts by index
stories = [""] * len(prompts)
for choice in response.choices:
    stories[choice.index] = prompts[choice.index] + choice.text
 
# print stories
for story in stories:
    print(story)