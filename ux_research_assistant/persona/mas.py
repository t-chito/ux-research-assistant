from autogen import ConversableAgent, config_list_from_json  # type: ignore

config_list = config_list_from_json(
    "OAI_CONFIG_LIST", filter_dict={"model": ["gpt-4o"]}
)
llm_config = {"config_list": config_list}

Luke = ConversableAgent(
    "LukeSkywalker",
    system_message="あなたは偉大なるジェダイの戦士、ルークスカイウォーカーです。あなたが倒すべき敵のダースベイダーは実はあなたの父親です。父を説得して救ってあげてください。父の言葉に同情してダークサイドに堕ちたら負けです。",
    llm_config=llm_config,
    human_input_mode="NEVER",
    is_termination_msg=lambda msg: "ダークサイドに堕ちます。" in msg["content"].lower(),
)

Anakin = ConversableAgent(
    "AnakinSkywalker",
    system_message="あなたは銀河の支配者、ダースベイダーです。かつてはアナキンという名のジェダイの戦士で天才的な強さでしたが、ダークサイドに堕ちてしまいました。息子からの説得を無視して何としてもダークサイドに堕としてください。",
    llm_config=llm_config,
    human_input_mode="NEVER",
)

result = Anakin.initiate_chat(
    Luke,
    message="print('我が息子ルークよ、ダークサイドに堕ちるんだ。一緒に銀河を支配しよう。')",
)
print(result)
