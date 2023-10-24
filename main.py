from src.assembler.image_text_assambler import assemble_image
from src.function_calling.langchain_function_calling import run_agent
from src.image_generation.image_generator import ImageGenerator, create_image_generator, download_and_save_image
from src.gpt.text_generator import request_chat_completion
import logging



# Set up logging
logging.basicConfig(filename='PropagandaAI.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

logger.info('Starting PropagandaAI')
user_prompt: str = input('What shall PropogandaAI generate: ')

answers = run_agent(user_prompt)
logger.info(f"Finished running langchain_function_calling.py, result: {answers}")