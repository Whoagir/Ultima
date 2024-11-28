import os
import subprocess
import logging
from datetime import datetime

# Настройка логирования
log_path = r"D:\_teach\_prog\_prog_git\Education\py_commit\auto_commit.log"
logging.basicConfig(
    filename=log_path,
    level=logging.INFO,  # Уровни: DEBUG, INFO, WARNING, ERROR, CRITICAL
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"  # "a" - добавляет новые записи в конец файла
)

repo_path = r"D:\_teach\_obsidian\Riman"


def auto_commit():
    try:
        logging.info("Начало авто коммита.")

        # Разделяем букву диска и оставшийся путь
        disk, path = os.path.splitdrive(repo_path)
        logging.debug(f"Split drive: диск={disk}, путь={path}")

        # Переход на нужный диск
        os.system(f"{disk}")
        logging.debug(f"Перешёл на диск: {disk}")

        # Переход в директорию репозитория
        os.chdir(path)
        logging.info(f"Перешёл в директорию репозитория: {path}")

        # Добавление всех изменений
        subprocess.run(['git', 'add', '.'], check=True)
        logging.info("Добавлены все изменения в индекс.")

        # Создание коммита с текущей датой
        commit_message = f"Auto-commit: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        subprocess.run(['git', 'commit', '-m', commit_message], check=True)
        logging.info(f"Создан коммит с сообщением: {commit_message}")

        # Отправка коммита в удалённый репозиторий
        subprocess.run(['git', 'push'], check=True)
        logging.info("Изменения отправлены в удалённый репозиторий.")

        print("Автокоммит выполнен успешно!")
        logging.info("Автокоммит завершён успешно.")

    except subprocess.CalledProcessError as cpe:
        logging.error(f"Ошибка выполнения команды: {cpe}", exc_info=True)
        print(f"Ошибка выполнения команды: {cpe}")
    except Exception as e:
        logging.error(f"Произошла ошибка: {e}", exc_info=True)
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    logging.info("Запуск скрипта.")
    auto_commit()
