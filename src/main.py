from config.constant import constant
from shared.logger import get_log

if __name__ == "__main__":
    log = get_log("MAIN")
    log.info(f"RUN {constant.APP_NAME}")
