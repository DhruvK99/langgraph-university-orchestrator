from typing import TypedDict,Optional,Annotated
from langgraph.graph.message import add_messages

class UniversityState(TypedDict):
    messages: Annotated[list,add_messages]
    student_name:Optional[str]
    register_no:Optional[str]
    department:Optional[str]
    query_category: str
    kb_context:str
    