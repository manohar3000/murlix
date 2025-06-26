"""
Model configuration and management for Murlix.
"""
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class ModelConfig:
    """Configuration for an AI model."""
    name: str
    display_name: str
    description: str
    is_default: bool = False

class ModelManager:
    """Manages available AI models and their configurations."""
    
    def __init__(self):
        self._models = [
            ModelConfig(
                name="gemini-2.0-flash",
                display_name="Gemini Flash",
                description="Fast responses, good for code completion",
                is_default=True
            ),
            ModelConfig(
                name="gemini-2.0-pro",
                display_name="Gemini Pro",
                description="More capable, better for complex tasks",
                is_default=False
            ),
        ]
        self._current_model = next(m for m in self._models if m.is_default)
    
    @property
    def available_models(self) -> List[ModelConfig]:
        """Get list of available models."""
        return self._models.copy()
    
    @property
    def current_model(self) -> ModelConfig:
        """Get currently selected model."""
        return self._current_model
    
    def set_model(self, model_name: str) -> Optional[ModelConfig]:
        """Set current model by name. Returns None if model not found."""
        for model in self._models:
            if model.name == model_name:
                self._current_model = model
                return model
        return None

# Global instance
model_manager = ModelManager() 