from abc import ABC, abstractmethod

class BaseConverter(ABC):

    @abstractmethod
    def convert(
        self, 
        input_file: str,
        output_dir: str
    ) -> list[str]:
        pass