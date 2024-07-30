from langchain_ollama.llms import OllamaLLM
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field


class Recipe(BaseModel):
    dish_name: str = Field(description="Name of Dish")
    recipe: str = Field(description="Recipe of the dish")


model = OllamaLLM(model="llama3", temperature=0)


def generate_recipe(vegetable, food_style):

    dishname_prompt = PromptTemplate(
    template="""You are a master chef. Specialized in Indian Home Food.
            Give me Only dishname of a {Food} with {Vegetable} in 3 words. Not Recipes""",
    input_variables=["Food", "Vegetable"])
    dishname_chain = dishname_prompt | model 
    
    json_parser = JsonOutputParser(pydantic_object=Recipe)
    
    recipe_prompt = PromptTemplate(
        template="""You are a master chef. Specialized in Indian Home Food. 
              {format_instructions}
              Return Recipe for {dishname} in 3 lines""",
        input_variables=["dishname"],
        partial_variables={"format_instructions": json_parser.get_format_instructions()})
    recipe_chain = dishname_chain | recipe_prompt | model
    
    json_chain = recipe_chain | json_parser
    response = json_chain.invoke({"Vegetable": vegetable, "Food": food_style})
    return response

if __name__ == "__main__":
    print(generate_recipe("Tomato","Gravy for Rotis"))