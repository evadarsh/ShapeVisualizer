# shapes/models.py

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        """Abstract method for drawing the shape."""
        pass
