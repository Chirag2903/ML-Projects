from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv
load_dotenv()

import asyncio
import os
os.environ["GOOGLE_GEMINI_API_KEY"] = os.getenv("GOOGLE_GEMINI_API_KEY")

async def main():
    client = MultiServerMCPClient( 
        {
            "utilityTools":{
                "command":"python",
                "args":["utilityToolsMcpServer.py"],
                "transport":"stdio",
            },
            "currencyConvertor": {
                "url": "http://localhost:8000/mcp",
                "transport": "streamable_http",
            }
        }
    )

    tools=await client.get_tools()
    model = ChatGoogleGenerativeAI(
       model="gemini-2.5-flash",
       temperature=0.3,
       api_key=os.getenv("GOOGLE_GEMINI_API_KEY")
    )
    agent = create_agent(tools=tools, model=model)
    
    utilityTools_response = await agent.ainvoke({
        "messages": [ {"role": "user", "content": "What is 49 degree Celsius in Fahrenheit?"} ]
    })

    print("Utility Tools response:", utilityTools_response['messages'][-1].content)

    currencyConvertor_response = await agent.ainvoke({ 
        "messages":[ {"role":"user", "content": "How much is 10 dollar in indian rupees"} ]
    })
    print("Currency Convertor response:", currencyConvertor_response['messages'][-1].content)

asyncio.run(main())