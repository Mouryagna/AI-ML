from langchain_ollama import ChatOllama
from dotenv import load_dotenv
load_dotenv()
from pydantic import BaseModel,Field
from typing import Optional,Literal
model = ChatOllama(model='llama3.1')

#schema
class Review(BaseModel):
    key_theme: list[str]=Field(description="Write down all the key themes discussed in the review in a list")
    summary:str =Field(description="A brief summary of the review")
    sentiment: Literal["pos", "neg"] = Field(
        description="Return sentiment of the review either negative, positive or neutral")
    pros: Optional[list[str]] = Field(default=None, description="Write down all the pros inside a list")
    cons: Optional[list[str]] = Field(default=None, description="Write down all the cons inside a list")
    name: Optional[str] = Field(default=None, description="Write the name of the reviewer")

structured_model=model.with_structured_output(Review)

sample="""
I recently bought the Nova X12 Pro, and my experience has been a mix of pleasant surprises and frustrating compromises. The phone itself feels premium right out of the box, with a sturdy aluminum frame and a vibrant AMOLED display that makes videos and games look fantastic. Performance has been consistently smooth, even while multitasking or playing graphics-intensive games, and the battery comfortably lasts an entire day with moderate to heavy use.

However, the unboxing experience was somewhat disappointing. Although the packaging looked elegant and environmentally friendly, the box contained only the phone, a USB-C cable, and some documentation. There was no charger, no protective case, and not even a pre-applied screen protector. Considering the phone's price, this felt like unnecessary cost-cutting.

The camera performs exceptionally well in daylight, capturing detailed and vibrant photos. Night photography is decent but inconsistent, often producing noisy images in very low-light conditions. The software is generally clean and responsive, but I've encountered a few random bugs, including occasional app crashes and delayed notifications after recent updates.

One thing I truly appreciated was the build quality and the premium feel of both the phone and its packaging. The minimalist box design gave a flagship impression, even though the lack of accessories reduced the excitement of unboxing.

Overall, I would recommend the Nova X12 Pro to users who prioritize performance, display quality, and battery life. On the other hand, buyers expecting a complete in-box package or perfectly polished software may find the experience somewhat disappointing. It's a very capable smartphone, but it still leaves room for improvement.

Review by Mourya
"""

result=structured_model.invoke(sample)

print(result)
#result.name