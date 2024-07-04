from voyager import Voyager

mc_port = 

deepseek = Voyager(
    mc_port=mc_port,
    max_iterations=1000,
    ckpt_dir="deepseek-coder-v2",
    server_port=3000,
    action_agent_model_name="deepseek-coder-v2",
    resume=False
)
deepseek.learn(reset_env=False)