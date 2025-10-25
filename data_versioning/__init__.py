def version_pipeline_step(step_name, description):
    print(f"🔖 Versioning step: {step_name} - {description}")
    return f"version_{step_name.lower().replace(' ', '_')}"
