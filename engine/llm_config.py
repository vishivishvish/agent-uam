from langchain_openai import AzureChatOpenAI;

azure_key = "e6cd8b069c0243bb877b9d202fac9f74";
azure_endpoint = "https://llmcoesre-openai.openai.azure.com/";
azure_model = "gpt-5.1";
api_version = "2025-04-01-preview";
temperature = 0;

llm = AzureChatOpenAI\
(
    api_key = azure_key,
    azure_endpoint = azure_endpoint,
    deployment_name = azure_model,
    api_version = api_version,
    temperature = temperature
);

print("All good - engine/llm_config.py now ready to be used");