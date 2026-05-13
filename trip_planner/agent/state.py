from typing import TypedDict, List, Optional


class AgentState(TypedDict):

    user_query: str

    selected_tool: Optional[str]

    tool_input: Optional[dict]

    tool_output: Optional[str]

    final_response: Optional[str]

    messages: List[str]
